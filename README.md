# MetronomePython

Utilizamos las librerias PyGame y PyAudio para poder desarrollar un metronomo flexible que indique los cambios de tiempo además de curvas para el cambio de velocidad dentro de la canción. 

Antes de hacer correr el script asegurese de tener instaladas las librerias 

* PyAudio
* PyGame

Para poder utilizar el metrónomo se recurre a un archivo de texto plano donde se definen, la estructura y los parámetros de cada una de las canciones con las que se quiera trabajar 

# Definición de los formato del archivo de apoyo
El metrónomo recurre a un archivo externo que debe contener cada una de las secciones de la estructura de nuestra canción, con los siguientes parámetros: 

### Cada sección de la cancion tendrá los siguientes parámetros
Metronome(bpm, time_sig,loops, name, color , ... )
* bpm= beats por minuto
* metrica = contedo de cuandos golpes hay por compas 
* compaces = Número de compases para cada sección
* nombre = Nombre de la sección para que aparezca en la pantalla
* color = color de la pantalla(un número entre 0 y 5 para que se elija uno de la paleta de colores dentro del programa)

### Adicionalmente si quieres que una sección que cambie de velocidad, puedes añadir 2 parametros al final

Metronome ( ... , change, FSpeed) 

* change = Puede tomar 2 valores, "acelerate" o "decrease", para acelerar o disminuir la velocidad respectivamente
* FSpeed = Es la velocidad final a la que se quiere llegar una vez terminada la transición 

Un archivo de canción estará compuesto por una o más secciones que cumplan con los parámetros descritos anteriormente, por ejemplo:  

80, 4, 8, Verso II, 0

80, 4, 4, Verso + , 3

80, 4, 8, Transición , 5, acelerate, 100

# Activación del metrónomo 

Para poder utilizar la aplicación debe ejecutar la siguiente orden: 

python3 visualMetro.py file.txt [-s] [-e]

donde llamamos a que python3 ejecute el script visualMetro.py con los parámetros: 
*Parámetro obligatorio*
file.txt,  que puede ser reemplazado con la ruta del archivo de texto que tenga la estructura de nuestra canción con los parámetros definidos en la sección anterior.  
*Parámetros opcionales*
[-s] , -s 3, donde el número entero hace referencia al número de sección por donde queremos que empiece el metrónomo, esto para el caso donde solo se quiera desarrollar una parte
[-e] , -e 5, donde el número entero hace referencia al número de sección en donde queremos que termine el metrónomo, para los casos donde no queremos que toque toda la canción.  


# Ejemplos : 

python3 visualMetro.py songs/Rodia.txt

python3 visualMetro.py songs/Huevear.txt -s 5 -e 7


(c) Uqi Software 2018
