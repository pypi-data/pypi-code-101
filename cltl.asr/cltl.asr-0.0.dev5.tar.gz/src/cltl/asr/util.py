import numpy as np
import sounddevice as sd
import soundfile


def store_wav(frames, sampling_rate, save=None):
    if not isinstance(frames, np.ndarray):
        audio = np.concatenate(frames)
    else:
        audio = frames

    if save:
        soundfile.write(save, audio, sampling_rate)
    else:
        sd.play(audio, sampling_rate)
        sd.wait()
