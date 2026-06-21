from playwright.sync_api import Page, expect

#Test Formulario de Contacto Email invalido

def test_enviar_formulario_test_invalido(page: Page):
    print("Given el usuario abre la página de contacto")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print("When rellena el campo nombre")
    page.get_by_role("textbox", name="Nombre *").fill("Lluvia aguilar")
    
    print("And rellena el campo email inválido")
    page.get_by_role("textbox", name="Email *").fill("test")

    print("And rellena el campo mensaje")
    page.get_by_role("textbox", name="Mensaje *").fill("Mensaje de Prueba")

    print("And envia el mesaje")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print("Then debe ver un mensaje de error")
    expect(page.get_by_text("El formato del email no es válido")).to_be_visible()  
    