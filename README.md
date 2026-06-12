======= Cajero automatico =======

Este proyecto simula un cajero automatico el cual tiene las funciones

* Consultar saldo
* Depositar
* Retirar
* Cambiar pin
* Ver historial
* Donar a una fundacion infantil

pruebas para realizar en la exposicion

* validar el pin

Prueba 1 - PIN incorrecto una vez:
  Ingresar: 0000
  Esperado: "quedan 2 intentos"

Prueba 2 - PIN con letras:
  Ingresar: abcd
  Esperado: "PIN incorrecto"

Prueba 3 - Bloqueo por 3 intentos:
  Ingresar: 0000, 1111, 2222
  Esperado: "Tarjeta bloqueada"

Prueba 4 - PIN correcto:
  Ingresar: 1234
  Esperado: acceso al cajero

-----------------------------------------------------


* Consultar saldo

Prueba 1 - Consulta normal:
  Accion: elegir opcion 1
  Esperado: muestra saldo, retiradoHoy y limiteDiario

---------------------------------------------------

* Depositar

Prueba 1 - Deposito valido:
  Ingresar: 100000
  Esperado: saldo aumenta, movimiento registrado

Prueba 2 - Monto en cero:
  Ingresar: 0
  Esperado: "el monto debe ser mayor a 0"

Prueba 3 - Monto negativo:
  Ingresar: -5000
  Esperado: "ingrese solo numeros"

Prueba 4 - Monto con letras:
  Ingresar: abc
  Esperado: "ingrese solo numeros"

Prueba 5 - Monto con decimales:
  Ingresar: 10.5
  Esperado: "ingrese solo numeros"

-------------------------------------------------

* Retirar

Prueba 1 - Retiro valido:
  Ingresar: 50000
  Esperado: saldo disminuye, retiradoHoy aumenta

Prueba 2 - Saldo insuficiente:
  Ingresar: 999999
  Esperado: "Saldo insuficiente"

Prueba 3 - Supera limite diario:
  Retirar primero 250000, luego intentar 100000
  Esperado: "supera el limite diario"

Prueba 4 - Monto en cero:
  Ingresar: 0
  Esperado: "el monto debe ser mayor a 0"

Prueba 5 - Monto con letras:
  Ingresar: xyz
  Esperado: "ingrese solo numeros"

Prueba 6 - Exactamente el limite diario:
  Ingresar: 300000 (con saldo suficiente)
  Esperado: retiro exitoso

Prueba 7 - Retirar todo el saldo:
  Ingresar: monto exacto del saldo disponible
  Esperado: saldo queda en 0
Tocaria modicar el limite diario


----------------------------------------------------

* Cambiar pin

Prueba 1 - Cambio exitoso:
  PIN actual: 1234
  PIN nuevo: 5678
  Confirmar: 5678
  Esperado: PIN cambiado correctamente

Prueba 2 - PIN actual incorrecto:
  PIN actual: 9999
  Esperado: "pin actual no es correcto"

Prueba 3 - PIN nuevo con letras:
  PIN nuevo: ab12
  Esperado: "solo debe contener numeros"

Prueba 4 - PIN nuevo menos de 4 digitos:
  PIN nuevo: 123
  Esperado: "debe ser exactamente 4 digitos"

Prueba 5 - PIN nuevo mas de 4 digitos:
  PIN nuevo: 12345
  Esperado: "debe ser exactamente 4 digitos"

Prueba 6 - PIN nuevo igual al anterior:
  PIN nuevo: 1234
  Esperado: "no puede ser igual al actual"

Prueba 7 - Confirmacion no coincide:
  PIN nuevo: 5678
  Confirmar: 5679
  Esperado: "la confirmacion no coincide"


-----------------------------------------------------

* Ver historial

Prueba 1 - Con movimientos:
  Accion: hacer deposito y retiro primero, luego ver historial
  Esperado: lista numerada con todos los movimientos

Prueba 2 - Sin movimientos:
  Accion: ver historial con datos.json recien creado
  Esperado: "No hay movimientos registrados"


-------------------------------------------------------

* Donar

Prueba 1 - Donacion opcion 1:
  Ingresar: 1
  Esperado: descuenta 2000, donacionesTotales aumenta

Prueba 2 - Donacion opcion 2:
  Ingresar: 2
  Esperado: descuenta 5000, donacionesTotales aumenta

Prueba 3 - Donacion opcion 3:
  Ingresar: 3
  Esperado: descuenta 10000, donacionesTotales aumenta

Prueba 4 - Saldo insuficiente:
  Retirar casi todo el saldo, luego intentar donar
  Esperado: "Saldo insuficiente"

Prueba 5 - Cancelar donacion:
  Ingresar: 4
  Esperado: "Donacion cancelada"

Prueba 6 - Opcion invalida:
  Ingresar: 9
  Esperado: "Opcion incorrecta"

--------------------------------------------------------

* Validar el json 

Prueba 1 - Después de depositar:
  Abrir datos.json
  Esperado: saldo actualizado y movimiento en la lista

Prueba 2 - Después de retirar:
  Abrir datos.json
  Esperado: saldo, retiradoHoy actualizados

Prueba 3 - Después de cambiar PIN:
  Abrir datos.json
  Esperado: pin actualizado

Prueba 4 - Después de donar:
  Abrir datos.json
  Esperado: saldo y donacionesTotales actualizados



-------------------------------------------------------

* Salir

Prueba 1 - Salir normal:
  Ingresar: 7
  Esperado: mensaje de despedida y programa termina

Prueba 2 - Opcion invalida en menu:
  Ingresar: 9
  Esperado: "Opcion no valida" y vuelve al menu



