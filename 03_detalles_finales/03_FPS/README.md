# 3.3 FPS

En esta sección se muestra cómo forzar la misma velocidad de movimiento en el juego, 
de forma independiente a los FPS del juego configurando el game loop con la función:     pyglet.clock.schedule_interval(update, 1.0/x), donde x serían los FPS.

