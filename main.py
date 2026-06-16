from cajero import cargarDatos, verificarPin, mostrarMenu, consultarSaldo, depositar, retirar, cambiarPin, verHistorial, donar

def main():

    
    if not verificarPin():
        print("Acceso denegado PIN incorrecto 3 veces")
        return
    
    datos = cargarDatos()
    
    opcion = ""
    while opcion != "7" :
        opcion = mostrarMenu()

        if opcion == "1":
            consultarSaldo(datos)

        elif opcion == "2":
            datos = depositar(datos)

        elif opcion == "3":
            datos = retirar(datos)

        elif opcion == "4":
            datos = cambiarPin(datos)

        elif opcion == "5":
            verHistorial(datos)

        elif opcion == "6":
            datos = donar(datos)

        elif opcion == "7":
            print("Gracias por usar BANCO INTER NAL. Vuelva pronto.")
        
        else:
            print("Opcion no valida. vuelva a intentar")

main()