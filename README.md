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
## 🎥 Project Demo

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
## 🎥 Project Demo

<p align="center">
  <a href="https://www.youtube.com/watch?v=FR_ebnw7Q-U">
    <img src="https://img.youtube.com/vi/FR_ebnw7Q-U/maxresdefault.jpg" width="700">
  </a>
</p>









