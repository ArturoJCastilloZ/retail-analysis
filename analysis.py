import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Función para cargar datos desde un archivo CSV
def cargar_datos(file_csv):
    '''La función recibe como argumento la ruta de un archivo CSV, 
    utiliza la librería pandas para leer el archivo 
    y devuelve un objeto DataFrame que contiene los datos.

    Args:
        file_csv: Ruta de un archivo CSV
    
    Returns:
        pd.read_csv(file_csv): Dataframe con los datos
    '''
    return pd.read_csv(file_csv)


# Función para limpiar los datos, eliminando valores nulos y duplicados
def limpiar_datos(datos_cargados):
    '''La función recibe como argumento un objeto DataFrame con los datos cargados previamente,
    elimina las filas que tienen valores nulos y las filas duplicadas. 
    Finalmente, devuelve el DataFrame limpio.

    Args:
        datos_cargados: Objeto DataFrame
    
    Returns:
        datos_cargadis: Dataframe limpio sin valores nulos y fuilas duplicadas
    '''
    datos_cargados.dropna(inplace=True)
    datos_cargados.drop_duplicates(inplace=True)
    return datos_cargados


# Función para visualizar los datos limpios
def visualizar_datos(datos_limpios):
    '''La función recibe como argumento un objeto DataFrame 
    con los datos limpios y muestra un histograma de la columna "Country".

    Args:
        datos_limpios: Objeto DataFrame con datos limpios
    
    Returns:
        Muestra un histograma de la columna "Country"
    '''
    plt.hist(datos_limpios['Country'])  # Crear un histograma para la columna "Country"
    plt.show()  # Mostrar el histograma


# Función para realizar el análisis de datos con regresión lineal
def analizar_datos(datos, columna_x, columna_y):
    '''La función recibe como argumento un objeto DataFrame con los datos, una lista con el 
    nombre de la columna x y el nombre de la columna y. Crea un objeto LinearRegression, 
    define los valores x e y para entrenar el modelo y devuelve el modelo entrenado.

    Args:
        datos: DataFrame con los datos
        columna_x: Lista con el nombre de la columna
        columna_y: nombre de la columna
    
    Returns:
        Define los valores x e y para entrenar el modelo y devuelve el modelo entrenado
    '''
    model = LinearRegression()  # Crear una instancia de la clase LinearRegression
    x = datos[columna_x]  # Seleccionar la columna correspondiente a "columna_x"
    y = datos[columna_y]  # Seleccionar la columna correspondiente a "columna_y"
    model.fit(x, y)  # Ajustar el modelo utilizando las variables independiente y dependiente
    return model  # Devolver el modelo


# Función para imprimir un mensaje en la consola
def comunicado(texto):
    print(texto)


if __name__ == '__main__':
    FILE_CSV = './Online Retail.csv'
    datos_cargados = cargar_datos(FILE_CSV)  # Cargar los datos desde el archivo CSV
    datos_limpios = limpiar_datos(datos_cargados)  # Limpiar los datos
    visualizar_datos(datos_limpios)  # Visualizar los datos limpios
    modelo = analizar_datos(datos_limpios, ['UnitPrice'], 'Quantity')  # Analizar los datos con regresión lineal
    print(modelo.coef_)  # Imprimir el coeficiente de regresión lineal
    comunicado("Listo")  # Imprimir un mensaje en la consola
