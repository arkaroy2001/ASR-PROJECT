from scipy.io import wavfile
from pesq import pesq
import numpy as np
import soundfile as sf
import librosa 
import wave 
import os

def add_white_noise(signal, noise_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_factor
    return augmented_signal


if __name__ == "__main__":
    #file_name = "./p11/voli_1672948199633_1672948780895/1672948199633#A15996VY63BQ2D#G6G1GG09136704WM#1672948199128-0-augmented.wav"
    path = "./p11/voli_1672948199633_1672948780895/"
    for file_name in os.listdir(path):
        print(file_name)
        pre_extension = os.path.splitext(file_name)[0]
        file_extension = os.path.splitext(file_name)[1]

        if file_extension != ".wav": continue

        signal, sr = librosa.load(path + file_name)
        augmented_signal = add_white_noise(signal, 0.3)
        #resample = librosa.resample(augmented_signal,)
        sf.write(path + pre_extension + "-augmented.wav", augmented_signal, sr)
        # with wave.open(path + file_name,'rb') as f:
        #     framerate = f.getframerate()
        #     print(framerate)

    


