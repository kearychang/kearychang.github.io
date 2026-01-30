# Audio Recorder Script

A Python script for recording audio from your default output device (loopback) with keyboard controls.

## Features

- Lists all available audio output devices on startup
- Records audio from default output source (what's playing on your speakers/headphones)
- Press 'R' to start/stop recording
- Press 'Esc' to exit
- Automatically crops silence from beginning and end of recordings
- Saves recordings as MP4 files with timestamps

## Requirements

### Python Packages

Install the required packages:

```bash
pip install -r requirements_audio_recorder.txt
```

Or manually:

```bash
pip install sounddevice numpy pydub keyboard moviepy
```

### System Dependencies

**Windows:**
- The script uses WASAPI for loopback recording
- You may need to enable "Stereo Mix" or similar loopback device in Windows Sound settings:
  1. Right-click the speaker icon in system tray
  2. Select "Sounds" → "Recording" tab
  3. Right-click in empty space → "Show Disabled Devices"
  4. Enable "Stereo Mix" or your loopback device
  5. Set it as default if needed

**FFmpeg (Required for MP4 conversion):**
- `pydub` and `moviepy` require FFmpeg to be installed
- Download from: https://ffmpeg.org/download.html
- Add FFmpeg to your system PATH
- Or install via package manager:
  - Windows: `choco install ffmpeg` or `scoop install ffmpeg`
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg` (Ubuntu/Debian) or `sudo yum install ffmpeg` (RHEL/CentOS)

## Usage

Run the script:

```bash
python audio_recorder.py
```

### Controls

- **R**: Start/stop recording
- **Esc**: Exit the program

### Output

Recordings are saved in the current working directory with filenames like:
- `recording_20260129_143022.mp4`

The script automatically:
- Crops silence from the beginning and end
- Converts audio to MP4 format with AAC codec

## Troubleshooting

### "No audio data recorded"
- Make sure audio is actually playing on your system
- Check that your loopback device is enabled (see Windows setup above)
- Try adjusting the audio volume

### "Error starting loopback recording"
- Enable "Stereo Mix" or loopback device in Windows Sound settings
- Try running as administrator
- Check that no other application is using the audio device

### "FFmpeg not found"
- Install FFmpeg and ensure it's in your system PATH
- Verify installation: `ffmpeg -version`

### Recording quality issues
- The script uses 44.1kHz sample rate by default
- MP4 files use AAC codec at 192kbps bitrate
- You can modify these settings in the script if needed

## Notes

- The script records in stereo (2 channels) by default
- Silence detection threshold can be adjusted in the `crop_silence` method
- On Windows, loopback recording requires WASAPI support (included with sounddevice)
