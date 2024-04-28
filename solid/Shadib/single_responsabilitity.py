print(" ")
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
            print(f"-  {ingrediente.nombre} x{ingrediente.cantidad}")
        print("- pan")
        self.listo = True


class HumanitoCocinero:
    def Azar_Sandwich(Arma_Sandwich):
        if Arma_Sandwich.listo:
            print("Humanito que cocina a asado el sandwich")
        else:
            print("Sandwich no preparado")



ingredientes = [Ingredientes("Jamón", 2), Ingredientes("Queso", 1)]
sandwich = Arma_Sandwich(ingredientes)
sandwich.preparar_sandwich()
HumanitoCocinero.Azar_Sandwich(sandwich)


#___________________________________________________
print(" ")
#_______________________________________________________




class Sandwich:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
        self.listo = False

    def preparar_sandwich(self):
        print("Preparando sándwich con los siguientes ingredientes:")
        print("- pan")
        for ingrediente in self.ingredientes:
            print(f"-  {ingrediente}")
        print("- pan")
        self.listo = True

    def Azar_Sandwich(self):
        if self.listo:
            print("Humanito que cocina a asado el sandwich")
        else:
            print("Sandwich no preparado")





Ingredientes = ["Jamón", "Queso"]
sandwich0 = Sandwich(Ingredientes)
sandwich0.preparar_sandwich()
sandwich0.Azar_Sandwich()
