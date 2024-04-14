from MiniGameEngine import GameObject


class Alien(GameObject):
    # inicializamos el Alien
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/Alien.png", "Alien")

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
        self.RANGO_DE_MOVIMIENTO = 50
        

    def zigzag(self, dt: float):
        """
        Mueve el objeto en zigzag

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
        """

        #direccion
        if abs(self._rx - self._ox) > self.RANGO_DE_MOVIMIENTO: self._dx *= -1
        
        #velocidad
        self._rx = self._rx + self._dx * dt
        self._ry = self._ry + self._dy * dt

        self.setPosition(int(self._rx), int(self._ry))
    
    # manejamos las colisiones
    def onCollision(self, dt: float, gobj):
        if gobj.getTipo() == "Bullet":
            self.destroy()
            print("Alien:me dieron")

    def onUpdate(self, dt: float):
        """
        Llamado en cada actualización del juego para el objeto.

        Args:
            dt (float): Tiempo en segundos desde la ultima llamada.
        """
        #Se mueve
        self.zigzag(dt)
    
