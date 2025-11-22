from cliente import Cliente
from producto import Producto
from venta import Venta
from tienda import Tienda

# Crear cliente
cliente1 = Cliente("Luis", "luis@mail.com", 1000)

# Crear productos
p1 = Producto("Teclado", 250)
p2 = Producto("Mouse", 150)

# Crear ventar y agregar productos
venta1 = Venta(cliente1)
venta1.agregar_producto(p1)
venta1.agregar_producto(p2)

# Crear tienda y registrar venta
tienda = Tienda("TechStore")
tienda.registrar_venta(venta1)

# Mostrar resultado
print(cliente1.mostrar_info())
print(f"Total de la venta: ${venta1.total():.2f}")
print(f"Ventas registradas: {len(tienda.ventas)}")
