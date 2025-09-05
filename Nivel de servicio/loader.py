# loader.py
import pandas as pd
import glob
import os

def cargar_datos(ruta_carpeta):
    """
    Carga todos los archivos Excel (.xlsx o .xls) de una carpeta y los unifica en un DataFrame.
    
    Parámetros:
        ruta_carpeta (str): Ruta a la carpeta que contiene los archivos Excel.
    
    Retorna:
        pd.DataFrame: DataFrame con todos los datos unificados.
    """
    # Buscar todos los archivos Excel en la carpeta
    archivos = glob.glob(os.path.join(ruta_carpeta, "*.xlsx")) + glob.glob(os.path.join(ruta_carpeta, "*.xls"))
    
    if not archivos:
        raise FileNotFoundError(f"No se encontraron archivos Excel en la carpeta: {ruta_carpeta}")
    
    # Lista para almacenar cada DataFrame
    lista_df = []
    
    for archivo in archivos:
        try:
            df = pd.read_excel(archivo)
            lista_df.append(df)
            print(f"✅ Archivo cargado: {archivo} ({df.shape[0]} filas, {df.shape[1]} columnas)")
        except Exception as e:
            print(f"❌ Error al cargar {archivo}: {e}")
    
    # Unir todos los DataFrames en uno solo
    df_unido = pd.concat(lista_df, ignore_index=True)
    print(f"📊 DataFrame unificado: {df_unido.shape[0]} filas, {df_unido.shape[1]} columnas")
    
    return df_unido
