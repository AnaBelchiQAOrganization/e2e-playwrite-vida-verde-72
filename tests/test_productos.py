from playwright.sync_api import Page, expect
from pages.productos_page import ProductosPage


def test_ver_productos_y_detalles(page: Page):

    productos_page = ProductosPage(page)

    print("Given la usuaria abre la página de productos")
    productos_page.visitar_productos()

    print("Then la usuaria debe ver el título 'Catálogo de Productos'")
    productos_page.verificar_titulo("Catálogo de Productos")

    print("And la usuaria debe ver la categoría del producto 'Plantas'")
    productos_page.verificar_categoria("Plantas")

    print("And la usuaria debe ver el nombre del producto 'Ficus Lyrata'")
    productos_page.verificar_nombre_producto("Ficus Lyrata")

    print("And la usuaria debe ver el precio del producto '35.00 €'")
    productos_page.verificar_precio_producto("35.00 €")
