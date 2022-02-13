import pyglet
from manager import SceneManager

gameManager = SceneManager()

if __name__ == "__main__":
    gameManager.start()
    pyglet.app.run()