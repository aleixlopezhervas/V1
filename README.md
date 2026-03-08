# Notas de la Versión 1 del Proyecto de Drones [UPC EETAC 2026] - Aleix López
 
## 4.1.1 → Modificaciones en “DashboardLocalPython.py”

El objetivo de este apartado es poder controlar nuestro dron desde un dispositivo local mediante python con los siguientes retos:

1. Modificar el código para que las operaciones de aterrizaje y RTL tengan un comportamiento similar a la operación de despegue (llamada no bloqueante)
2. Incorporar al bloque de datos de telemetría algún dato más (por ejemplo, el estado del dron o la velocidad). Conviene mirar la documentación de DronLink para ver qué información viene en el paquete de datos de telemetría.
3. Añadir algún botón más para realizar una nueva función. De nuevo, mirar la documentación de DronLink en busca de inspiración.

* Implementaciones Reto 1:
  - Añadidas las funciones “onGround” y “atHome”, siguen con el mismo comportamiento que la función incluida “inTheAir”.
  - También hay que hacer que la función “land” y “RTL” sean no bloqueantes y hagan un callback a la funciones mencionadas anteriormente.
* Implementaciones Reto 2:
  - En el bloque de telemetría añadir el label “groundSpeed” siguiendo la base de los modelos que ya estaban implementados.
 * Implementaciones Reto 3:
   - Añadida una barra deslizante para seleccionar la altura del “takeOff”.
   - Editar “inTheAir”, “onGround” y “atHome” para que cuando haga un despegue los botones de aterrizaje no tengan color y viceversa.
   - Añadida una barra deslizante para cambiar la altura de vuelo, después de revisar “dron_altitude.py”, esto se consigue gracias a la nueva función “changeAltitude”.
   - Editar “changeHeading” ya que el programa petaba si ponemos el heading a 0º.

Estas funcionalidades se pueden ver demostradas en el siguiente vídeo:
## 🎥 Demo Python Local

<p align="center">
  <a href="https://www.youtube.com/watch?v=MSE9zdbZ_DE">
    <img src="https://img.youtube.com/vi/MSE9zdbZ_DE/maxresdefault.jpg" width="700">
  </a>
</p>

## 4.1.2 → Modificaciones en “DashboardLocalCsharp”

El objetivo de este apartado es poder controlar nuestro dron desde un dispositivo local mediante cSharp con los siguientes retos:

1. Hacer que el usuario pueda establecer la altura de despegue con una barra de desplazamiento, igual que el heading o la velocidad
2. Añadir algún dato más a los datos de telemetría (consultar la documentación de csDronLink)
3. Incorporar un botón para realizar alguna nueva función (a elegir)

* Implementaciones Reto 1:
  - Añadido “takeoffTrackBar” con valores comprendidos entre 1 y 20 metros.
  - Muestra en “takeoffLabel” el valor que se está seleccionando en la barra.
  - Para confirmar el despegue aún hace falta pulsar “Despegar”.
* Implementaciones Reto 2:
  - No hay más telemetría.
 * Implementaciones Reto 3:
   - Añadida una barra para poder cambiar la altitud, sólo se aplica si tenemos la telemetría activada (porque usamos la función “IrAlPunto”).

Estas funcionalidades se pueden ver demostradas en el siguiente vídeo:
## 🎥 Demo cSharp Local

<p align="center">
  <a href="https://www.youtube.com/watch?v=FR_ebnw7Q-U">
    <img src="https://img.youtube.com/vi/FR_ebnw7Q-U/maxresdefault.jpg" width="700">
  </a>
</p>

## 4.2.2 → Modificaciones en “DashboardGlobalPython.py”

El objetivo de este apartado es poder controlar nuestro dron desde un modo global mediante python usando el archivo AutoPilot con los siguientes retos:

1. El botón de parar la recepción de datos de telemetría no está funcionando. Detectar el error y corregirlo.
2. Los cambios de velocidad y de heading no están operativos en el dashboard. Introducir el código necesario para implementar estas funcionalidades.

* Implementaciones Reto 1:
  - La función “stopTelem” fallaba porque el comando estaba mal escrito.
* Implementaciones Reto 2:
  - Modificar “changeHeading” y “changeNavSpeed” para que envíen la funcionalidad del drone al “AutopilotService”.
  - Añadir un “{STUDENT_ID}” para que nuestro drone solo sea controlado por nuestra interfaz, de este modo también puede ser controlado por otro dispositivo si accede a nuestra ID seleccionada.

Estas funcionalidades se pueden ver demostradas en el siguiente vídeo:
## 🎥 Demo Python Global

<p align="center">
  <a href="https://youtu.be/OstrefRnL78">
    <img src="https://img.youtube.com/vi/OstrefRnL78/maxresdefault.jpg" width="700">
  </a>
</p>

## 4.2.3 → WebApp

El objetivo de este apartado es poder controlar nuestro dron de un modo global mediante una WebApp usando el AutoPilot de python con los siguientes retos. 

Primero nos encontramos con unos retos para el caso de usar HTTP.

1. El botón de aterrizar tiene un comportamiento diferente al de despegar. Hacer los cambios necesarios para que el botón también se ponga en color amarillo cuando empiece el aterrizaje y se ponga en verde cuando el dron esté en tierra.
2. Añadir un nuevo botón para realizar la operación RTL.

* Implementaciones Reto 1:
  - Crear booleano “takeoffInitiated”, true si este cliente pidió un takeoff y está esperando confirmación por telemetría.
  - Crear booleano “blockAutoGreen”, si true, bloquea que el botón "Despegar" se ponga verde automáticamente (se activa cuando el usuario pulsa “Aterrizar Dron” o “RTL”; por defecto true para evitar recolor inicial).
  - Crear booleano “despegarConfirmedGreen” (boolean): true si ya confirmamos mediante telemetría el despegue y aplicamos verde. Persiste visualmente el verde hasta que el usuario haga land/rtl.
  - Crear booleano “despegarConfirmedGreen” (boolean): true si ya confirmamos mediante telemetría el despegue y aplicamos verde. Persiste visualmente el verde hasta que el usuario haga land/rtl.
* Implementaciones Reto 2:
  - Crear la función “rtlDron” siguiendo la estructura de la función “aterrizarDron”.

Estas funcionalidades se pueden ver demostradas en el siguiente vídeo:
## 🎥 Demo WebApp HTTP

<p align="center">
  <a href="https://youtu.be/NA5SStmj-9I">
    <img src="https://img.youtube.com/vi/NA5SStmj-9I/maxresdefault.jpg" width="700">
  </a>
</p>

Y por último unos retos para el caso de usar MQTT.

1. El botón de aterrizar tiene un comportamiento diferente al de despegar. Hacer los cambios necesarios para que el botón también se ponga en color amarillo cuando empiece el aterrizaje y se ponga en verde cuando el dron esté en tierra.
2. Añadir un nuevo botón para realizar la operación RTL.
3. Añadir los elementos necesarios para poder cambiar el heading del dron, igual que puede hacerse en las aplicaciones descritas en apartados anteriores.

* Implementaciones Reto 1:
  - Copiamos un poco la estructura de “despegarDron” y lo aplicamos en “aterrizarDron”, ahora sigue el mismo procedimiento de colores.
* Implementaciones Reto 2:
  - Añadimos el botón “rtlDron” siguiendo con el mismo comportamiento de colores de los otros dos botones mencionados anteriormente.
* Implementaciones Reto 3:
  - Añadimos una barra deslizante que publica el cambio por MQTT.
  - Modificamos “AutopilotService” para que calcule el giro hacia el lado más corto.
  - Igual que en HTTP, añadimos el “{STUDENT_ID}”.

Estas funcionalidades se pueden ver demostradas en el siguiente vídeo:
## 🎥 Demo WebApp MQTT

<p align="center">
  <a href="https://youtu.be/55B1zZb8Wf0">
    <img src="https://img.youtube.com/vi/55B1zZb8Wf0/maxresdefault.jpg" width="700">
  </a>
</p>

## 4.4 → Uso de “DashboardLocalConDeteccion.py”

El objetivo de este apartado es configurar nuestro dron para una posible implementación de detección de objetos. Los retos son los siguientes:

1. Procesar 1 de cada 100 frames hace que el impacto en la fluidez sea despreciable, pero introduce un retardo en la detección del objeto. Experimentar con valores más bajos de ese periodo hasta encontrar un mejor compromiso entre fluidez y retardo en la detección.
2. Añadir botones para reconocer otros objetos del data set de COCO.

* Implementaciones Reto 1:
  - Crear la variable “DETECT_EVERY” para ir probando. Haciendo pruebas con esta variable vemos que con valores por debajo de 10 el vídeo reacciona con muchísimo retraso y obviamente el procesado es igual de malo.
  - Se elige la variable con valor 10, el vídeo se ve fluido y la detección de imágenes es bastante acertada y rápida.
* Implementaciones Reto 2:
  - Añadir el botón “Gato”, “Perro” y “Pastel”.

Estas funcionalidades se pueden ver demostradas en el siguiente vídeo:
## 🎥 Demo Detección Python

<p align="center">
  <a href="https://youtu.be/9XCC3LqpSUw">
    <img src="https://img.youtube.com/vi/9XCC3LqpSUw/maxresdefault.jpg" width="700">
  </a>
</p>
