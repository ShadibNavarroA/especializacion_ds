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

    def servir(self):
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
sandwich.servir()
HumanitoCocinero.asar_sandwich(sandwich)



#___________________________________________________
print(" ")
#_______________________________________________________


class HumanitoCocinero:
    def Azar_Sandwich(self, Arma_Sandwich):
        if Arma_Sandwich.listo:
            print("Humanito que cocina a asado el sandwich")
        else:
            print("Sandwich no preparado")

    def Cocina_Sandwich(self, Arma_Sandwich):
        if not Arma_Sandwich.listo:
            print("Preparando sándwich con los siguientes ingredientes:")
            print("- pan")
            for ingrediente in Arma_Sandwich.ingredientes:
                print(f"- {ingrediente.nombre} x{ingrediente.cantidad}")
            print("- pan")
            Arma_Sandwich.listo = True



ingredientes = [Ingredientes("Jamón", 2), Ingredientes("Queso", 1)]
sandwich = Arma_Sandwich(ingredientes)
cocinero = HumanitoCocinero()
cocinero.Cocina_Sandwich(sandwich)
cocinero.Azar_Sandwich(sandwich)