class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def retirar(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta.")
        else:
            print("No hay suficiente saldo para realizar la retirada.")

    def mostrar(self):
        return f"Titular: {self.titular}, Saldo: {self.cantidad}"

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # Setter y getter para la bonificación
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    # Método para verificar si el titular es válido
    def esTitularValido(self):
        if 18 <= self.titular['edad'] < 25:
            return True
        return False

    # Método para retirar dinero solo si el titular es válido
    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("No puedes retirar dinero porque no eres un titular válido.")

    # Método para mostrar los detalles de la cuenta
    def mostrar(self):
        return f"Cuenta Joven con bonificación del {self.bonificacion}%. Titular: {self.titular['nombre']}, Saldo: {self.cantidad}"

# Ejemplo de uso
titular1 = {'nombre': 'Juan', 'edad': 22}
cuenta1 = CuentaJoven(titular1, 1000, 5)  # 5% de bonificación

print(cuenta1.mostrar())  # Muestra la información de la cuenta
cuenta1.retirar(200)  # Intenta retirar dinero
cuenta1.retirar(1000)  # Intenta retirar más de lo disponible

titular2 = {'nombre': 'Ana', 'edad': 30}
cuenta2 = CuentaJoven(titular2, 1500, 7)  # 7% de bonificación

print(cuenta2.mostrar())  # Muestra la información de la cuenta
cuenta2.retirar(100)  # No podrá retirar porque no es titular válido
