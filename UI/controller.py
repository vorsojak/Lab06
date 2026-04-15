import flet as ft

from model.retailer import Retailer


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def get_lista_anni(self):
        self._view._lvOut.controls.clear()
        res = []
        res.append(
            ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")
        )
        lista_anni = self._model.get_lista_anni()
        for anno in lista_anni:
            res.append(
                ft.dropdown.Option(
                    key=anno,
                    text=anno
                )
            )
        return res

    def get_lista_brand(self):
        self._view._lvOut.controls.clear()
        res = []
        res.append(
            ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")
        )
        lista_brand = self._model.get_lista_brand()
        for brand in lista_brand:
            res.append(
                ft.dropdown.Option(
                    key=brand,
                    text=brand
                )
            )
        return res

    def get_lista_retailer(self):
        self._view._lvOut.controls.clear()
        res = []
        res.append(
            ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")
        )
        lista_retailer: list[Retailer] = self._model.get_lista_retailer()
        for retailer in lista_retailer:
            res.append(
                ft.dropdown.Option(
                    key=str(retailer.Retailer_code),
                    text=retailer.Retailer_name
                )
            )
        return res

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

        retailer = self._view._dd_retailer.value
        if retailer is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un retailer", color="red")
            )
            self._view.update_page()
            return
        if retailer == "Nessun filtro":
            retailer = None

        output: str = self._model.top_vendite(anno, brand, retailer)
        if output == "":
            self._view._lvOut.controls.append(
                ft.Text("Nessuna vendita trovata per le opzioni selezionate")
            )
            self._view.update_page()
            return
        self._view._lvOut.controls.append(
            ft.Text(output)
        )
        self._view.update_page()


    def analizza_vendite(self, e):
        self._view._lvOut.controls.clear()

        anno = self._view._dd_anno.value
        if anno is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un anno", color="red")
            )
            self._view.update_page()
            return
        if anno == "Nessun filtro":
            anno = None

        brand = self._view._dd_brand.value
        if brand is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un brand", color="red")
            )
            self._view.update_page()
            return

        retailer = self._view._dd_retailer.value
        if retailer is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Seleziona un retailer", color="red")
            )
            self._view.update_page()
            return
        if retailer == "Nessun filtro":
            retailer = None

        output: [] = self._model.analizza_vendite(anno, brand, retailer)

        self._view._lvOut.controls.append(
            ft.Text("Statistiche vendite: ")
        )

        self._view._lvOut.controls.append(
            ft.Text(f"Giro d'affari: {output[0]["giro_affari"]}\n"
                    f"Numero vendite: {output[1]["n_vendite"]}\n"
                    f"Numero retailers coinvolti: {output[2]["n_retailers"]}\n"
                    f"Numero prodotti coinvolti: {output[3]["n_prodotti"]}")
        )
        self._view.update_page()




























