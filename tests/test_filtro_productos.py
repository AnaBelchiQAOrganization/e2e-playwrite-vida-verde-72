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

    print("And debe ver el precio “22”")
    expect(page.get_by_text("€")).to_be_visible()
