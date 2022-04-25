# PYGLET TETRIS

Versión simplificada del Tetris clásico para analizar y practicar tras el curso de OpenWebinars de Desarrollo de Videjuegos con Python+Pyglet.

## Requisitos:
- Python 3
- Pyglet package
- Numpy

Instalar dependencias:
```
pip3 install pyglet
pip3 install numpy
```

## Como ejecutar el juego:

Ejecutar:
```
python3 main.py
```

## Detalles de implementación:

Para implementar el juego se ha diseñado una clase Grid que gestiona la matriz por donde se moverán los bloques, así como los paneles de información (siguiente bloque, conteo de bloques y líneas e instrucciones de juego). En esta clase está casi toda la lógica del juego, mientras que en main.py se realiza la gestión general de la ventana y estados del juego, control de eventos de teclado y métodos de "update" con distinto propósito y frecuencia.

Los ficheros y clases adicionales son para representar los bloques (blocks.py), los "ladrillos" o "cuadritos" de los bloques (brick.py) y los paneles anexos a la matriz del juego (next.py, score.py, help.py).

Estados del juego: inicio, juego y "game over". Para comenzar el juego al inicio o después de un "game over" se espera que se pulse la tecla "espacio".

Para salir del juego en cualquier momento se debe pulsar la tecla ESC.

Se ha usado nomenclatura para los tipos de bloques según las implementaciones clásicas: O, I, S, Z, L, J. Consultar la Wiki del apartado de "Referencias" para más información sobre los tipos de bloques.

Se ha implementación la rotación clásica de Nintendo. Consultar la Wiki del apartado de "Referencias" para más información sobre los tipos de rotación en otras versiones.

La generación de bloques aleatoria se realiza de la siguiente manera: se mete cada tipo de bloque en un array

## Ejercicios propuestos:
- Implementa un método de puntuaciones más allá de contar los bloques y líneas.
- Implementa una evolución de la dificultad, por ejemplo, aumentando la frecuencia del método que mueve el bloque hacia abajo automáticamente, lo cual aumentaría su velocidad después de limpiar cierto número de líneas.
- Implementa otra generación aleatoria de bloques.
- Pinta una "sombra" del bloque que está cayendo, al fondo de la línea vertical desde su posición, para mostrar donde encajaría el bloque mientras va cayendo.
- Implementa la rotación en ambos sentidos, usando dos teclas del teclado (por defecto los bloques sólo rotan en un sentido, pulsando "espacio").
- Añade animación para cuando se completan líneas
- Añade sonidos para algunos eventos (cuando un bloque encaja o se "congela", al completar una línea, game over)
- Idea tus propias modificaciones sobre el juego!

Consulta la Wiki del apartado "Referencias" al final de este README, donde encontrarás algunas ideas en base a las distintas implementaciones y características de las diversas versiones de Tetris.

## References:
- Se recomienda visitar la wiki del Tetris de fandom.com, donde encontrarás mucha información sobre diferentes aspectos de múltiples versiones del Tetris: https://tetris.fandom.com/wiki/Tetris_Wiki


