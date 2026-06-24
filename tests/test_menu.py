from playwright.sync_api import Page, expect

def test_visitar_enlaces(page: Page):
    print("Given el usuario abre la página de inicio")
    page.goto("https://web-qa.dev.adalab.es/")

    print("When visita el menú “Quiénes Somos”")
    page.get_by_role("link", name="Quiénes Somos").click()
    
    print("Then debe ver la url “https://web-qa.dev.adalab.es/about”")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/about")

    print("And debe ver el titulo “Quiénes Somos”")
    expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()

    print("When visita el menú “Productos”")
    page.get_by_role("link", name="Productos").click()

    print("Then debe ver la url “https://web-qa.dev.adalab.es/products”")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/products")

    print("And debe ver el titulo “Catálogo de Productos”")
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()

    print("When visita el menú “Contacto”")
    page.get_by_role("link", name="Contacto").click()

    print("Then debe ver la url “https://web-qa.dev.adalab.es/contact”")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/contact")

    print("And debe ver el titulo “Contáctanos”")
    expect(page.get_by_role("heading", name="Contáctanos")).to_be_visible()

    print("When visita el menú “Inicio”")
    page.get_by_role("link", name="Inicio", exact=True).click()

    print("Then debe ver la url “https://web-qa.dev.adalab.es/”")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/")

    print("And debe ver el titulo “Vida Verde”")
    expect(page.get_by_role("heading", name="Vida Verde")).to_be_visible()
