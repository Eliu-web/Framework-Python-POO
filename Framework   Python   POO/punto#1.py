class Persona:
    def __init__(self, nombre="", edad=None, dni=""):
        # Constructor con valores por defecto
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)
    
    # Setter y Getter para el nombre
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.nombre = nombre
        else:
            print("El nombre debe ser una cadena no vacía.")
            self.nombre = ""
    
    def get_nombre(self):
        return self.nombre
    
    # Setter y Getter para la edad
    def set_edad(self, edad):
        if edad is None or (isinstance(edad, int) and edad >= 0):
            self.edad = edad
        else:
            print("La edad debe ser un número entero no negativo.")
            self.edad = None
    
    def get_edad(self):
        return self.edad
    
    # Setter y Getter para el DNI
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9 and dni[0:8].isdigit() and dni[8].isalpha():
            self.dni = dni
        else:
            print("El DNI debe tener 9 caracteres: 8 dígitos seguidos de una letra.")
            self.dni = ""
    
    def get_dni(self):
        return self.dni
    
    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Edad: {self.get_edad()}")
        print(f"DNI: {self.get_dni()}")
    
    # Método para verificar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad is not None:
            return self.edad >= 18
        return False

# Ejemplo de uso
persona1 = Persona("Juan Pérez", 25, "12345678Z")
persona1.mostrar()
print("¿Es mayor de edad?", persona1.es_mayor_de_edad())

persona2 = Persona("Ana", 17, "98765432Y")
persona2.mostrar()
print("¿Es mayor de edad?", persona2.es_mayor_de_edad())
