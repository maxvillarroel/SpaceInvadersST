# VSCODE
# File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"

from MiniGameEngine import GameWorld
from SpaceShip import SpaceShip
from Alien import Alien


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Actividad 01", bgpic="Recursos/Fondo.png")
        
        # agregamos a los actores 
        SpaceShip(400, 540)

        for i in range(100, 800, 100):
            for j in (50, 150, 250):
                Alien(i, j) 


    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
         #print(fps)  
        if self.isPressed("Escape"):
            self.exitGame()                                

        #Dispara
        Alien.fire(dt)

# -- show time
game = Game()
game.gameLoop(60)