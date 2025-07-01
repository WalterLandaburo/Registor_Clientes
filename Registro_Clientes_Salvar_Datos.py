"""

registro_clientes.py 

Autor: Landaburo, Walter Nahuel (desarrollador autodidacta).
Fecha de creación: 2025 - 07 - 01.

Descripción:
-----------
Este script implementa una simulación básica de un registro de clientes.
Permite agregar datos: nombre, apellido y correo electrónico a una lista principal y crear o sobrescribir un archivo de texto para guardar la información.
El programa está diseñado para interactuar con el usuario/a.

Estructura general:
------------------
• archivo de texto para guardar información.
• docstring para documentar las acciones al recorrer el script.

Notas:
------
• este programa es parte mi práctica de Python.
• posteriormente incluiré un cambio respecto a como se muestra el contenido guardado en el archivo de texto.

Licencia:
--------
Este código es de uso educativo y puede ser modificado con fines personales o de aprendizaje.

Compatibilidad:
---------------
Python 3.0
"""




#lista principal 
list_clients = []


#Datos: nombre, apellido y correo electrónico 
print("=== Registro de clientes,===")
print("Ingrese los datos del cliente")

 

while True:
    
    name = str(input("\nIngrese el nombre del cliente: ")).strip().title()
        
    #Salir del bucle 
    if name == "":
        print("Finalizar registro. Saliendo ....")
        break
            
    lastname = str(input("\nIngrese el apellido del cliente: ")).strip().capitalize()

    email = str(input("\nIngrese el correo electrónico del cliente: ")).strip()
    
    
    #Sub-lista para cada cliente    
    client = [name, lastname, email]
    
    #Añadir sub-lista a la lista principal 
    list_clients.append(client)
    
    
    """
Archivo de texto:
     guarda la información en un archivo de texto
     usa 'w': significa que crea un archivo o sobrescribe uno existente con el nombre indicado 
     cada vez que inicia el programa sobrescribe el archivo, lo que significa que desaparece la información guardada anteriormente, siendo reemplazada por la nueva
     ubique la acción después de la acción de añadir a la lista para que sea inmediato y no dependa de la decisión del usuario cuando guardar. Así se disminuye el riesgo de la perdida de la información por una falla de energía que pueda cerrar la sesión abruptamente, no dando oportunidad al usuario/a de elegir guardar el registro
     se guarda como una lista en cada línea, cada línea representa a un cliente, su apariencia es '[name, lastname, email]'
     
"""
    archivo = open("datos.txt", "w")
    
    
    
    for client in list_clients:
        archivo.write(f"{client}\n")
        
    archivo.close()


    #Confirma la acción de registro del cliente 
    print("\n\n✅ Cliente registrado")
    print(f"Nombre: {client[0]} Apellido: {client[1]} Correo electrónico: {client[2]}")


    #Ordenar lista principal 
    list_clients.sort()
    
    #Mostrar el contenido de la lista principal 
    print("\n\nLista de clientes")
    for i, client in enumerate(list_clients, start=1):
        print(f"{i}. Nombre: {client[0]} Apellido: {client[1]} Correo electrónico: {client[2]}")
    
         
        
        
  
 