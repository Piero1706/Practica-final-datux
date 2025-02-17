import pandas as pd
import os

def GenerateReportProfitPivotPandas(app):
    file_path = "proyecto/files/datafuente.xls"
    output_path = "proyecto/files/reporte_ganancias.csv"
    
    if not os.path.exists(file_path):
        print(f"❌ ERROR: El archivo {file_path} no existe.")
        return
    
    try:
        df = pd.read_excel(file_path)
        
        column_mapping = {
            'Order Date': 'Order Date',
            'Category': 'Category',
            'Profit': 'Profit'
        }
        
        df.rename(columns=column_mapping, inplace=True)
        
        required_columns = ['Order Date', 'Category', 'Profit']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"❌ ERROR: Faltan las siguientes columnas en el archivo Excel: {missing_columns}")
            print(f"🔍 Columnas encontradas en el archivo: {list(df.columns)}")
            return
        
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
        
        pivot_profit = df.pivot_table(values='Profit', index='Category', aggfunc='sum')
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        pivot_profit.to_csv(output_path)
        
        print(f"✅ Reporte generado con éxito: {output_path}")
    except Exception as e:
        print(f"❌ ERROR: Ocurrió un problema al procesar el archivo Excel. Detalles: {e}")
