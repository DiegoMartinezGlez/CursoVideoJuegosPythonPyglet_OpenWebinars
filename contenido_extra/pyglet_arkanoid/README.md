# PYGLET ARKANOID

Versión de Arkanoid a medio desarrollar, para analizar y practicar tras el curso de OpenWebinars de Desarrollo de Videjuegos con Python+Pyglet.

Se ha implementado únicamente el movimiento de la plataforma del jugador y la bola, con su movimiento y colisiones de la bola con la plataforma y los bordes de la zona de juego.

## Requisitos:
- Python 3
- Pyglet package

Instalar dependencias:
```
pip3 install pyglet
```

## Como ejecutar el juego:

Ejecutar:
```
python3 main.py
```

## Ejercicios propuestos:

Para completar una primera versión del juego:
- Implementa una clase "bloque" para representar los clásicos bloques del Arkanoid, añade control de colisiones y el eliminado del bloque cuando la bola entra en contacto.
- Diseña uno o varios niveles con distinta configuración de bloques
- Implementa (con o sin gestión de escenas) estados del juego: inicio, juego, game over.

Amplía la versión inicial con tus propias ideas o alguno de los siguientes ejemplos:
- Diseña más niveles con evolución de la dificultad
- Diseña e implementa tipos de bloques
- Diseña un sistema de puntuaciones
- Modifica el rebote de la bola sobre la plataforma para darle efecto en base al movimiento y velocidad tanto de la bola como de la plataforma
- Diseña e implementa un sistema de generación aleatoria de bloques para generar niveles aleatorios


## References:
- Se recomienda visitar la wiki del Arkanoid de fandom.com, donde encontrarás mucha información sobre diferentes aspectos de múltiples versiones del Arkanoid: https://gameszone.fandom.com/es/wiki/Arkanoid


