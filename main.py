
print("===BIENVENIDOS A 'EL MEJOR'===")

print("¿A quién querés conocer?")
print("1. Hombres")
print("2. Mujeres")

opcion = input("Elegí una opción: ")

if opcion == "1":
    print("\nElegiste conocer hombres")
    print("1. Sebastian")
    print("2. Raul")
    print("3. Pedro")

    persona = input("Elegí una persona: ")

    if persona == "1":
        print("\nElegiste a Sebastian")
        compatibilidad = 0

        print("\n¿Te gusta salir los fines de semana?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta viajar?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta escuchar música?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\nCompatibilidad con Sebastian:",
              compatibilidad, "/ 3 ❤️")

    elif persona == "2":
        print("\nElegiste a Raul")
        compatibilidad = 0

        print("\n¿Te gusta cocinar?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta mirar películas?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta hacer deporte?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\nCompatibilidad con Raul:",
              compatibilidad, "/ 3 ❤️")

    elif persona == "3":
        print("\nElegiste a Pedro")
        compatibilidad = 0

        print("\n¿Te gusta leer?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gustan los videojuegos?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta viajar?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\nCompatibilidad con Pedro:",
              compatibilidad, "/ 3 ❤️")

    else:
        print("Opción inválida")


elif opcion == "2":
    print("\nElegiste conocer mujeres")
    print("1. Valentina")
    print("2. Maria")
    print("3. Samanta")

    persona = input("Elegí una persona: ")

    if persona == "1":
        print("\nElegiste a Valentina")
        compatibilidad = 0

        print("\n¿Te gusta salir?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta bailar?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta viajar?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\nCompatibilidad con Valentina:",
              compatibilidad, "/ 3 ❤️")

    elif persona == "2":
        print("\nElegiste a Maria")
        compatibilidad = 0

        print("\n¿Te gusta leer?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta mirar series?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta cocinar?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\nCompatibilidad con Maria:",
              compatibilidad, "/ 3 ❤️")

    elif persona == "3":
        print("\nElegiste a Samanta")
        compatibilidad = 0

        print("\n¿Te gusta escuchar música?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta cocinar?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\n¿Te gusta ir al cine?")
        print("1. Si")
        print("2. No")
        respuesta = input("Elegí una opción: ")

        if respuesta == "1":
            compatibilidad += 1

        print("\nCompatibilidad con Samanta:",
              compatibilidad, "/ 3 ❤️")

    else:
        print("Opción inválida")


else:
    print("Opción inválida")
