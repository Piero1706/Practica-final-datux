import pandas as pd
from config.app import App

def GenerateReportProfitPivotPandas(app: App):
    """
    Genera un reporte de Profit por Categoría y Sub-Categoría utilizando
    únicamente Pandas (pivot table), sin consultas SQL.
    Luego envía el reporte por correo.
    """
    pathData = "/workspaces/Practica-final-datux/proyecto/files/datafuente.xls"
    df = pd.read_excel(pathData, sheet_name="Orders")
 
    pivot_profit = df.pivot_table(
        index="Category",       
        columns="Sub-Category", 
        values="Profit",        
        aggfunc="sum"           
    )

    fecha = "reporte_profit_pivot"
    path = f"/workspaces/workspacepy0125v2/proyecto/files/data_{fecha}.csv"
    pivot_profit.to_csv(path)
    print(f"✅ Reporte pivot de Profit generado en: {path}")

    subject = "Reporte de Profit (Pivot) por Categoría y Sub-Categoría"
    body = (
        "Hola,\n\n"
        "Adjunto encontrarás el reporte de Profit agrupado por Categoría y Sub-Categoría "
        "generado con una pivot table en Pandas.\n\n"
        "Saludos,\nEl Equipo"
    )
    app.mail.send_email(
        receiver_email="from@example.com",
        subject=subject,
        body=body,
        file_path=path
    )
    print("✅ Correo enviado con el reporte de Profit (Pivot).")
