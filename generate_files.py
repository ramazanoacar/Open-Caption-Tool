import time 

def format_time(seconds):
    millis = int((seconds - int(seconds)) * 1000)
    time_str = time.strftime('%H:%M:%S', time.gmtime(seconds))
    return f"{time_str},{millis:03d}"

def generate_srt(subtitles, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for idx, sub in enumerate(subtitles, 1):
            start = format_time(sub['start_time'])
            end = format_time(sub['end_time'])
            text = sub['text']
            f.write(f"{idx}\n{start} --> {end}\n{text}\n\n")
