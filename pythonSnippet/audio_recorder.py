import pyaudiowpatch as pyaudio
import numpy as np
import keyboard
import os
import threading
import time
from datetime import datetime
from pydub import AudioSegment
from pydub.silence import detect_leading_silence
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Utility for trimming silence
def trim_silence(seg, threshold_offset=-14):
    thresh = seg.dBFS + threshold_offset
    start_trim = detect_leading_silence(seg, silence_threshold=thresh)
    end_trim = detect_leading_silence(seg.reverse(), silence_threshold=thresh)
    return seg[start_trim:len(seg)-end_trim]

class AudioRecorder:
    def __init__(self):
        self.is_recording = False
        self.frames = []
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.loopback_device = None
        self.sample_rate = 44100
        self.channels = 2
        
        # Find the default speakers loopback device
        self._setup_device()

    def _setup_device(self):
        try:
            # Get default WASAPI info
            wasapi_info = self.p.get_host_api_info_by_type(pyaudio.paWASAPI)
            default_speakers = self.p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])
            
            if not default_speakers["isLoopbackDevice"]:
                for loopback in self.p.get_loopback_device_info_generator():
                    # Look for the loopback device associated with the default speakers
                    if default_speakers["name"] in loopback["name"] and loopback["maxInputChannels"] > 0:
                        self.loopback_device = loopback
                        break
            else:
                self.loopback_device = default_speakers

            if self.loopback_device:
                self.sample_rate = int(self.loopback_device["defaultSampleRate"])
                self.channels = self.loopback_device["maxInputChannels"]
                print(f"Found Loopback Device: {self.loopback_device['name']}")
            else:
                print("Error: No loopback device found.")
        except Exception as e:
            print(f"Device Setup Error: {e}")

    def start_recording(self):
        if self.is_recording:
            print("Already recording...")
            return

        if not self.loopback_device:
            print("Cannot start: No loopback device.")
            return

        self.frames = []
        self.is_recording = True
        
        def record_thread():
            try:
                self.stream = self.p.open(
                    format=pyaudio.paInt16,
                    channels=self.channels,
                    rate=self.sample_rate,
                    input=True,
                    input_device_index=self.loopback_device["index"],
                )
                
                print(">>> RECORDING STARTED")
                while self.is_recording:
                    try:
                        data = self.stream.read(1024, exception_on_overflow=False)
                        self.frames.append(data)
                    except Exception as e:
                        print(f"Read error: {e}")
                        break
                
                self.stream.stop_stream()
                self.stream.close()
            except Exception as e:
                print(f"Stream Error: {e}")
                self.is_recording = False

        self.thread = threading.Thread(target=record_thread, daemon=True)
        self.thread.start()

    def stop_recording(self):
        if not self.is_recording:
            return None
        
        self.is_recording = False
        print("Stopping recording...")
        if hasattr(self, 'thread'):
            self.thread.join(timeout=2.0)
        
        if not self.frames:
            return None
        
        return b''.join(self.frames)

    def save(self, raw_data, filename):
        def run_save():
            print(f"Processing audio for {filename}...")
            try:
                seg = AudioSegment(
                    raw_data, 
                    frame_rate=self.sample_rate,
                    sample_width=2,
                    channels=self.channels
                )
                
                trimmed = trim_silence(seg)
                temp_wav = f"temp_{datetime.now().strftime('%f')}.wav"
                trimmed.export(temp_wav, format="wav")
                
                audio_clip = AudioFileClip(temp_wav)
                audio_clip.write_audiofile(filename, codec='aac', bitrate="192k", verbose=False, logger=None)
                audio_clip.close()
                
                if os.path.exists(temp_wav):
                    os.remove(temp_wav)
                    
                print(f"Successfully saved: {filename}")
            except Exception as e:
                print(f"Save Error: {e}")

        save_thread = threading.Thread(target=run_save, daemon=True)
        save_thread.start()

    def close(self):
        self.is_recording = False
        self.p.terminate()

def main():
    rec = AudioRecorder()
    exit_program = threading.Event()

    print("\nControls:")
    print("  [.]   - Start Recording")
    print("  [Esc] - Stop Recording (or Exit if not recording)")
    
    def on_start(e):
        if not rec.is_recording:
            rec.start_recording()

    def on_stop_or_exit(e):
        if rec.is_recording:
            data = rec.stop_recording()
            if data:
                timestamp = datetime.now().strftime("%H%M%S")
                filename = f"game_capture_{timestamp}.mp4"
                rec.save(data, filename)
            else:
                print("No audio captured.")
        else:
            print("Exiting...")
            exit_program.set()

    keyboard.on_press_key('.', on_start)
    keyboard.on_press_key('esc', on_stop_or_exit)
    
    # Wait for the exit event instead of keyboard.wait directly
    while not exit_program.is_set():
        time.sleep(0.1)
    
    rec.close()

if __name__ == "__main__":
    main()