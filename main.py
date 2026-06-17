from cajero import cargarDatos, iniciarSesion, guardarDatos, mostrarMenu, consultarSaldo, depositar, retirar, cambiarPin, verHistorial, donar

def main():

    
    usuario = iniciarSesion()

    if usuario is None:
        print("Acceso denegado.")
        return
    
    datosCompletos = cargarDatos()
    datos = datosCompletos[usuario]
    
    opcion = ""
    while opcion != "7" :
        opcion = mostrarMenu()

        if opcion == "1":
            consultarSaldo(datos)
            datosCompletos[usuario] = datos
            guardarDatos(datosCompletos)

        elif opcion == "2":
            datos = depositar(datos)
            datosCompletos[usuario] = datos
            guardarDatos(datosCompletos)

        elif opcion == "3":
            datos = retirar(datos)
            datosCompletos[usuario] = datos
            guardarDatos(datosCompletos)

        elif opcion == "4":
            datos = cambiarPin(datos)
            datosCompletos[usuario] = datos
            guardarDatos(datosCompletos)

        elif opcion == "5":
            verHistorial(datos)

        elif opcion == "6":
            datos = donar(datos)
            datosCompletos[usuario] = datos
            guardarDatos(datosCompletos)

        elif opcion == "7":
            print("Gracias por usar BANCO INTER NAL. Vuelva pronto.")
        
        else:
            print("Opcion no valida. vuelva a intentar")

main()