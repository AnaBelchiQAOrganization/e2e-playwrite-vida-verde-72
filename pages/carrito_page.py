from playwright.sync_api import Page, expect


class CarritoPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/cart"

    def verificar_nombre_producto(self, nombre):
        expect(self.page.get_by_role("heading", name=nombre)).to_be_visible()

    def verificar_precio_carrito(self, precio):
        expect(self.page.get_by_text(precio).first).to_be_visible()

    def verificar_resumen(self, titulo):
        expect(self.page.get_by_role(
            "heading", name=titulo)).to_be_visible()

    def verificar_desglose_pedido(self, precio):
        expect(self.page.get_by_text(precio)).to_be_visible()

    def verificar_producto_eliminado_carrito(self, producto):
        expect(self.page.get_by_role(
            "heading", name=producto)).not_to_be_visible()

    def verificar_mensaje_carrito_vacio(self, mensaje):
        expect(self.page.get_by_text(mensaje)).to_be_visible()

    def proceder_al_pago(self):
        self.page.get_by_role("link", name="Proceder al Pago").click()

    def eliminar_producto_del_carrito(self, producto):
        self.page.get_by_role("button", name=producto).click()

    def vaciar_carrito(self):
        self.page.get_by_role("button", name="Vaciar Carrito").click()

    def ver_productos(self):
        self.page.get_by_role("link", name="Ver Productos").click()
