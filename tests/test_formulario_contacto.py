from playwright.sync_api import Page, expect
from pages.contacto_page import ContactoPage


#Enviar formulario con campos obligatorios validos 

def test_formulario_contactos_obligatorios_validos(page: Page):

    contacto_page = ContactoPage(page)
    
    print("Given el usuario abre la página de contacto")
    contacto_page.visitar_contacto()

    print("When rellena el campo nombre con nombre válido")
    contacto_page.rellenar_nombre("Reyes Cuesta")

    print("And rellena el campo email con email válido")
    contacto_page.rellenar_email("test@gmail.com")

    print ("And rellena campo de mensaje")
    contacto_page.rellenar_mensaje("Mensaje de prueba")

    print("And envía el formulario")
    contacto_page.enviar_mensaje()

    print("The debe ver un mensaje de exito")
    contacto_page.verificar_mensaje_exito()

#Enviar formulario email invalido    
def test_enviar_formulario_email_invalido(page: Page):

    contacto_page = ContactoPage(page)

    print("Given el usuario abre la página de contacto")
    contacto_page.visitar_contacto()

    print("When rellena el campo nombre")
    contacto_page.rellenar_nombre("Lluvia aguilar")
    
    print("And rellena el campo email inválido")
    contacto_page.rellenar_email("test")

    print("And rellena el campo mensaje")
    contacto_page.rellenar_mensaje("Mensaje de prueba")

    print("And envia el mesaje")
    contacto_page.enviar_mensaje()

    print("Then debe ver un mensaje de error")
    contacto_page.verificar_mensaje_error_email

#Test Formulario de Contacto Email vacío
def test_enviar_formulario_email_vacio(page: Page):

    contacto_page = ContactoPage(page)
    
    print("Given el usuario abre la página de contacto")
    contacto_page.visitar_contacto()

    print("When rellena el campo nombre")
    contacto_page.rellenar_nombre("Lluvia aguilar")
    
    print("And deja el campo email vacío")
   
    print("And rellena el campo mensaje")
    contacto_page.rellenar_mensaje("Mensaje de prueba")

    print("And envia el mesaje")
    contacto_page.enviar_mensaje()

    print("Then debe ver un mensaje de error")
    contacto_page.verificar_mensaje_error_email_obligatorio()
