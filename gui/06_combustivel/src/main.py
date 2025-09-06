import flet as ft

def main(page: ft.Page):

    # função do evento
    def calcular_combustivel(e):
        if not gasolina.value:
            gasolina.error_text = "Peso não pode ficar vazio"
            page.update()
        else:
            gasolina.error_text = ""
            page.update()

        if not etanol.value:
            etanol.error_text = "Altura não pode ficar vazio"
            page.update()
        else:
            etanol.error_text = ""

            # recebe os valores dos inputs
            gasolina.value = float(gasolina.value.replace(",", "."))
            etanol.value = float(etanol.value.replace(",", "."))

            # calcula a vantagem
            vantagem = (etanol.value/gasolina.value)*100

            # exibe o valor da vantagem
            dlg_modal.title.value = f"Vantagem é de {vantagem:.2f}"

            # diagnóstico
            if vantagem < 70:
                dlg_modal.content.value = f"Valor do porcentual {vantagem:.2f}%, compensa o etanol"
            else:
                dlg_modal.content.value = f"Valor do porcentual {int(vantagem)}%, compensa a gasolina"


            # abre o modal
            page.open(dlg_modal)

            # limpa e prepara os campos
            gasolina.value = ""
            etanol.value = ""
                
            page.update()

    # propriedades da janela
    page.title = "Melhor Combustível para Abastecer"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # variáveis
    gasolina = ft.TextField(prefix_text="R$ ", label="Gasolina")
    etanol = ft.TextField(prefix_text="R$ ", label="Etanol", on_submit=calcular_combustivel)

    # caixa de diálogo
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    # barra superior
    page.appbar = ft.AppBar(title=ft.Text("Melhor Combustível para Abastecer", size=16))

    # conteúdo da janela
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Melhor Combustível para Abastecer", size=30, weight="bold"),
                alignment=ft.alignment.center
            ),
            expand=True
        ),
        ft.ResponsiveRow(
            [
                ft.Container(gasolina, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(etanol, col={"sm": 6, "md": 4, "xl": 2})
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    ft.ElevatedButton("Calcular Melhor Combustível para Abastecer", on_click=calcular_combustivel),
                    padding=30
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)
