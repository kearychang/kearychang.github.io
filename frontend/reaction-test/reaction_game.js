// Game State
const gameState = {
    isActive: false,
    isWaitingForReaction: false,
    reactionStartTime: null,
    reactionTimes: [],
    talonStrikesPlayed: 0,
    maxTalonStrikes: 10,
    currentAudio: null,
    audioFiles: [],
    talonStrikeFile: null,
    difficulty: 'medium',
    reactionKey: 'r',
    mixupTimeout: null,
    failureThreshold: 350,
    // Web Audio API
    audioContext: null,
    talonStrikeBuffer: null,
    currentAudioSource: null,
    audioStartTime: null
};

// Difficulty Settings
const difficultySettings = {
    easy: {
        mixupChance: 0.1,      // 10% chance of mixup
        minSilence: 1000,       // 1 second minimum silence
        maxSilence: 3000        // 3 seconds maximum silence
    },
    medium: {
        mixupChance: 0.3,      // 30% chance of mixup
        minSilence: 500,       // 0.5 seconds minimum silence
        maxSilence: 2000       // 2 seconds maximum silence
    },
    hard: {
        mixupChance: 0.5,      // 50% chance of mixup
        minSilence: 200,       // 0.2 seconds minimum silence
        maxSilence: 1000       // 1 second maximum silence
    }
};

// Initialize game
function init() {
    // Initialize Web Audio API
    try {
        gameState.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        console.log('Web Audio API initialized');
    } catch (error) {
        console.error('Web Audio API not supported:', error);
        alert('Web Audio API is not supported in this browser. Audio timing may be less accurate.');
    }
    
    loadAudioFiles();
    setupEventListeners();
    updateUI();
    // Initialize YouTube embed with default video ID
    updateYouTubeEmbed('ACtM9ZxJw78');
}

// Load audio file as ArrayBuffer and decode using Web Audio API
async function loadAudioBuffer(url) {
    if (!gameState.audioContext) {
        throw new Error('AudioContext not initialized');
    }
    
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const arrayBuffer = await response.arrayBuffer();
        const audioBuffer = await gameState.audioContext.decodeAudioData(arrayBuffer);
        return audioBuffer;
    } catch (error) {
        console.error(`Error loading audio buffer from ${url}:`, error);
        throw error;
    }
}

// Load audio files from audio folder
async function loadAudioFiles() {
    try {
        const audioFolder = './audio/';
        
        // Try to fetch a manifest file first (if available)
        // Otherwise, try common filenames
        const commonFiles = [
            'auto_attack.wav',
            'cloud_step.wav',
            'dragon_breath.wav',
            'drunken_poet.wav',
            'free_morph.wav',
            'frog.wav',
            'soaring_strike.wav',
            'talon_strike.wav'
        ];
        
        gameState.audioFiles = [];
        gameState.talonStrikeFile = null;
        gameState.talonStrikeBuffer = null;
        
        // Try to load talon_strike using Web Audio API first (for precise timing)
        const talonStrikeVariants = ['talon_strike.wav', 'talon_strike.mp4'];
        let talonStrikeLoaded = false;
        
        if (gameState.audioContext) {
            // Try Web Audio API first for precise timing
            for (const filename of talonStrikeVariants) {
                try {
                    const buffer = await loadAudioBuffer(`${audioFolder}${filename}`);
                    if (!talonStrikeLoaded) {
                        gameState.talonStrikeBuffer = buffer;
                        talonStrikeLoaded = true;
                        console.log(`Loaded talon strike (Web Audio API): ${filename}`);
                        break;
                    }
                } catch (error) {
                    // Try next variant
                    continue;
                }
            }
        }
        
        // Fallback to HTML5 Audio if Web Audio API failed
        if (!talonStrikeLoaded) {
            for (const filename of talonStrikeVariants) {
                const audio = new Audio(`${audioFolder}${filename}`);
                audio.preload = 'auto';
                
                const loadPromise = new Promise((resolve) => {
                    audio.addEventListener('canplaythrough', () => {
                        if (!talonStrikeLoaded) {
                            gameState.talonStrikeFile = audio;
                            talonStrikeLoaded = true;
                            console.log(`Loaded talon strike (HTML5 Audio): ${filename}`);
                            resolve(true);
                        }
                    });
                    
                    audio.addEventListener('error', () => {
                        resolve(false);
                    });
                });
                
                audio.load();
                if (await loadPromise) break;
            }
        }
        
        // Load other audio files (for mixups, HTML5 Audio is fine)
        const loadedPromises = [];
        for (const filename of commonFiles) {
            // Skip talon_strike variants (already loaded)
            if (talonStrikeVariants.includes(filename)) continue;
            
            const audio = new Audio(`${audioFolder}${filename}`);
            audio.preload = 'auto';
            
            const loadPromise = new Promise((resolve) => {
                audio.addEventListener('canplaythrough', () => {
                    gameState.audioFiles.push(audio);
                    console.log(`Loaded audio file: ${filename}`);
                    resolve(true);
                });
                
                audio.addEventListener('error', () => {
                    resolve(false);
                });
            });
            
            audio.load();
            loadedPromises.push(loadPromise);
        }
        
        // Wait a bit for files to load
        await Promise.all(loadedPromises);
        
        // Check if we have the required talon_strike file
        setTimeout(() => {
            if (!gameState.talonStrikeBuffer && !gameState.talonStrikeFile) {
                console.error('ERROR: talon_strike.mp4 or talon_strike.wav not found!');
                alert('ERROR: talon_strike.mp4 or talon_strike.wav is required in the ./audio/ folder');
            } else if (gameState.audioFiles.length === 0) {
                console.warn('Warning: No other audio files found. Game will only play talon_strike.');
            } else {
                console.log(`Loaded ${gameState.audioFiles.length} audio file(s) for mixups`);
            }
        }, 1000);
        
    } catch (error) {
        console.error('Error loading audio files:', error);
    }
}

// Setup event listeners
function setupEventListeners() {
    // Space key to start game
    document.addEventListener('keydown', (e) => {
        if ((e.key === '`' || e.key === 'Backquote') && !gameState.isActive) {
            e.preventDefault();
            startGame();
        }
    });
    
    // Reaction key listener
    document.addEventListener('keydown', handleReactionKey);
    
    // Difficulty selector
    document.getElementById('difficulty-select').addEventListener('change', (e) => {
        if (!gameState.isActive) {
            gameState.difficulty = e.target.value;
        }
    });
    
    // Reaction key input
    const reactionKeyInput = document.getElementById('reaction-key-input');
    reactionKeyInput.addEventListener('input', (e) => {
        const value = e.target.value.toUpperCase();
        if (value.match(/[A-Z]/)) {
            gameState.reactionKey = value.toLowerCase();
            e.target.value = value;
        } else {
            e.target.value = gameState.reactionKey.toUpperCase();
        }
    });
    
    reactionKeyInput.addEventListener('blur', (e) => {
        if (!e.target.value.match(/[A-Z]/)) {
            e.target.value = gameState.reactionKey.toUpperCase();
        }
    });
    
    // Failure threshold radio buttons
    const thresholdRadios = document.querySelectorAll('input[name="failure-threshold"]');
    thresholdRadios.forEach(radio => {
        radio.addEventListener('change', (e) => {
            if (!gameState.isActive) {
                gameState.failureThreshold = parseInt(e.target.value);
            }
        });
    });
    
    // YouTube URL input and Apply button
    const youtubeUrlInput = document.getElementById('youtube-url-input');
    const applyYoutubeBtn = document.getElementById('apply-youtube-btn');
    
    applyYoutubeBtn.addEventListener('click', () => {
        const url = youtubeUrlInput.value.trim();
        if (url) {
            const videoId = extractYouTubeVideoId(url);
            if (videoId) {
                updateYouTubeEmbed(videoId);
                youtubeUrlInput.value = ''; // Clear input after applying
            } else {
                alert('Invalid YouTube URL. Please paste a valid YouTube link.');
            }
        }
    });
    
    // Allow Enter key to apply YouTube URL
    youtubeUrlInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            applyYoutubeBtn.click();
        }
    });
}

// Extract YouTube video ID from various URL formats
function extractYouTubeVideoId(url) {
    if (!url) return null;
    
    // Remove whitespace
    url = url.trim();
    
    // Handle various YouTube URL formats:
    // https://www.youtube.com/watch?v=VIDEO_ID
    // https://youtu.be/VIDEO_ID
    // https://www.youtube.com/embed/VIDEO_ID
    // https://youtube.com/watch?v=VIDEO_ID
    // VIDEO_ID (if just the ID is provided)
    
    let videoId = null;
    
    // Check if it's just a video ID (11 characters, alphanumeric, dashes, underscores)
    if (/^[a-zA-Z0-9_-]{11}$/.test(url)) {
        return url;
    }
    
    // Try to extract from various URL patterns
    const patterns = [
        /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})/,
        /youtube\.com\/watch\?.*v=([a-zA-Z0-9_-]{11})/,
    ];
    
    for (const pattern of patterns) {
        const match = url.match(pattern);
        if (match && match[1]) {
            videoId = match[1];
            break;
        }
    }
    
    return videoId;
}

// Update YouTube embed iframe with new video ID
function updateYouTubeEmbed(videoId) {
    const iframe = document.getElementById('youtube-video');
    if (iframe && videoId) {
        // Build embed URL with autoplay, mute, loop, and other parameters
        const embedUrl = `https://www.youtube.com/embed/${videoId}?enablejsapi=1&autoplay=1&mute=1&loop=1&playlist=${videoId}&controls=0&rel=0`;
        iframe.src = embedUrl;
    }
}

// Handle reaction key press
function handleReactionKey(e) {
    if (!gameState.isActive || !gameState.isWaitingForReaction) {
        return;
    }
    
    const pressedKey = e.key.toLowerCase();
    if (pressedKey === gameState.reactionKey.toLowerCase()) {
        e.preventDefault();
        
        // Otherwise, record reaction (will check if < 100ms for false reaction)
        recordReaction();
    }
}

// Start the game
function startGame() {
    gameState.isActive = true;
    gameState.isWaitingForReaction = false;
    gameState.reactionTimes = [];
    gameState.talonStrikesPlayed = 0;
    
    document.body.classList.add('game-active');
    document.getElementById('header').textContent = 'Game Active - Listen for Talon Strike!';
    document.getElementById('current-status').textContent = 'Listening...';
    
    updateStatsDisplay();
    playNextAudio();
}

// Play next audio (with silence periods and mixups)
function playNextAudio() {
    if (!gameState.isActive) {
        return;
    }
    
    // Check if game is complete
    if (gameState.talonStrikesPlayed >= gameState.maxTalonStrikes) {
        endGame();
        return;
    }
    
    const settings = difficultySettings[gameState.difficulty];
    
    // Period of silence before next audio
    const silenceDuration = Math.random() * (settings.maxSilence - settings.minSilence) + settings.minSilence;
    
    setTimeout(() => {
        if (!gameState.isActive) return;
        
        // Decide what to play
        const shouldPlayTalonStrike = Math.random() < 0.3; // 30% chance to play talon strike directly
        
        if (shouldPlayTalonStrike && (gameState.talonStrikeBuffer || gameState.talonStrikeFile)) {
            playTalonStrike();
        } else if (gameState.audioFiles.length > 0) {
            // Play a regular audio file
            const randomIndex = Math.floor(Math.random() * gameState.audioFiles.length);
            const audio = gameState.audioFiles[randomIndex].cloneNode();
            
            gameState.currentAudio = audio;
            audio.play();
            
            // Mixup logic: after 30-100ms, chance to interrupt with talon strike
            const mixupDelay = Math.random() * 70 + 30; // 30-100ms
            
            gameState.mixupTimeout = setTimeout(() => {
                if (Math.random() < settings.mixupChance && gameState.isActive) {
                    // Stop current audio and play talon strike
                    audio.pause();
                    audio.currentTime = 0;
                    playTalonStrike();
                }
            }, mixupDelay);
            
            audio.addEventListener('ended', () => {
                if (gameState.isActive) {
                    playNextAudio();
                }
            });
        } else {
            // No audio files available, just play talon strike
            if (gameState.talonStrikeBuffer || gameState.talonStrikeFile) {
                playTalonStrike();
            }
        }
    }, silenceDuration);
}

// Play talon strike audio
function playTalonStrike() {
    if (!gameState.isActive) {
        return;
    }
    
    // Check if we have talon strike audio available
    if (!gameState.talonStrikeBuffer && !gameState.talonStrikeFile) {
        return;
    }
    
    // Clear any mixup timeout
    if (gameState.mixupTimeout) {
        clearTimeout(gameState.mixupTimeout);
        gameState.mixupTimeout = null;
    }
    
    // Stop current audio if playing
    if (gameState.currentAudioSource) {
        try {
            gameState.currentAudioSource.stop();
        } catch (e) {
            // Source may already be stopped
        }
        gameState.currentAudioSource = null;
    }
    if (gameState.currentAudio) {
        gameState.currentAudio.pause();
        gameState.currentAudio.currentTime = 0;
        gameState.currentAudio = null;
    }
    
    gameState.isWaitingForReaction = true;
    document.getElementById('current-status').textContent = 
        `TALON STRIKE! Press "${gameState.reactionKey.toUpperCase()}" NOW!`;
    
    // Use Web Audio API for precise timing if available
    if (gameState.audioContext && gameState.talonStrikeBuffer) {
        playTalonStrikeWebAudio();
    } else if (gameState.talonStrikeFile) {
        // Fallback to HTML5 Audio
        playTalonStrikeHTML5();
    }
}

// Play talon strike using Web Audio API (precise timing)
function playTalonStrikeWebAudio() {
    try {
        // Resume audio context if suspended (required by some browsers)
        if (gameState.audioContext.state === 'suspended') {
            gameState.audioContext.resume();
        }
        
        // Create audio source
        const source = gameState.audioContext.createBufferSource();
        source.buffer = gameState.talonStrikeBuffer;
        source.connect(gameState.audioContext.destination);
        
        gameState.currentAudioSource = source;
        
        // Get the precise AudioContext time when audio will start playing
        // AudioContext.currentTime is in seconds and is very precise (sub-millisecond)
        const audioContextStartTime = gameState.audioContext.currentTime;
        
        // Schedule audio to start immediately
        source.start(audioContextStartTime);
        
        // Convert AudioContext time to performance.now() time
        // AudioContext.currentTime starts from 0 when context is created
        // We need to find the offset between AudioContext time and real-world time
        const audioContextTimeNow = gameState.audioContext.currentTime;
        const performanceTimeNow = performance.now();
        
        // Calculate the offset: AudioContext was created at (performanceTimeNow - audioContextTimeNow * 1000)
        // So audioContextStartTime in real-world time is:
        const audioContextCreationTime = performanceTimeNow - (audioContextTimeNow * 1000);
        const actualAudioStartTimeMs = audioContextCreationTime + (audioContextStartTime * 1000);
        
        // Store the precise start time for reaction calculation
        // This is accurate to sub-millisecond precision
        gameState.reactionStartTime = actualAudioStartTimeMs;
        
        // Set timeout for failure (based on threshold)
        const timeoutMs = gameState.failureThreshold;
        setTimeout(() => {
            if (gameState.isWaitingForReaction && gameState.isActive) {
                // Reaction too slow - record as failure
                recordReaction(true);
            }
        }, timeoutMs);
        
        // Handle audio end
        source.onended = () => {
            if (gameState.isActive) {
                if (gameState.isWaitingForReaction) {
                    // Audio ended but no reaction - record as failure
                    recordReaction(true);
                }
                // Play next audio after talon_strike finishes (whether reaction was recorded or not)
                if (gameState.talonStrikesPlayed < gameState.maxTalonStrikes) {
                    playNextAudio();
                }
            }
            gameState.currentAudioSource = null;
        };
        
    } catch (error) {
        console.error('Error playing talon strike with Web Audio API:', error);
        // Fallback to HTML5 Audio
        if (gameState.talonStrikeFile) {
            playTalonStrikeHTML5();
        }
    }
}

// Play talon strike using HTML5 Audio (fallback)
function playTalonStrikeHTML5() {
    const audio = gameState.talonStrikeFile.cloneNode();
    gameState.currentAudio = audio;
    
    // Record start time when audio actually starts playing (more accurate)
    let playEventFired = false;
    audio.addEventListener('play', () => {
        if (!playEventFired) {
            gameState.reactionStartTime = performance.now();
            playEventFired = true;
        }
    }, { once: true });
    
    // Fallback: record before play() in case 'play' event doesn't fire
    gameState.reactionStartTime = performance.now();
    
    audio.play();
    
    // Set timeout for failure (based on threshold)
    setTimeout(() => {
        if (gameState.isWaitingForReaction && gameState.isActive) {
            // Reaction too slow - record as failure
            recordReaction(true);
        }
    }, gameState.failureThreshold);
    
    audio.addEventListener('ended', () => {
        if (gameState.isActive) {
            if (gameState.isWaitingForReaction) {
                // Audio ended but no reaction - record as failure
                recordReaction(true);
            }
            // Play next audio after talon_strike finishes (whether reaction was recorded or not)
            if (gameState.talonStrikesPlayed < gameState.maxTalonStrikes) {
                playNextAudio();
            }
        }
    });
}

// Record reaction
function recordReaction(isTimeout = false) {
    if (!gameState.isWaitingForReaction) {
        return;
    }
    
    gameState.isWaitingForReaction = false;
    
    let reactionTime = null;
    if (!isTimeout && gameState.reactionStartTime) {
        reactionTime = performance.now() - gameState.reactionStartTime;
    }
    
    // Record the reaction
    // Any reaction < 100ms is considered false
    if (reactionTime !== null && reactionTime < 100) {
        // False reaction - too fast (likely accidental)
        gameState.reactionTimes.push({
            time: reactionTime,
            isFail: true
        });
    } else if (reactionTime !== null && reactionTime <= gameState.failureThreshold) {
        // Valid reaction
        gameState.reactionTimes.push({
            time: reactionTime,
            isFail: false
        });
    } else {
        // Timeout or invalid reaction
        gameState.reactionTimes.push({
            time: null,
            isFail: true
        });
    }
    
    gameState.talonStrikesPlayed++;
    
    // Don't stop audio - let it continue playing
    // Audio will be stopped only during mixups in playTalonStrike()
    
    updateStatsDisplay();
    
    // Check if game is complete
    if (gameState.talonStrikesPlayed >= gameState.maxTalonStrikes) {
        // Stop audio only when game ends
        if (gameState.currentAudio) {
            gameState.currentAudio.pause();
            gameState.currentAudio.currentTime = 0;
            gameState.currentAudio = null;
        }
        setTimeout(() => {
            endGame();
        }, 1000);
    } else {
        document.getElementById('current-status').textContent = 'Listening...';
        // Don't call playNextAudio immediately - let talon_strike audio finish
        // The playTalonStrike function will handle calling playNextAudio when audio ends
    }
}

// Update stats display
function updateStatsDisplay() {
    const listElement = document.getElementById('reaction-times-list');
    listElement.innerHTML = '<strong>Reaction Times:</strong><br>';
    
    gameState.reactionTimes.forEach((item, index) => {
        const div = document.createElement('div');
        div.className = 'reaction-time-item' + (item.isFail ? ' fail' : '');
        
        if (item.isFail) {
            // Check if it's a false reaction (< 100ms) or a timeout
            if (item.time !== null) {
                // False reaction - too fast
                div.textContent = `${index + 1}. ${item.time.toFixed(0)}ms (FALSE)`;
            } else {
                // Timeout or invalid reaction
                div.textContent = `${index + 1}. - (FAIL)`;
            }
        } else {
            div.textContent = `${index + 1}. ${item.time.toFixed(0)}ms`;
        }
        
        listElement.appendChild(div);
    });
    
    // Calculate and display average (excluding failures)
    const validTimes = gameState.reactionTimes.filter(item => !item.isFail);
    if (validTimes.length > 0) {
        const average = validTimes.reduce((sum, item) => sum + item.time, 0) / validTimes.length;
        document.getElementById('average-time').textContent = 
            `Average: ${average.toFixed(0)}ms (${validTimes.length} valid)`;
    } else {
        document.getElementById('average-time').textContent = 'Average: N/A';
    }
    
    // Update strikes count
    document.getElementById('strikes-count').textContent = 
        `Talon Strikes: ${gameState.talonStrikesPlayed}/${gameState.maxTalonStrikes}`;
}

// End game
function endGame() {
    gameState.isActive = false;
    gameState.isWaitingForReaction = false;
    
    // Stop any playing audio
    if (gameState.currentAudioSource) {
        try {
            gameState.currentAudioSource.stop();
        } catch (e) {
            // Source may already be stopped
        }
        gameState.currentAudioSource = null;
    }
    if (gameState.currentAudio) {
        gameState.currentAudio.pause();
        gameState.currentAudio.currentTime = 0;
        gameState.currentAudio = null;
    }
    
    if (gameState.mixupTimeout) {
        clearTimeout(gameState.mixupTimeout);
        gameState.mixupTimeout = null;
    }
    
    document.body.classList.remove('game-active');
    document.getElementById('header').textContent = 'Game Complete! Press ` to Start Again';
    document.getElementById('current-status').textContent = 'Game Finished!';
    
    // Calculate final stats
    const validTimes = gameState.reactionTimes.filter(item => !item.isFail);
    if (validTimes.length > 0) {
        const average = validTimes.reduce((sum, item) => sum + item.time, 0) / validTimes.length;
        const fails = gameState.reactionTimes.filter(item => item.isFail).length;
        document.getElementById('current-status').textContent = 
            `Game Finished! Average: ${average.toFixed(0)}ms | Failures: ${fails}`;
    }
}

// Update UI
function updateUI() {
    document.getElementById('difficulty-select').value = gameState.difficulty;
    document.getElementById('reaction-key-input').value = gameState.reactionKey.toUpperCase();
    document.getElementById(`threshold-${gameState.failureThreshold}`).checked = true;
}

// Initialize when page loads
window.addEventListener('DOMContentLoaded', init);
