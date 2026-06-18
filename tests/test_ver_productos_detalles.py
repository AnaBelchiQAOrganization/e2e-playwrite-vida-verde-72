from playwright.sync_api import Page, expect


def test_ver_productos_y_detalles(page: Page):
    print("Given la usuaria abre la página de productos")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("Then la usuaria debe ver el título 'Catálogo de Productos'")
    # Comprobamos que la página contiene el título "Catálogo de Productos"
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()

    print("And la usuaria debe ver la categoría del producto 'Plantas'")
    # Comprobamos que la usuaria ve la categoría del producto "Plantas"
    expect(page.get_by_text("Plantas").nth(2)).to_be_visible()

    print("And la usuaria debe ver el nombre del producto 'Ficus Lyrata'")
    # Comprobamos que la usuaria ve el nombre del producto "Fycus Lyrata"
    expect(page.get_by_role("heading", name="Ficus Lyrata")).to_be_visible()

    print("And la usuaria debe ver el precio del producto '35.00 €'")
    # Comprobamos que la usuaria ve el precio del producto "35.00 €"
    expect(page.get_by_text("35.00 €")).to_be_visible()
