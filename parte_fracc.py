"""
Regresa si un número dado tiene o no decimales.
"""
# Entradas
numero = float(input("Introduzca un número: "))

# Proceso
numero_entero = int(numero)
if numero_entero == numero:
    resultado = "No"
else:
    resultado = "Sí"

# Salidas
print(resultado, "tiene decimales")
