from playwright.sync_api import Page

from pages.carrito_page import CarritoPage
from pages.components.menu import MenuComponent
from pages.productos_page import ProductosPage


def test_carrito(page: Page):

    productos_page = ProductosPage(page)
    menu_component = MenuComponent(page)
    carrito_page = CarritoPage(page)

    print("Given el usuario abre la página de productos")
    productos_page.visitar_productos()

    print("When filtra por producto 'Regadera'")
    productos_page.filtrar_por_nombre("regadera")

    print("And agrega el producto al carrito")
    productos_page.agregar_producto("Añadir Regadera Metálica")

    print("And filtra por producto 'Tijeras'")
    productos_page.filtrar_por_nombre("tijeras")

    print("And agrega el producto al carrito")
    productos_page.agregar_producto("Añadir Tijeras de Podar")

    print("When visita el carrito")
    menu_component.clic_carrito_de_la_compra()

    print("Then debe ver el producto Regadera y su precio")
    carrito_page.verificar_nombre_producto("Regadera Metálica")
    carrito_page.verificar_precio_carrito("24.00 €")

    print("And debe ver el producto Tijeras y su precio")
    carrito_page.verificar_nombre_producto("Tijeras de Podar")
    carrito_page.verificar_precio_carrito("18.50 €")

    print("And debe ver el resumen del pedido")
    carrito_page.verificar_resumen("Resumen del Pedido")
    carrito_page.verificar_desglose_pedido("42.50 €")
    carrito_page.verificar_desglose_pedido("8.92 €")
    carrito_page.verificar_desglose_pedido("5.00 €")
    carrito_page.verificar_desglose_pedido("56.42 €")

    print("When elimina el producto Regadera")
    carrito_page.eliminar_producto_del_carrito("Eliminar Regadera Metálica")

    print("Then no debe ver el producto Regadera")
    carrito_page.verificar_producto_eliminado_carrito("Regadera")

    print("And resumen del pedido actualizado")
    carrito_page.verificar_precio_carrito("18.50 €")
    carrito_page.verificar_precio_carrito("3.88 €")
    carrito_page.verificar_precio_carrito("27.38 €")

    print("When vacía el carrito")
    carrito_page.vaciar_carrito()

    print("Then debe ver mensaje carrito vacío")
    carrito_page.verificar_mensaje_carrito_vacio("Tu carrito está vacío")

    print("And hace clic en Ver Productos")
    carrito_page.ver_productos()

    print("Then debe ver la página de productos")
    productos_page.verificar_url()
    productos_page.verificar_titulo("Catálogo de Productos")
