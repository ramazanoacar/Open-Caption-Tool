import tensorflow as tf
import numpy as np
import librosa

def load_yamnet_model():
    yamnet_model_handle = 'https://tfhub.dev/google/yamnet/1' ## Check model
    yamnet_model = tf.keras.models.load_model(yamnet_model_handle)
    return yamnet_model

def detect_sound_events(audio_path, model):
    waveform, sr = librosa.load(audio_path, sr=16000)
    scores, embeddings, spectrogram = model(waveform)
    class_names = model.class_names  # List of class names

    # Thresholding to filter out low confidence predictions
    threshold = 0.5
    events = []
    for i, score in enumerate(scores):
        if np.max(score) > threshold:
            top_class = np.argmax(score)
            events.append({
                'start_time': spectrogram.times[i],
                'end_time': spectrogram.times[i+1],
                'class': class_names[top_class],
                'confidence': float(np.max(score))
            })
    return events
