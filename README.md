# Audio Transcription with Whisper

This project serves as a building block for processing Telegram voice messages to text. Other projects will use this code to then provide the text output to LLMs to make aware Telegram Agents. This python application transcribes OGG audio files to text using OpenAI's Whisper model locally.

## 🎯 Overview

This project provides a simple and efficient way to convert audio files (specifically OGG format) into text using OpenAI's Whisper automatic speech recognition (ASR) model. The application runs entirely locally, ensuring privacy and eliminating the need for API calls.

## ✨ Features

- **Local Processing**: No API keys or internet connection required for transcription
- **OGG Audio Support**: Specifically designed to handle OGG audio files
- **Multiple Model Sizes**: Support for various Whisper model sizes (tiny, base, small, medium, large)
- **Easy Configuration**: Simple file path and model selection
- **Error Handling**: Comprehensive error handling for missing files and model loading issues

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7 or higher
- FFmpeg (required for audio processing)
- Chocolatey package manager (for easy FFmpeg installation on Windows)

## 🚀 Installation

### Step 1: Install Chocolatey (Windows Package Manager)

Open PowerShell as Administrator and run the following command:

```powershell
# Install Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Verify the installation:
```powershell
choco --version
```

### Step 2: Install FFmpeg using Chocolatey

Once Chocolatey is installed, you can easily install FFmpeg:

```powershell
# Install FFmpeg
choco install ffmpeg -y
```

Verify FFmpeg installation:
```powershell
ffmpeg -version
```

### Step 3: Set Up Python Environment

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 🔧 Configuration

The application can be configured by modifying the following variables in `main.py`:

```python
# Path to your OGG audio file
AUDIO_FILE_PATH = "audio/voice_8138985924_11.ogg"

# Whisper model size (tiny, base, small, medium, large, large-v3)
MODEL_NAME = "base"
```

### Model Size Recommendations

- **tiny**: Fastest, lowest accuracy (39 MB)
- **base**: Good balance of speed and accuracy (74 MB)
- **small**: Better accuracy, slower (244 MB)
- **medium**: High accuracy, much slower (769 MB)
- **large**: Best accuracy, slowest (1550 MB)

## 🎵 Audio File Requirements

- **Format**: OGG audio files
- **Location**: Place your audio files in the `audio/` directory
- **Naming**: Update the `AUDIO_FILE_PATH` variable to match your file

## 🏃‍♂️ Usage

### Basic Usage

1. Place your OGG audio file in the `audio/` directory
2. Update the `AUDIO_FILE_PATH` in `main.py` if needed
3. Run the transcription:

```bash
python main.py
```

### Expected Output

```
Loading Whisper model: base...
Transcribing audio from: voice.file.you.provide.ogg...
Transcription Result: [Your transcribed text will appear here]
```

## 📁 Project Structure

```
audio-transcription-whisper/
├── audio/                          # Directory for audio files
│   └── voice.file.you.provide.ogg    # Sample audio file
├── venv/                          # Python virtual environment
├── main.py                        # Main application script
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. FFmpeg Not Found
**Error**: `ffmpeg: command not found`
**Solution**: Ensure FFmpeg is installed via Chocolatey and restart your terminal

#### 2. Model Loading Error
**Error**: `Error loading model`
**Solution**: 
- Ensure you have sufficient disk space for the model
- Check your internet connection for initial model download
- Verify Python dependencies are installed correctly

#### 3. Audio File Not Found
**Error**: `Error: Audio file not found`
**Solution**: 
- Check that the file exists in the specified path
- Verify the file path in `AUDIO_FILE_PATH` is correct
- Ensure the file has the correct extension (.ogg)

#### 4. Virtual Environment Issues
**Error**: `ModuleNotFoundError: No module named 'whisper'`
**Solution**: 
- Ensure virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt`

### Performance Tips

- Use smaller models (tiny, base) for faster processing
- Ensure your system has sufficient RAM for larger models
- Close other applications to free up system resources

## 🔒 Privacy & Security

- All audio processing is done locally on your machine
- No audio data is sent to external servers
- No API keys or authentication required
- Your audio files remain private and secure