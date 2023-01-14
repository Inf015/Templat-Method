from abc import ABC, abstractmethod

class padre:

    def saludar(self):
            print("Hola")

    @abstractmethod
    def decirNombre(self):
            print("Mi Nombre es ")

        

    def saludocmpleto(self):
        self.saludar()
        self.decirNombre()

s1= padre()
s1.saludocmpleto()

class hijo(padre):

    def decirNombre(self):
        print("Mi nombre es oliver")


n2= hijo()



