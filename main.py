import whisper
import os

# I installed FFMPEG on my system for audio processing via Chocolatey.
# --- Configuration ---
# 1. Specify the path to your OGG audio file
AUDIO_FILE_PATH = "audio/voice_testing.ogg"

# 2. Choose the Whisper model size (tiny, base, small, medium, large, large-v3)
# 'base' is a good starting point for accuracy and speed.
MODEL_NAME = "base"

# --- Transcription Function ---
def transcribe_ogg_to_text(file_path: str, model_name: str) -> str:
    """
    Transcribes an OGG audio file to text using the local Whisper model.
    """
    if not os.path.exists(file_path):
        return f"Error: Audio file not found at {file_path}"
    
    print(f"Loading Whisper model: {model_name}...")
    try:
        # Load the model locally
        model = whisper.load_model(model_name)
    except Exception as e:
        print(f"Error loading model. Ensure you have the model downloaded and ffmpeg installed.")
        print(f"Details: {e}")
        return ""
    
    print(f"Transcribing audio from: {os.path.basename(file_path)}...")
    
    # The transcribe method handles the OGG file automatically
    result = model.transcribe(file_path)
    
    transcribed_text = result["text"]    
    return transcribed_text

# --- Main Execution ---
if __name__ == "__main__":

        transcript = transcribe_ogg_to_text(AUDIO_FILE_PATH, MODEL_NAME)
        if transcript:
            print("Transcription Result:", transcript)        