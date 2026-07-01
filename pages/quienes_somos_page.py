from playwright.sync_api import Page, expect


class QuienesSomosPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/about"

    def verificar_url(self):
        expect(self.page).to_have_url("https://web-qa.dev.adalab.es/about")

    def verificar_titulo(self, titulo):
        expect(self.page.get_by_role("heading", name=titulo)).to_be_visible()
