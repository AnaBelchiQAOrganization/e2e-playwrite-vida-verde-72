from playwright.sync_api import Page, expect

#Enviar formulario con campos obligatorios validos 
def test_formulario_contactos_obligatorios_validos(page: Page):
    
    print("Given el usuario abre la página de contacto")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print("When rellena el campo nombre con nombre válido")
    page.get_by_label("Nombre").fill("Reyes Cuesta")

    print("And rellena el campo email con email válido")
    page.get_by_label("Email").fill("test@gmail.com")

    print ("And rellena campo de mensaje")
    page.get_by_label("Mensaje").fill("Mensaje de prueba")

    print("And envía el formulario")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print("The debe ver un mensaje de exito")
    expect(page.get_by_text("¡Mensaje enviado con éxito!")).to_be_visible()
    expect(page.get_by_text("Gracias por contactarnos. Te responderemos lo antes posible")).to_be_visible()