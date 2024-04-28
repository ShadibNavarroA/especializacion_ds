class Ingredientes:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad



class PreparadorSándwich:
    def preparar_sandwich(self):
        pass



class ServidorSándwich:
    def servir_sandwich(self):
        pass



class Arma_Sandwich(PreparadorSándwich, ServidorSándwich):
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
        self.listo = False

    def preparar_sandwich(self):
        print("Preparando sándwich con los siguientes ingredientes:")
        print("- pan")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente.nombre} x{ingrediente.cantidad}")
        print("- pan")
        self.listo = True

    def servir_sandwich(self):
        if self.listo:
            print("¡Sándwich servido!")
        else:
            print("¡Sándwich no preparado!")




class HumanitoCocinero:
    @staticmethod
    def asar_sandwich(arma_sandwich):
        if arma_sandwich.listo:
            print("¡Humanito cocinero ha asado el sándwich!")
        else:
            print("¡Sándwich no preparado!")




ingredientes = [Ingredientes("Jamón", 2), Ingredientes("Queso", 1)]
sandwich = Arma_Sandwich(ingredientes)
sandwich.preparar_sandwich()
HumanitoCocinero.asar_sandwich(sandwich)


#___________________________________________________
print(" ")
#_______________________________________________________



class Arma_Sandwich:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
        self.listo = False

    def preparar_sandwich(self):
        print("Preparando sándwich con los siguientes ingredientes:")
        print("- pan")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente.nombre} x{ingrediente.cantidad}")
        print("- pan")
        self.listo = True

    def servir_sandwich(self):
        if self.listo:
            print("¡Sándwich servido!")
        else:
            print("¡Sándwich no preparado!")

    def asar_sandwich(self):
        if self.listo:
            print("¡Asando el sándwich!")
        else:
            print("¡Sándwich no preparado!")




ingredientes = [Ingredientes("Jamón", 2), Ingredientes("Queso", 1)]
sandwich = Arma_Sandwich(ingredientes)
sandwich.preparar_sandwich()
sandwich.asar_sandwich()
