# 2.7 Física con Pymunk

2 scripts de ejemplo de integración de Pymunk para controlar la física de los objetos del juego.

En el primero de ellos se crea un "space" de pymunk donde se define cierta gravedad, y al arrancar el juego dicho objeto cae por la gravedad. Ejemplo sencillo para ver los conceptos básicos de pymunk: space, space.step(dt) y bodies.

En el segundo se pintan más cuerpos (bodies) para formar un sistema sismétrico, y se añaden los conceptos de elasticidad y fricción. Se pueden modificar valores para cada objeto, de forma que al disponerse inicialmente de forma simétrica,se observen diferencias de comportamientos al tener distintas propiedades.