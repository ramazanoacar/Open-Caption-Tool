from transcription import transcribe_audio
from sed import load_yamnet_model, detect_sound_events
from merge import merge_events
from generate_files import generate_srt


def process_audio(audio_path, output_path):
    # Transcribe dialogue
    transcriptions = transcribe_audio(audio_path)
    
    # Load YAMNet model
    yamnet_model = load_yamnet_model()
    
    # Detect sound events
    sound_events = detect_sound_events(audio_path, yamnet_model)
    
    # Merge events
    merged_subtitles = merge_events(transcriptions, sound_events)
    
    # Generate SRT file
    generate_srt(merged_subtitles, output_path)
    
    print(f"Subtitle file generated at {output_path}")
