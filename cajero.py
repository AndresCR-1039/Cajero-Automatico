# Importamos para poder usar el .json
import json

# Defino la funcion cargarDatos vacio pues siempre abre el mismo archivo
def cargarDatos():
    archivo = open("datos.json", "r") # Abrimos el json en modo read osea modo lectura
    datos = json.load(archivo) # Lee el archivo y lo combierte para que python lo pueda interpretar en este caso a un diccionario
    archivo.close() # Cerramos el archivo para que no genere problemas
    return datos # retorna los datos del diccionario para poder ser utilizado

# Defino la funcion guardarDatos y recibe datos que es el diccionario actualizado 
def guardarDatos(datos):
    archivo = open("datos.json", "w") # abre el archivo y con el w lo abre de forma de escritura
    json.dump(datos, archivo, indent=4, ensure_ascii=False) # con esto volvemos a convertir de diccionario a texto json 
    # con el indent=4 ponemos el texto con sangria 4 para poder ser leido por humano si no todo quedaria en una sola linea
    # con el ensure_ascii=False hacemos que pueda guardar tildes y ñ para que no quede raro el texto
    archivo.close() # con esto cerramos el archivo 

# Defino la funcion verificarPin para validar los pin correcto incorrectos y bloquear la tarjeta cuando se llegue a 3 intentos fallidos
def verificarPin():
    datos = cargarDatos() # Cargo los datos de json para poder validar con el pin que se engresa
    intentos = 0 # incialiso en 0 para poder sumar intentos y poder validar cuando llegue a 3 intentos fallidos

    while intentos < 3: # creamos el bucle con la condicion que intentos sea menos a 3 
        pin = input("Ingrese su PIN: ") # le pedimos al usuario el pin

        if pin == datos["pin"]: # creamos el if para validar si el pin ingresado es igual a el pin en el json
            print("PIN correcto.") # le damos un mensaje que el pin es correcto
            return True # retornamos True para que de acceso al cajero
        else: # declaramos el else para cuando el pin sea diferente al guardado en el json
            intentos += 1 # le sumamos a intentos 1 para ir aumentando en 1 
            restantes = 3 - intentos # le damos a restantes el resultado de 3 - los intentos fallidos para determinar cuando este en 0 
            if restantes > 0: # declaramos el if para entrar mientras que restantes sea mayor a 0
                print(f"PIN incorrecto. quedan {restantes} intento.") # le muestra al usuario que el pin fue incorrecto y le dice cuantos intentos le quedan
    print("Tarjeta bloqueada. Demaciados intentos fallidos.") # cuando sale del while sin returnar true quiere decir que no logro con los 3 intentos
    # al tener 3 intentos fallidos la tarjeta se bloquea y por esto se le manda este mensaje
    return False # se returna False para decir que no puede usar el cajero

# defino la funcion mostrarMenu para mostrar el menu al usuario y pedir la opcion
def mostrarMenu():
    print("\n=========================")
    print("      BANCO INTER NAL      ")
    print("=========================")
    print("    1. Consultar saldo")
    print("    2. Depositar")
    print("    3. Retirar")
    print("    4. Cambiar PIN")
    print("    5. Ver historial")
    print("    6. Donar a fundacion infantil")
    print("    7. Salir")
    print("=========================")
    opcion = input("Seleccione una opcion: ") # le pedimos al usuario que ingrese una opcion 
    return opcion # retornamos la opcion escojida

# defino la funcion consultarSaldo que recibe el diccionario datos despues le imprimimos los datos de este diccionario a el usuario
def consultarSaldo(datos):
    print("\n=========================")
    print("    SALDO DISPONIBLE")
    print("=========================")
    print(f"  Saldo disponible: {datos['saldo']:,}") #con :, le damos un formato especial que separa en miles al numero  
    print(f"  Retiro de hoy: {datos['retiradoHoy']:,}")
    print(f"  Limite diario: {datos['limiteDiario']:,}")
    print("========================")

# defino la funcion depositar la cual recibe el diccionario
def depositar(datos):
    print("\n=========================")
    print("        DEPOSITO         ")
    print("=========================")
    monto = input("Ingrese el monto a depositar: ") # aqui lo mandamos como texto para poder validar mas adelante con el .isdigit

    if monto.isdigit() == False: # con este if validamos si el ingreso son digitos de ser texto o floar retorna False por lo que entra al mensaje para el usuario
        print("Error el monto solo puede ser numeros.") # mensaje de error
        return datos  # guardamos en el json sin modificar
    monto = int(monto) # cambiamos monto a int para ya poder seguir con el monto

    if monto <= 0: # con este if validamos que el ingreso no sea 0 o negativo
        print("Error el monto debe ser mayor a 0.") 
        return datos # Guardamos en el json sin modificar
    datos["saldo"] = datos["saldo"] + monto  # con este actualizamos el saldo con el monto
    datos["movimientos"].append(f"[+] Deposito: {monto:,} | Saldo: {datos['saldo']:,}") # con este sumamos un movimientos para despues poder mostrarlos
    guardarDatos(datos) #retornamos los cambios al json
    print(f" Deposito exitos. tu nuevo saldo es: {datos['saldo']:,}") # le damos el mensaje exitoso al cliente
    return datos

# declaro la funcion retirar
def retirar(datos):
    print("\n=========================")
    print("       RETIRAR           ")
    print("=======================")
    print(f"   Saldo disponible: {datos['saldo']:,}") # le imprimo al usuario el saldo
    print(f"   Limite diario restante: {datos['limiteDiario']- datos['retiradoHoy']:,}") # le imprimo al usuario cuanto mas puede retirar hoy

    monto = input("\nIngrese el monto a retirar: ") # le mandamos monto como texto para poder validar despues con isdigit

    if monto.isdigit() == False: # validamos si es solo digitos si no se cumple le damos un mensaje y retornamos sin modificar
        print("Ingrese solo numeros.")
        return datos
    
    monto = int(monto) # convertimos monto a entero

    if monto <= 0: # validamos que el monto a retirar sea mayor a 0
        print("Error el monto debe ser mayor a 0.")
        return datos # si no le retornamos sin modificar
    
    if monto > datos["saldo"]: # validamos que el saldo que va a retirar si sea suficiente
        print("Saldo insuficiente")
        return datos # si no retornamos sin modificar
    
    if datos["retiradoHoy"] + monto > datos ["limiteDiario"]: # validamos que lo que se retirara no exceda el limite diario
        restante = datos["limiteDiario"] - datos["retiradoHoy"]
        print(f"error: supera el limite diario. queda disponible hoy {restante:,} ")
        return datos # si lo excede retornamos sin modificar
    
    datos["saldo"] = datos["saldo"] - monto # actualizamos el saldo menos el monto retirado
    datos["retiradoHoy"] = datos["retiradoHoy"] + monto # le sumamos al limite de retiro lo que se acava de retirar
    datos["movimientos"].append(f"[-] Retiro: {monto:,} | Saldo: {datos['saldo']:,}") # sumamos a movimientos los datos para despues poder inprimir el historial
    guardarDatos(datos) # se guarda los datos en el json
    print(f"\n Retiro exitoso su nuevo saldo es: {datos['saldo']:,}") # le mostramos mediante mensaje el exito y el nuevo saldo
    return datos #retornamos los datos modificados

#defino la funcion cambiarPin
def cambiarPin(datos):
    print("\n=========================")
    print("       CAMBIAR PIN       ")
    print("=======================")

    pinActual = input("Ingrese su PIN actual: ") # le pido el pin actual para validar que si sea el usuario

    if pinActual != datos['pin']: # con este if valido si es correcto el pin
        print("Error el pin actual no es correcto.")
        return datos # retornamos sin cambios
    
    pinNuevo = input("Ingrese el nuevo PIN: ") # le pedimos el nuevo pin en texto para poder validar con el isdigit

    if pinNuevo.isdigit() == False: # validamos que solo sea digitos
        print("Error el PIN solo debe contener numeros")
        return datos #retornamos sin cambios
    
    if len(pinNuevo) != 4 : # si el pin es diferente de 4 osea menos o mas digitos le retornamos error, con el len validamos el tamaño del pinNuevo
        print("Error el PIN debe ser exactamente 4 digitos")
        return datos # retornamos sin cambios
    
    if pinNuevo == pinActual:
        print("Error el pin nuevo no puede ser igual al actual.")
        return datos
    
    pinConfirmar = input("Confirme su nuevo PIN: ") # pedimos confirmacion del pin

    if pinNuevo != pinConfirmar :  # si son diferentes el pinNuevo y el pinConfirmar le damos error
        print("Error: la confirmacion no coincide.")
        return datos # retornamos sin cambios
    
    datos["pin"] = pinNuevo # modificamos el pin 
    datos["movimientos"].append("[!] Cambio de PIN exitoso.") # le sumamos a movimientos para despues poder consultarlo
    guardarDatos(datos) # guardamos los datos en json
    print("PIN cambiado correctamente.") # mensaje de cambio correcto
    return datos # retornamos 

# Defino la funcion verHistorial
def verHistorial(datos):
    print("\n=========================")
    print("      MOVIMIENTOS      ")
    print("=======================")

    if len(datos["movimientos"]) == 0:  # con este if validamos que en movimientos si tengamos movimientos
        print("No hay movimientos registrados.") 
        return # si no retornamos, como esta variable solo muestra no modifica no tenemos que retornar nada mas
    
    contador = 1 # declaramos una variable contador en 1
    for movimiento in datos["movimientos"]: # con este for recorremos todos los datos guardados en movimientos en el json
        print(f"   {contador}. {movimiento}") # le imprimimos los movimientos 1 por 1 al usuario
        contador += 1 # aumentamos el contador

    print("=======================")


# Defino la funcion donar
def donar(datos):
    print("\n=========================")
    print("   DONAR A FUNDACION   ")
    print("       SONRISAS        ")
    print("=======================")
    print("  Selecciones el monto a donar: ") # le muestro el mensaje de opciones a donar
    print("  1. 2,000")
    print("  2. 5,000")
    print("  3. 10,000")
    print("  4. Cancelar")
    print("=======================")

    opcion = input("Seleccione la opcion: ") # le pido que seleccione una opcion

    if opcion == "1": # mediante if y elif se dan a validar las opciones y se le lleva a monto la cantidad donada
        monto = 2000
    elif opcion == "2":
        monto = 5000
    elif opcion == "3":
        monto = 10000
    elif opcion == "4":
        print("Donacion cancelada.") # se cancela la donacion se retorna datos sin modificar
        return datos
    else:
        print("Opcion incorrecta.") # si elije una opcion diferente se da error y se retorna sin modificar
        return datos
    
    if monto > datos['saldo']:
        print("Saldo insuficiente para realizar la donacion.") # si el saldo es insuficiente se manda error y se retoran sin modificar
        return datos
    
    datos["saldo"] = datos["saldo"] - monto # se modifica el saldo
    datos["donacionesTotales"] = datos["donacionesTotales"] + monto # se modifica las dornaciones totales
    datos["movimientos"].append(f"[!] Donacion: {monto:,} | Saldo: {datos['saldo']:,}") # se actualiza un movimiento para despues poder listar
    guardarDatos(datos) # se guardan los datos en el json
    print(f"Gracias por tu donacion de {monto:,}") 
    print(f"Has donado un total de {datos['donacionesTotales']:,}")
    print("Los niños te lo agradeseran") # mensajes de agradecimiento
    return datos # se retorna datos




