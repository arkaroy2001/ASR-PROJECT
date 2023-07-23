from scipy.io import wavfile
from pesq import pesq
import os

rate,ref = wavfile.read("./p11/voli_1672948199633_1672948780895/1672948199633#A15996VY63BQ2D#G6G1GG09136704WM#1672948199128-0.wav")
rate, deg = wavfile.read("./p11/voli_1672948199633_1672948780895/1672948199633#A15996VY63BQ2D#G6G1GG09136704WM#1672948199128-0-augmented.wav")


path = "./p11/voli_1672948199633_1672948780895/"

bag = set()

for file_name in os.listdir(path):  

    pre_extension = os.path.splitext(file_name)[0]

    file_extension = os.path.splitext(file_name)[1]
    if file_extension != ".wav": continue

    last_char = pre_extension[-1]
    print(pre_extension)

    if last_char.isalpha():
        if pre_extension[:-10] in bag: 
            print("SKIP")
            continue
        file1 = path + pre_extension[:-10] + ".wav"
        file2 = path + pre_extension + ".wav"
        bag.add(pre_extension[:-10])
    elif last_char.isdigit():
        if pre_extension in bag: 
            print("SKIP")
            continue
        file1 = path + pre_extension + ".wav"
        file2 = path + pre_extension + "-augmented.wav" 
        bag.add(pre_extension)
    

    rate,ref = wavfile.read(file1)
    rate, deg = wavfile.read(file2)

    print(pesq(rate, ref, deg, 'wb'))
    print(pesq(rate, ref, deg, 'nb'))
    print('--------------------')

