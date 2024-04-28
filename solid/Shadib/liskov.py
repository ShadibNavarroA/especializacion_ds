class Ingredientes:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad




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



class HumanitoCocinero:
    @staticmethod
    def asar_sandwich(arma_sandwich):
        if arma_sandwich.listo:
            print("¡Humanito cocinero ha asado el sándwich!")
        else:
            print("¡Sándwich no preparado!")




class Arma_SandwichEspecial(Arma_Sandwich):
    def __init__(self, ingredientes):
        super().__init__(ingredientes)


    def preparar_sandwich(self):
        print("Preparando un sándwich especial con los siguientes ingredientes:")
        print("- pan integral")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente.nombre} x{ingrediente.cantidad}")
        print("- pan integral")
        self.listo = True




ingredientes = [Ingredientes("Jamón", 2), Ingredientes("Queso", 1)]
sandwich_normal = Arma_Sandwich(ingredientes)
sandwich_especial = Arma_SandwichEspecial(ingredientes)

sandwich_normal.preparar_sandwich()
HumanitoCocinero.asar_sandwich(sandwich_normal)

print("\n")

sandwich_especial.preparar_sandwich()
HumanitoCocinero.asar_sandwich(sandwich_especial)


#___________________________________________________
print(" ")
#_______________________________________________________


class HumanitoCocinero:
    def Azar_Sandwich(self, Arma_Sandwich):
        if Arma_Sandwich.listo:
            print("Humanito que cocina a asado el sandwich")
        else:
            print("Sandwich no preparado")



ingredientes = [Ingredientes("Jamón", 2), Ingredientes("Queso", 1)]
sandwich = Arma_Sandwich(ingredientes)
sandwich.preparar_sandwich()
cocinero = HumanitoCocinero()
cocinero.Azar_Sandwich(sandwich)