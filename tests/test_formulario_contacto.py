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

    #Test Formulario de Contacto Email invalido

def test_enviar_formulario_email_invalido(page: Page):
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

    #Test Formulario de Contacto Email vacío
def test_enviar_formulario_email_vacio(page: Page):
    print("Given el usuario abre la página de contacto")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print("When rellena el campo nombre")
    page.get_by_role("textbox", name="Nombre *").fill("Lluvia aguilar")
    
    print("And deja el campo email vacío")
    page.get_by_role("textbox", name="Email *").fill("")

    print("And rellena el campo mensaje")
    page.get_by_role("textbox", name="Mensaje *").fill("Mensaje de Prueba")

    print("And envia el mesaje")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print("Then debe ver un mensaje de error")
    expect(page.get_by_text("El email es obligatorio")).to_be_visible()
