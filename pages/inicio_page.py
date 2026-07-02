from playwright.sync_api import Page, expect


class InicioPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/"

    def visitar_inicio(self):
        self.page.goto(self.url)

    def verificar_url(self):
        expect(self.page).to_have_url(self.url)

    def verificar_titulo(self, titulo):
        expect(self.page.get_by_role("heading", name=titulo)).to_be_visible()

    def verificar_titulo_pagina(self, titulo_pagina):
        expect(self.page).to_have_title(titulo_pagina)

    def verificar_boton_productos(self, boton_productos):
        expect(self.page.get_by_role(
            "link", name=boton_productos)).to_be_visible()
