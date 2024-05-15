class Personaje:
    def __init__(self, nombre):
        # Constructor
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        # Getter de estado
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def asignar_estado(self, experiencia):
        # Setter de estado
        self.experiencia += experiencia
        while self.experiencia >= 100:
            self.experiencia -= 100
            self.nivel += 1
        while self.experiencia < 0 and self.nivel > 1:
            self.experiencia += 100
            self.nivel -= 1
        if self.experiencia < 0:
            self.experiencia = 0

    def __gt__(self, otro):
        # Sobrecarga para comparar “mayor que”
        return self.nivel > otro.nivel

    def __lt__(self, otro):
        # Sobrecarga para comparar “menor que”
        return self.nivel < otro.nivel

    def __eq__(self, otro):
        # Sobrecarga para comparar “igual que”
        return self.nivel == otro.nivel

    def probabilidad_ganar(self, otro):
        # Método de instancia que retorna la probabilidad de la instancia actual de ganar respecto de otra instancia
        if self > otro:
            return 0.66
        elif self < otro:
            return 0.33
        else:
            return 0.50

    @staticmethod
    def dialogo_enfrentamiento(probabilidad):
        # Método que muestra diálogo de enfrentamiento al orco y retorna opción escogida por el jugador
        print(f"Con tu nivel actual, tienes {probabilidad * 100}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Huir")
        return int(input())
