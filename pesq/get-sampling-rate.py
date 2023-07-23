import os
import wave

if __name__ == "__main__":
    path = "./p11/voli_1672948199633_1672948780895/"
    for file_name in os.listdir(path):

        pre_extension = os.path.splitext(file_name)[0]
        file_extension = os.path.splitext(file_name)[1]
        if file_extension != ".wav": continue

        with wave.open(path + file_name,'rb') as f:
            framerate = f.getframerate()
            print(pre_extension + ": " + str(framerate))