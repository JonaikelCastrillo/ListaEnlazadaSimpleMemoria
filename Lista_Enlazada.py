from Nodo import Nodo
from Person import Person
class ListaEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def get_primero(self):
        return self.primero
    
    def set_primero(self, nuevo_primero):
        self.primero = nuevo_primero
        
    def get_ultimo(self):
        return self.ultimo
    
    def set_ultimo(self, nuevo_ultimo):
        self.ultimo = nuevo_ultimo
        
        
    def insertarNodo(self, dato):
        nodoNuevo = Nodo(dato)
        if self.get_primero() == None:
            self.primero = nodoNuevo
            self.primero.set_siguiente(None)
            self.ultimo = self.primero
            print("Inserte bien 1")
        else:
            self.ultimo.set_siguiente(nodoNuevo)
            nodoNuevo.set_siguiente(None)
            self.ultimo = nodoNuevo
            print("Inserte bien 2")
            
    def mostrarLista(self):
        nodoActual = self.primero
        listaString = ""
        while nodoActual != None:
            listaString += str(nodoActual.get_dato()) + "\n"
            nodoActual = nodoActual.get_siguiente()
            
        return listaString
    
    def buscar(self, dato):
        nodoActual = self.primero
        bandera = False
        while nodoActual != None:
            if nodoActual.get_dato().get_name() == dato:
                bandera = True
            nodoActual = nodoActual.get_siguiente()
        return bandera
    
    def buscar_mayor(self):
        nodoActual = self.primero
        if nodoActual:
            max= nodoActual.get_dato()
            while nodoActual != None:
                if nodoActual.get_dato().get_age() > max.get_age():
                    max = nodoActual.get_dato()
                nodoActual = nodoActual.get_siguiente()
            print(f"La persona de mayor edad es: {max}")
        else:
            print("La lista está vacía.")
            
    def buscar_menor(self):
        nodoActual = self.primero
        if nodoActual:
            min = nodoActual.get_dato()
            while nodoActual != None:
                if nodoActual.get_dato().get_age() < min.get_age():
                    min = nodoActual.get_dato()
                nodoActual = nodoActual.get_siguiente()
            print(f"La persona de menor edad es: {min}")
        else:
            print("La lista está vacía.")
    
    def promedio(self):
        nodoActual = self.primero
        if nodoActual:
            suma = 0
            contador = 0
            while nodoActual != None:
                suma += nodoActual.get_dato().get_age()
                contador += 1
                nodoActual = nodoActual.get_siguiente()
            promedio = suma//contador
            print(f"El promedio de edad es: {promedio}")
        else:
            print("La lista está vacía.")
    
    def modificar(self, dato):
        nodoActual = self.primero
        bandera = False
        while nodoActual != None:
            if nodoActual.get_dato().get_name() == dato:
                nuevo_nombre = input("Digite el nuevo nombre: ")
                nueva_edad = int(input("Digite la nueva edad: "))
                persona = Person(nuevo_nombre, nueva_edad)
                nodoActual.set_dato(persona)
                bandera = True
            nodoActual = nodoActual.get_siguiente()
        return bandera
            
    def eliminar(self, dato):
        nodoActual = self.primero
        bandera = False
        if nodoActual is not None and nodoActual.get_dato().get_name() == dato:
            self.primero = nodoActual.get_siguiente()
            nodoActual = None
            bandera = True
            return
        
        anterior = None
        while nodoActual is not None and nodoActual.get_dato().get_name() != dato:
            anterior = nodoActual
            nodoActual = nodoActual.get_siguiente()

        if nodoActual is None:
            return

        anterior.set_siguiente(nodoActual.get_siguiente())
        nodoActual = None
        return bandera #no indica que la persona se eliminó
    