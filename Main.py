from Lista_Enlazada import ListaEnlazada
from Person import Person
miLista = ListaEnlazada()
numero = 0
opcion = 0

while opcion != 9:
    opcion = int(input("Digite la opción que requiera:\n"
                       "1. Ingresar \n"
                       "2. Mostrar\n"
                       "3. Buscar\n"
                       "4. Buscar persona de mayor edad\n"
                       "5. Buscar persona de menor edad\n"
                       "6. Modificar\n"
                       "7. Eliminar\n"
                       "8. Calcular promedio\n"
                       "9. Salir: \n"))
    
    match opcion:
        case 1:
            name = input("Digite el nombre: ")
            age = int(input("Digite la edad: "))
            persona = Person(name, age)
            miLista.insertarNodo(persona)
        case 2: 
            print(miLista.mostrarLista())
        case 3:
            dato = input("Digite el nombre de la persona que desea buscar: ")
            if miLista.buscar(dato):
                print("Persona encontrada")
            else:
                print("Persona no encontrada")
        case 4:
            miLista.buscar_mayor()
        case 5:
            miLista.buscar_menor()
        case 6:
            dato = input("Digite el nombre de la persona que desea modificar: ")
            if miLista.modificar(dato):
                print("Persona modificada.")
            else:
                print("Persona no encontrada. No se puede modificar")
        case 7:
            dato = input("Digite el nombre de la persona que desea eliminar: ")
            if miLista.buscar(dato):
                miLista.eliminar(dato)
                if miLista.buscar(dato) is False:
                    print("Persona eliminada.")
                else:
                    print("Error. Persona no eliminada")
            else:
                print("La persona no se encuentra en la lista.")
        case 8:
            miLista.promedio()
        case 9:
            print("Saliendo del programa...")
        case _:
            print("Opció inválida")