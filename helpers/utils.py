def filterBooks(libros, edad, presupuesto, motivo, tiempo):
    libros_filtrados = []
    for libro in libros:
        if libro["Edad"] == edad and libro["Presupuesto"] == presupuesto and libro["Motivo"] == motivo and libro["Tiempo"] == tiempo:
            libros_filtrados.append(libro)
    return libros_filtrados