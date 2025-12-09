import whisper
import os
import torch

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
        # Load the model locally. Choose compute dtype based on whether CUDA is available.
        device = "cuda" if torch.cuda.is_available() else "cpu"
        compute_type = "float16" if device == "cuda" else "float32"
        try:
            # Newer versions of whisper accept `device` and `compute_type`.
            model = whisper.load_model(model_name, device=device, compute_type=compute_type)
        except TypeError as te:
            # Older versions may not accept compute_type; fall back to specifying device only
            model = whisper.load_model(model_name, device=device)
            # Ensure model uses float32 on CPU to avoid FP16 warnings
            if device == "cpu":
                try:
                    model.to(torch.float32)
                except Exception:
                    # If this fails, ignore and proceed; at worst a warning may still appear
                    pass
    except Exception as e:
        print(f"Error loading model. Ensure you have the model downloaded and ffmpeg installed.")
        print(f"Details: {e}")
        return ""
    
    print(f"Transcribing audio from: {os.path.basename(file_path)}...")
    
    # The transcribe method handles the OGG file automatically
    # Force fp16=False on CPU to prevent the FP16 warning
    result = model.transcribe(file_path, fp16=False)
    
    transcribed_text = result["text"]    
    return transcribed_text

# --- Main Execution ---
if __name__ == "__main__":

        transcript = transcribe_ogg_to_text(AUDIO_FILE_PATH, MODEL_NAME)
        if transcript:
            print("Transcription Result:", transcript)        