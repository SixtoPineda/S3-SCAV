import subprocess

print("\t\t\t\tEMPEZEMOS\n\n")

print("\t\t- Realizar ejercicio (1)")
print("\n\t\t- Exit (0)")
i = input("\nSeleccione una opción (0 o 1): ")


while(int(i) == 1):#saldremos del bucle si el usuario decide hacer Exit poniendo un 0

    archivo = input("\n\nIntroduzca el nombre COMPLETO del video con el que trabajar: ")#pedmimos el nombre del video con el que trabajar
    scaleValue = ["1280:720","640:480","360:240","160:120"]#resoluciones
    codec = ["vp8","vp9","hevc","av1"]#codecs
    nameVideo = ["vp8_1280x720","vp9_640x480","h265_360x240","AV1_160x120"]#nombre de los archivos
    for i in range(len(codec)):

        subprocess.run(f"ffmpeg -i {archivo} -vf scale={scaleValue[i]} -c:v {codec[i]} {nameVideo[i]}.mkv", shell=True)


    #volvemos a empezar hasta que el usuario quiera marcharse, Exit
    print("\n\n\t\t- Realizar ejercicio (1)")
    print("\n\t\t- Exit (0)")
    i = input("\nSeleccione una opción (0 o 1): ")
