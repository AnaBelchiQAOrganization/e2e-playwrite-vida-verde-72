from playwright.sync_api import Page, expect


class CarritoPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/cart"

    def proceder_al_pago(self):
        self.page.get_by_role("link", name="Proceder al Pago").click()
