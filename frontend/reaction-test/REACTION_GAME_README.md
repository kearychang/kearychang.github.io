# Reaction Time Training Game

A web-based reaction time training game with audio cues and YouTube video background.

## Features

- **YouTube Video Background**: Embedded video at 66% size, centered, autoplay, muted
- **Audio-Based Reaction Training**: React to "talon_strike.mp4" audio cue
- **Mixup System**: Regular audio files can be interrupted by talon strike (30-100ms delay)
- **Difficulty Levels**: Easy, Medium, Hard (affects mixup frequency and silence periods)
- **Customizable Reaction Key**: Set any A-Z key as your reaction button
- **Statistics Tracking**: Shows individual reaction times and average (excluding failures)
- **Failure Detection**: Reactions over 1 second are marked as failures ("-")

## File Structure

```
.
├── reaction_game.html      # Main HTML file
├── reaction_game.css       # Stylesheet
├── reaction_game.js        # Game logic
└── audio/                  # Audio files folder
    ├── talon_strike.mp4   # Special reaction cue (required)
    ├── sound1.mp4         # Regular audio file (optional)
    ├── sound2.wav         # Regular audio file (optional)
    └── ...                # More audio files as needed
```

## Setup

1. **Create Audio Folder**: Create an `audio` folder in the same directory as the HTML file

2. **Add Audio Files**: 
   - Place `talon_strike.wav` in the audio folder (required)
   - Add other MP4/WAV files for mixup audio (optional but recommended)

3. **Open the Game**: 
   - For local testing, you may need to run a local server due to browser security restrictions
   - Use Python: `python -m http.server 8000` then open `http://localhost:8000/reaction_game.html`
   - Or use any other local web server

## How to Play

1. **Start**: Press `Space` to begin the game
2. **Listen**: The game will play random audio files with periods of silence
3. **React**: When you hear `talon_strike.wav`, press your reaction key (default: `R`)
4. **Goal**: React to 10 talon strikes as quickly as possible
5. **Failure**: Reactions over 1 second are marked as failures ("-")

## Settings

- **Difficulty**: 
  - Easy: 10% mixup chance, 1-3s silence
  - Medium: 30% mixup chance, 0.5-2s silence
  - Hard: 50% mixup chance, 0.2-1s silence

- **Reaction Key**: Enter any A-Z letter to change your reaction button

## Game Mechanics

- **Silence Periods**: Random silence between audio clips (varies by difficulty)
- **Mixup System**: Regular audio files can be interrupted after 30-100ms by talon strike
- **Reaction Timing**: Measured from when talon_strike.mp4 starts playing
- **Statistics**: 
  - Individual reaction times displayed in list
  - Average reaction time (excluding failures) shown in blue
  - Failures displayed as "-" in red

## Browser Compatibility

- Modern browsers (Chrome, Firefox, Edge, Safari)
- Requires JavaScript enabled
- Audio playback requires user interaction (Space key press)

## Notes

- The game automatically detects audio files in the `audio` folder
- If audio files aren't detected, check browser console for errors
- YouTube video can be changed by modifying the `src` attribute in the HTML
- For best results, use a local web server instead of opening HTML file directly
