from MiniGameEngine import GameObject
from Bullet import AlienBullet
import random

class Alien(GameObject):
    # inicializamos el Alien

    _last_shoot_time = 0.0
    _alien_fleet = []
    _CADENCE = 1/4

    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/Alien.png", "Alien")

        #Puntos de vida
        self._pts = 3

        #velocidad
        self._dx = 60.0
        self._dy = 0.0
        #posicion real
        self._rx = x
        self._ry = y
        #posicion original
        self._ox = x
        self._oy = y

        #Libertad de movimiento
        self._RANGO_DE_MOVIMIENTO = 64

        self._alien_fleet.append(self)
        

    def _zigzag(self, dt: float):
        """
        Mueve el objeto en zigzag

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
        """

        #direccion
        if abs(self._rx - self._ox) > self._RANGO_DE_MOVIMIENTO: self._dx *= -1
        
        #velocidad
        self._rx = self._rx + self._dx * dt
        self._ry = self._ry + self._dy * dt

        self.setPosition(int(self._rx), int(self._ry))
    
    @classmethod
    def fire(cls, dt):
        cls._last_shoot_time += dt
        if cls._last_shoot_time > cls._CADENCE:
            random.choice(cls._alien_fleet)._shoot()

    def _shoot(self):
        AlienBullet(self._rx, self._ry)
        Alien._last_shoot_time = 0
    
    # manejamos las colisiones
    def onCollision(self, dt: float, gobj):
        if gobj.getTipo() == "Bullet": 
            self._pts -=1
            if self._pts > 0:
                print(f"-Alien: Ouch! Me dieron! Pero aún tengo {self._pts} puntos más de vida")
            else:
                Alien._alien_fleet.remove(self)
                self.destroy()

    def onUpdate(self, dt: float):
        """
        Llamado en cada actualización del juego para el objeto.

        Args:
            dt (float): Tiempo en segundos desde la última llamada.
        """
        #Se mueve
        self._zigzag(dt)
            
