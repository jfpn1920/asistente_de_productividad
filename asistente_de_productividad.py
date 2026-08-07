ids = []
actividades = []
categorias = []
prioridades = []
estados = []
fechas_inicio = []
fechas_limite = []
descripciones = []
observaciones = []
#-----------------------------------------------#
#--|menu_principal_asistente_de_productividad|--#
#-----------------------------------------------#
while True:
    print("menu principal asistente de productividad")
    print("1) registrar actividad")
    print("2) editar actividad")
    print("3) eliminar actividad")
    print("4) buscar actividad")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-------------------------#
    #--|registrar_actividad|--#
    #-------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_actividad = 1
        else:
            id_actividad = ids[-1] + 1
        actividad = input("nombre de la actividad: ")
        categoria = input("categoría: ")
        prioridad = input("prioridad (alta, media o baja): ")
        estado = input("estado (pendiente, en progreso o completada): ")
        fecha_inicio = input("fecha de inicio: ")
        fecha_limite = input("fecha límite: ")
        descripcion = input("descripción: ")
        observacion = input("observación: ")
        ids.append(id_actividad)
        actividades.append(actividad)
        categorias.append(categoria)
        prioridades.append(prioridad)
        estados.append(estado)
        fechas_inicio.append(fecha_inicio)
        fechas_limite.append(fecha_limite)
        descripciones.append(descripcion)
        observaciones.append(observacion)
        print("actividad registrada correctamente.")
        print("id:", id_actividad)
    #----------------------#
    #--|editar_actividad|--#
    #----------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen actividades registradas.")
        else:
            print("editar actividad")
            for i in range(len(ids)):
                print(f"{ids[i]} | {actividades[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id de la actividad: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("actividad:", actividades[posicion])
                actividades[posicion] = input("nuevo nombre: ")
                categorias[posicion] = input("nueva categoría: ")
                prioridades[posicion] = input("nueva prioridad: ")
                estados[posicion] = input("nuevo estado: ")
                fechas_inicio[posicion] = input("nueva fecha de inicio: ")
                fechas_limite[posicion] = input("nueva fecha límite: ")
                descripciones[posicion] = input("nueva descripción: ")
                observaciones[posicion] = input("nueva observación: ")
                print("actividad actualizada correctamente.")
            else:
                print("id no encontrada.")
    #------------------------#
    #--|eliminar_actividad|--#
    #------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen actividades registradas.")
        else:
            print("eliminar actividad")
            for i in range(len(ids)):
                print(f"{ids[i]} | {actividades[i]}")
            id_buscar = int(input("ingrese la id de la actividad: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("actividad:", actividades[posicion])
                respuesta = input("¿desea eliminar esta actividad? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    actividades.pop(posicion)
                    categorias.pop(posicion)
                    prioridades.pop(posicion)
                    estados.pop(posicion)
                    fechas_inicio.pop(posicion)
                    fechas_limite.pop(posicion)
                    descripciones.pop(posicion)
                    observaciones.pop(posicion)
                    print("actividad eliminada correctamente.")
                else:
                    print("la actividad no fue eliminada.")
            else:
                print("id no encontrada.")
    #----------------------#
    #--|buscar_actividad|--#
    #----------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen actividades registradas.")
        else:
            print("buscar actividad")
            id_buscar = int(input("ingrese la id de la actividad: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("actividad:", actividades[posicion])
                print("categoría:", categorias[posicion])
                print("prioridad:", prioridades[posicion])
                print("estado:", estados[posicion])
                print("fecha de inicio:", fechas_inicio[posicion])
                print("fecha límite:", fechas_limite[posicion])
                print("descripción:", descripciones[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen actividades registradas.")
        else:
            pendientes = 0
            en_progreso = 0
            completadas = 0
            alta = 0
            media = 0
            baja = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {actividades[i]} | {categorias[i]} | {estados[i]}")
                if estados[i].lower() == "pendiente":
                    pendientes += 1
                elif estados[i].lower() == "en progreso":
                    en_progreso += 1
                elif estados[i].lower() == "completada":
                    completadas += 1
                if prioridades[i].lower() == "alta":
                    alta += 1
                elif prioridades[i].lower() == "media":
                    media += 1
                elif prioridades[i].lower() == "baja":
                    baja += 1
            print("estadísticas asistente de productividad")
            print("cantidad de actividades:", len(ids))
            print("pendientes:", pendientes)
            print("en progreso:", en_progreso)
            print("completadas:", completadas)
            print("alta prioridad:", alta)
            print("media prioridad:", media)
            print("baja prioridad:", baja)
            productividad = (completadas * 100) / len(ids)
            print("resumen de productividad")
            print("actividades registradas:", len(ids))
            print("actividades completadas:", completadas)
            print("productividad:", round(productividad, 2), "%")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el asistente de productividad.")
        break
    else:
        print("opción no válida.")