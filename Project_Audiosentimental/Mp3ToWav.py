import os
import subprocess
filename=input("Enter a filename from testdata (must include .mp3/.mp4): ")
command = "ffmpeg -i testdata/"+filename+" -ab 160k -ac 2 -ar 44100 -vn wavefiles/"+filename+".wav"
# Loop through the filesystem
subprocess.call(command, shell=True)
                
# Skip the file in case of error