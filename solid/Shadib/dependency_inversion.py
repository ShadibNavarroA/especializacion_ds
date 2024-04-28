from abc import ABC, abstractmethod



class Ingredientes:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad



class PreparadorSándwich(ABC):
    @abstractmethod
    def preparar_sandwich(self):
        pass



class Arma_Sandwich(PreparadorSándwich):
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



class Cocinero(ABC):
    @abstractmethod
    def cocinar(self, preparador_sandwich):
        pass




class HumanitoCocinero(Cocinero):
    def cocinar(self, preparador_sandwich):
        preparador_sandwich.preparar_sandwich()
        print("¡Sándwich preparado!")




ingredientes = [Ingredientes("Jamón", 2), Ingredientes("Queso", 1)]
sandwich = Arma_Sandwich(ingredientes)
cocinero = HumanitoCocinero()
cocinero.cocinar(sandwich)


#___________________________________________________
print(" ")
#_______________________________________________________




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