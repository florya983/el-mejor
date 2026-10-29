
Opciones={
    "Sebastian":["Ir al cine", "Hacer deporte","Viajar"],
    "Raul":["Ir al cine", "Cocinar", "Leer"],
    "Andres":["Hacer deporte", "Viajar", "Bailar"],
    "Carlos":["Leer", "Escuchar musica", "Nadar"]
}
Contadores={
    "Sebastian":0,
    "Raul":0,
    "Andres":0,
    "Carlos":0
}
maximo=0
Hobbies=["Ir al cine", "Hacer deporte", "Cocinar","Viajar","Bailar","Leer","Escuchar musica","Nadar"]
print("Bienvenidos!!!")
print ("\n Mi nombre es Cupido y elegire a la mejor opcion como posible pareja para vos")
print( "\n Para encontrar a tu crush responde a las siguientes preguntas")
for opcion in Hobbies:
    print("\n Te gusta", opcion , "? ")
    print("\n 1.si")
    print("\n 2.no")
    respuesta=input("\n Elegi una opcion ")
    if respuesta=="1":
        for nombre, listaHobbies in Opciones.items():
            if opcion in listaHobbies: 
                Contadores[nombre]+=1
for nombre,contador in Contadores.items():
    if contador>maximo:
        maximo=contador
        maximoNombre=nombre
if maximo>0:    
    print("Cupido te ha flechado!!!,tu mejor opcion es:",maximoNombre)
else: 
    print("No hay flechazo esta vez")
