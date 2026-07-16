from modelos.personas import Persona

# ==========================================
# CLASE: Estudiante
# Hereda de Persona
# ==========================================

class Estudiante(Persona):

    def __init__(self, id_persona, nombres, apellidos, carrera):

        super().__init__(id_persona, nombres, apellidos)

        self.__carrera = carrera

    # Getter
    def get_carrera(self):
        return self.__carrera

    # Setter
    def set_carrera(self, carrera):
        self.__carrera = carrera

    # Polimorfismo
    def mostrar_datos(self):
        super().mostrar_datos()
        print("Carrera:", self.__carrera)
