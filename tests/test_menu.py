from playwright.sync_api import Page, expect

from pages.components.menu import MenuComponent
from pages.contacto_page import ContactoPage
from pages.inicio_page import InicioPage
from pages.productos_page import ProductosPage
from pages.quienes_somos_page import QuienesSomosPage


def test_visitar_enlaces(page: Page):

    menu_component = MenuComponent(page)
    inicio_page = InicioPage(page)
    quienes_somos_page = QuienesSomosPage(page)
    productos_page = ProductosPage(page)
    contacto_page = ContactoPage(page)

    print("Given la usuaria abre la página de inicio")
    inicio_page.visitar_inicio()

    print("When visita el menú “Quiénes Somos”")
    menu_component.clic_menu("Quiénes Somos")

    print("Then debe ver la url “https://web-qa.dev.adalab.es/about”")
    quienes_somos_page.verificar_url()

    print("And debe ver el titulo “Quiénes Somos”")
    quienes_somos_page.verificar_titulo("Quiénes Somos")

    print("When visita el menú “Productos”")
    menu_component.clic_menu("Productos")

    print("Then debe ver la url “https://web-qa.dev.adalab.es/products”")
    productos_page.visitar_productos()

    print("And debe ver el titulo “Catálogo de Productos”")
    productos_page.verificar_titulo("Catálogo de Productos")

    print("When visita el menú “Contacto”")
    menu_component.clic_menu("Contacto")

    print("Then debe ver la url “https://web-qa.dev.adalab.es/contact”")
    contacto_page.visitar_contacto()

    print("And debe ver el titulo “Contáctanos”")
    contacto_page.verificar_titulo("Contáctanos")

    print("When visita el menú “Inicio”")
    menu_component.clic_menu("Inicio")

    print("Then debe ver la url “https://web-qa.dev.adalab.es/”")
    inicio_page.verificar_url()

    print("And debe ver el titulo “Vida Verde”")
    inicio_page.verificar_titulo("Vida Verde")
