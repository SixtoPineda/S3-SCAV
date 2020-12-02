import subprocess

nameVideo = ["vp8_1280x720","vp9_640x480","h265_360x240","AV1_160x120"]#nombre de los archivos

subprocess.run(f"ffmpeg -i {nameVideo[0]}.mkv -i {nameVideo[1]}.mkv -i {nameVideo[2]}.mkv -i {nameVideo[3]}.mkv -c copy -map 0 -map 1 -map 2 -map 3 4x1Container.mkv", shell=True)
