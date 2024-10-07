# Potential Future Feature
sound_description_map = {
    "dog": "A dog is barking",
    "door": "The sound of a door opening",
    "laughter": "Someone is laughing",
    # Add more mappings here
}

def enhance_sound_descriptions(sound_events):
    for event in sound_events:
        event['text'] = sound_description_map.get(event['class'], f"[{event['class']}]")
    return sound_events
