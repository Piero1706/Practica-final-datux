from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from config.app import App
from controller.function import IngestDataProducts
from controller.report import GenerateReportVentas
from controller.report_pandas import GenerateReportProfitPivotPandas

def menu(app: App):
    console = Console()
    while True:
        menu_text = Text()
        menu_text.append("\n📊 [bold cyan]Proyecto Datux[/bold cyan]\n", style="underline bold")
        menu_text.append("\n[1] 🟢 Ingestar Data\n", style="green")
        menu_text.append("[2] 📈 Reporte de Ventas (SQL)\n", style="blue")
        menu_text.append("[3] 📈 Reporte Profit Pivot (Pandas)\n", style="blue")
        menu_text.append("[4] ❌ Salir\n", style="red")

        console.print(Panel(menu_text, title="🚀 [bold magenta]Menú Principal[/bold magenta]", expand=False, border_style="yellow"))

        opcion = Prompt.ask("[bold yellow]Selecciona una opción[/bold yellow]", choices=["1", "2", "3", "4"], default="4")

        if opcion == "1":
            IngestDataProducts(app)
        elif opcion == "2":
            GenerateReportVentas(app)
        elif opcion == "3":
            GenerateReportProfitPivotPandas(app)
        elif opcion == "4":
            break
        else:
            print("Opción no reconocida")
