import subprocess

print("\n\n\t\t\t\tEMPEZEMOS\n\n")

print("\t\t- Realizar ejercicio (1)")
print("\n\t\t- Exit (0)")
i = input("\nSeleccione una opción (0 o 1): ")


while(int(i) == 1):#saldremos del bucle si el usuario decide hacer Exit poniendo un 0

    archivo = input("\n\nIntroduzca el nombre COMPLETO del video con el que Stremear: ")#pedimos el nombre del video con el que trabajar
    print("\n\tDir. streaming: udp://@224.2.2.2:2222\n")
    print("\n\tPulsar control+C para finalizar streaming.\n")
    subprocess.run(f"ffmpeg -i {archivo} -v 0 -f mpegts udp://@224.2.2.2:2222", shell=True)

    #volvemos a empezar hasta que el usuario quiera marcharse, Exit
    print("\n\n\t\t- Streamear (1)")
    print("\n\t\t- Exit (0)")
    i = input("\nSeleccione una opción (0 o 1): ")
