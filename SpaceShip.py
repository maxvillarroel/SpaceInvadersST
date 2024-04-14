import time
from MiniGameEngine import GameObject, GameWorld
from Bullet import Bullet


class SpaceShip(GameObject):
    # inicializamos la Nave Espacial
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/SpaceShip.png", "SpaceShip")
        self.lastBullet = time.time()
        #Puntos de vida
        self._pts = 5

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.isPressed("Left"):
            x = x - 4
            if x - w / 2 < 0:
                x = w / 2
        elif self.isPressed("Right"):
            x = x + 4
            if x > ww - w / 2:
                x = ww - w / 2
        self.setPosition(x, y)

        # disparamos una bala
        if self.isPressed("space"):
            if time.time() - self.lastBullet > 0.3:
                Bullet(x, y - 30)
                self.lastBullet = time.time()
    
    # manejamos las colisiones
    def onCollision(self, dt: float, gobj):
        if gobj.getTipo() == "AlienBullet": 
            self._pts -=1
            if self._pts > 0:
                print(f"-Space Ship: Ouch! Me dieron! Pero aun tengo {self._pts} puntosa de vida")
            else:
                self.destroy()
                GameWorld._getInstance().exitGame()