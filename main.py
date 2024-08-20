import sounddevice as sd
import morse
import numpy as np

# Generate a 440 Hz sine wave as a numpy array
sample_rate = 44100
frequency = 700

message = "CQ CQ DE PU1OWL PU1OWL K"

audio_data=morse.encode_message(message, frequency, sample_rate, 15, jitter=True)
noise=np.random.normal(0, 0.3, audio_data.shape)

# Play the raw audio data
sd.play(audio_data + noise, sample_rate)

# Use this to keep the script running until audio playback is done
sd.wait()