# ***SCAV: P3-Streaming and final exercises***

## **EJERCICIOS**

**IMPORTANTE: cuando ejecutamos los fichero python, dado que se pide al ususario cierta interacción, una vez puesto en ejecución el script, debemos presionar F5 para poder ver la pantalla emergente (cmd) donde poder introducir la información y trabajar con el script.**

### EJERCICIO-1
#### ***Python: BBB video converted***

<p align="justify">En este ejercicio se nos pedía crear 4 videos con las siguientes características: </p>

* Video 1: Codec: vp8 y resolución: 1280x720
* Video 2: Codec: vp9 y resolución: 640x480
* Video 3: Codec: h.265 y resolución: 360x240
* Video 4: Codec: AV1 y resolución: 160x120

<p align="center">(Para realizar cada uno de estos pasos, reutilicé código de prácticas anteriores)</p>
<p align="justify">Reutilicé el código siguiente: </p>
<p align="center">ffmpeg -i <strong>{inputVideo}</strong> -vf scale=<strong>{width:high}</strong> -c:v <strong>{CodecType}</strong> <strong>{nameVideo}</strong>.mkv</p>
<p align="justify">Donde le pedimos al usuario que nos introduzca el nombre del video con el que trabajar y realizo un bucle en python donde vamos creando cada uno de los videos mencionados anteriormente. Con este fin creé una lista con cada una de las resoluciones y sus respectivos códecs. <br><br>Cabe destacar que todos los videos obtenidos son guardados como .mkv dado que, el codec vp8 no es compatible con .mp4, y para poder realizar el siguiente ejercicio, poder tener todos los videos con la misma extensión favorecía a la hora de crear el container. </p>

##### **Resultados**

<p align="center">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/vp8.png" width="400">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/VP9.png" width="400">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/H265.png" width="400">
  <img src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-1/FOTOS/AV1.png" width="400">
</p>


<p align="justify">Como podemos ver, cada video corresponde con su respectiva resolución como se ha mencionado anteriormente al inicio del ejercicio.</p>
<p align="justify"><em>Resultado de cada video del ejercicio en EJERCICIO-1/FOTOS</em></p>

### EJERCICIO-2
#### ***Container of the 4 videos***

<p align="justify">Con el fin de crear un container con los cuatro videos, reutilicé el código de la práctica 3 donde creábamos un container con varios audios. Por ello el comando es: </p>

<p align="center">ffmpeg -i {nameVideo[0]}.mkv -i {nameVideo[1]}.mkv -i {nameVideo[2]}.mkv -i {nameVideo[3]}.mkv -c copy -map 0 -map 1 -map 2 -map 3 4x1Container.mkv</p>

<p align="justify">Fuente:<br>https://video.stackexchange.com/questions/12867/combine-multiple-videos-as-separate-streams-in-one-mkv-file</p>

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-2/result.png" />
</p>

<p align="justify">Como podemos ver, el container final tiene los 4 videos, y con sus respectivos audios y codecs. </p>
<p align="justify">En analizar los videos por separado he podido apreciar que el video con codec vp9 y una resolución de 640x480 obtiene unos mejores resultados visuales respecto el video con un peor codec como vp8 y una mayor resolución como 1280x720. Este factor puede ser dado por cómo de bien comprimen cada uno de los codecs. Tal y como vimos en teoría, el codec vp9 es la versión mejorada del vp8, por lo tanto, podemos entender que comprime mejor, lo cual se traduce en la capacidad de comprimir la información del video lo máximo que le es posible sin deteriorar la calidad de éste. Por esta razón el codec vp9 comprime muy bien evitando el decaimiento de la calidad, lo cual no consigue el codec vp8, que pese a trabajar con un video de mayor resolución, al no comprimir tan bien, provoca que la calidad del video sea menor. </p>

### EJERCICIO-4
#### ***Python: The online streaming***

<p align="justify">En este ejercicio se nos pedía crear un script que nos permita activar un streaming online mediante el cual transmitir el video que nosotros escojamos. Por ello, nuevamente cree un bucle donde se pedía al usuario el video con el que stremear. <br>Posteriormente procedíamos a realizar el comando: </p>
<p align="center">ffmpeg -i {archivo} -v 0 -f mpegts udp://@224.2.2.2:2222</p>
<p align="justify">con el que activamos el streaming con ese archivo en concreto. Para poder acceder al streaming tan solo debemos ir a nuestro programa de VLC, acceder a <strong>Medio</strong> y posteriormente abrir <strong>Abrir Ubicación de Red...</strong>. En la ventana emergente colocar la dirección que establecemos para stremear: udp://@224.2.2.2:2222 (dirección expresamente para poder realizar streamings).</p>
<p align="justify">Fuente: <br>https://stackoverflow.com/questions/43826675/how-to-live-stream-a-local-video-using-ffmpeg</p>

##### **Resultados**

<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/S3-SCAV/blob/main/EJERCICIO-4/result.png" />
</p>




