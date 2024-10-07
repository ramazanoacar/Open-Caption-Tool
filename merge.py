def merge_events(transcriptions, sound_events):
    merged = []
    for t in transcriptions:
        merged.append({
            'start_time': t['start'],
            'end_time': t['end'],
            'text': t['text'],
            'type': 'dialogue'
        })
    for se in sound_events:
        merged.append({
            'start_time': se['start_time'],
            'end_time': se['end_time'],
            'text': f"[{se['class']}]",
            'type': 'sound'
        })
    # Sort by start_time
    merged_sorted = sorted(merged, key=lambda x: x['start_time'])
    return merged_sorted
