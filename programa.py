from medicamento import Medicamento

nombre = input("Ingrese nombre del medicamento:\n")
stock = int(input("Ingrese stock del medicamento:\n"))
precio_bruto = int(input("Ingrese precio bruto del medicamento:\n"))

m1 = Medicamento(nombre, stock)
m1.precio = precio_bruto

if m1.descuento:
    print(f"Tiene un descuento de {int(m1.descuento * 100)}%")
    
print(f"El precio final del medicamento es ${int(m1.precio_final)}")
