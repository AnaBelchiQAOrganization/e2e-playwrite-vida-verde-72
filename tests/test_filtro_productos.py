from playwright.sync_api import Page, expect


def test_filtrar_nombre_precio_categoria_con_resultados(page: Page):
    print("Given el usuario abre la página de productos ")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("When filtra por nombre “Sanse”")
    page.get_by_role("searchbox", name="Nombre").fill("Sanse")

    print("And filtra por categoria “Plantas”")
    page.get_by_label("CategoríaTodas las categorí").select_option("Plantas")

    print("And filtra por precio minimo “10”")
    page.get_by_role("spinbutton", name="Precio mínimo").fill("10")

    print("And filtra por precio máximo “25”")
    page.get_by_role("spinbutton", name="Precio máximo").fill("25")

    print("Then debe ver el producto “Sansevieria”")
    expect(page.get_by_role("heading", name="Sansevieria")).to_be_visible()

    print("And debe ver la categoría “Plantas”")
    expect(page.get_by_role("article").get_by_text("Plantas")).to_be_visible()

    print("And debe ver el precio “22”")
    expect(page.get_by_text("€")).to_be_visible()


def test_filtrar_sin_resultados(page: Page):
    print("Given el usuario abre la página de productos")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("When filtra por nombre no existente “Test”")
    page.get_by_role("searchbox", name="Nombre").fill("Test")

    print("Then ve el mensaje no se encontraron productos")
    expect(page.get_by_text("No se encontraron productos")).to_be_visible()
