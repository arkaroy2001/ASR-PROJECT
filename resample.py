import os
import librosa 
import soundfile as sf


if __name__ == "__main__":

    path = "./p11/voli_1672948199633_1672948780895/"

    for file_name in os.listdir(path):
        print(file_name)

        pre_extension = os.path.splitext(file_name)[0]
        file_extension = os.path.splitext(file_name)[1]

        if file_extension != ".wav": continue

        y, sr = librosa.load(path + file_name, sr=16000)
        sf.write(path + file_name, y, sr)