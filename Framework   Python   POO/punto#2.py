class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    # Métodos para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad en cuenta: {self.cantidad:.2f}")
    
    # Método para ingresar dinero
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    # Método para retirar dinero
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

# Ejemplo de uso:

# Crear una cuenta con un titular y un saldo inicial
cuenta1 = Cuenta("Juan Pérez", 1000.0)

# Mostrar los datos de la cuenta
cuenta1.mostrar()

# Ingresar dinero en la cuenta
cuenta1.ingresar(500.0)
print("Después de ingresar 500.0:")
cuenta1.mostrar()

# Retirar dinero de la cuenta
cuenta1.retirar(200.0)
print("Después de retirar 200.0:")
cuenta1.mostrar()

# Intentar ingresar una cantidad negativa (no se hará nada)
cuenta1.ingresar(-100)
print("Intentando ingresar una cantidad negativa:")
cuenta1.mostrar()

# Intentar retirar una cantidad negativa (no se hará nada)
cuenta1.retirar(-50)
print("Intentando retirar una cantidad negativa:")
cuenta1.mostrar()
