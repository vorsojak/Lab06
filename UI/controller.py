import flet as ft

from model.retailer import Retailer


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def get_lista_anni(self):
        self._view._lvOut.controls.clear()

        self._view._dd_anno.options.append(
            ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")
        )
        lista_anni = self._model.get_lista_anni()
        for anno in lista_anni:
            self._view._dd_anno.options.append(
                ft.dropdown.Option(
                    key=anno,
                    text=anno
                )
            )

    def get_lista_brand(self):
        self._view._lvOut.controls.clear()

        self._view._dd_brand.options.append(
            ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")
        )
        lista_brand = self._model.get_lista_brand()
        for brand in lista_brand:
            self._view._dd_brand.options.append(
                ft.dropdown.Option(
                    key=brand,
                    text=brand
                )
            )

    def get_lista_retailer(self):
        self._view._lvOut.controls.clear()

        self._view._dd_retailer.options.append(
            ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")
        )
        lista_retailer: list[Retailer] = self._model.get_lista_brand()
        for retailer in lista_retailer:
            self._view._dd_retailer.options.append(
                ft.dropdown.Option(
                    key=str(retailer.Retailer_code),
                    text=retailer.Retailer_name
                )
            )

    def top_vendite(self, e):
        self._view._lvOut.controls.clear()

        anno = self._view._dd_anno.value
        if anno is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un anno", color="red")
            )
            self._view.update_page()
            return
        if anno ==  "Nessun filtro":
            anno = None

        brand = self._view._dd_brand.value
        if brand is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un brand", color="red")
            )
            self._view.update_page()
            return

        retailer = self._view._dd_brand.value
        if retailer is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un retailer", color="red")
            )
            self._view.update_page()
            return
        if retailer == "Nessun filtro":
            retailer = None

        output: str = self._model.top_vendite(anno, brand, retailer)

        self._view._lvOut.controls.append(
            ft.Text(output)
        )
        self._view.update_page()

    def aalizza_vendite(self, e):
        pass




























