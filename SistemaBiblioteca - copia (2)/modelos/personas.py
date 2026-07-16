# ==========================================
# CLASE: Persona
# ==========================================

class Persona:

    # Constructor
    def __init__(self, id_persona, nombres, apellidos):

        # Atributos privados (Encapsulamiento)
        self.__id_persona = id_persona
        self.__nombres = nombres
        self.__apellidos = apellidos

    # Getters
    def get_id_persona(self):
        return self.__id_persona

    def get_nombres(self):
        return self.__nombres

    def get_apellidos(self):
        return self.__apellidos

    # Setters
    def set_nombres(self, nombres):
        self.__nombres = nombres

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    # Método
    def mostrar_datos(self):
        print("ID:", self.__id_persona)
        print("Nombres:", self.__nombres)
        print("Apellidos:", self.__apellidos)
