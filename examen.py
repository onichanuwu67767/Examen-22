# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:
# Curso:
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

nombre = input (" pone tu nombre: ")
saldo = int(input ("cual es su saldo: "))
print ("bienvenido wei", nombre, "saldo: ", saldo)
 productos = ["agua", "alfajor", "tostada"]
 presios= ["700", "900", "2200"]



# =========================
# ETAPA 2 - COMPRAS
# =========================

print ("1. Agua       - $700")
print ("2. Alfajor    - $900")
print ("3. Tostado    - $2200")
print ("4. Consultar pedido")
print ("5. Finalizar compra")

opcion1 = int(input("elije opcion: "))
if opcion1 == 1:
    print ("producto: ", productos [0])
if opcion1 == 2:
    print ("producto: ", productos [1])
if opcion3 == 3:
    print ("producto: ", productos [-1])
    
# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
