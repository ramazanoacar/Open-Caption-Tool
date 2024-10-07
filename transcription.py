import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Choose model size based on performance needs
    result = model.transcribe(audio_path, verbose=True)
    return result['segments']  # List of segments with text and timestamps