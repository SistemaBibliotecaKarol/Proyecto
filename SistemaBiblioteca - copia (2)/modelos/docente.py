from modelos.personas import Persona

# ==========================================
# CLASE: Docente
# Hereda de Persona
# ==========================================

class Docente(Persona):

    def __init__(self, id_persona, nombres, apellidos, facultad):

        super().__init__(id_persona, nombres, apellidos)

        self.__facultad = facultad

    # Getter
    def get_facultad(self):
        return self.__facultad

    # Setter
    def set_facultad(self, facultad):
        self.__facultad = facultad

    # Polimorfismo
    def mostrar_datos(self):
        super().mostrar_datos()
        print("Facultad:", self.__facultad)
