# 3.1 Generar ejecutable

Instalar pyinstaller:
```
pip3 install pyinstaller
```

Generar ejecutable en un único fichero:
```
pyinstaller --onefile gui.py
```

Elejecutable se generará en carpeta "dist".

Recuerda añadir archivos que no sean de código junto al ejecutable generado (este ejemplo se hace con una fuente en fichero .ttf para probar este detalle).