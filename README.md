# Analisis de datos con python

## Descripción del codigo

>Este código en Python contiene funciones que permiten cargar, limpiar, visualizar y analizar datos utilizando la librería Pandas y la técnica de regresión lineal de la librería Scikit-Learn.

## Funciones 

### ___cargar_datos(file_csv: str) -> pd.DataFrame___
La función `cargar_datos` recibe como argumento la ruta de un archivo CSV, utiliza la librería Pandas para leer el archivo y devuelve un objeto DataFrame que contiene los datos.

### ___visualizar_datos(datos_limpios: pd.DataFrame) -> None___
La función `visualizar_datos` recibe como argumento un objeto DataFrame con los datos limpios y muestra un histograma de la columna "Country".

### ___analizar_datos(datos: pd.DataFrame, columna_x: List[str], columna_y: str) -> LinearRegression___
La función `analizar_datos` recibe como argumento un objeto DataFrame con los datos, una lista con el nombre de la columna x y el nombre de la columna y. Crea un objeto LinearRegression, define los valores x e y para entrenar el modelo y devuelve el modelo entrenado.

### ___comunicado(texto: str) -> None___
La función `comunicado` recibe un mensaje de texto y lo imprime en la consola.

----
## Uso

>Para usar este código, es necesario tener instaladas las librerías Pandas, Matplotlib y Scikit-Learn.

- `pandas as pd`: Importa la biblioteca pandas y se le asigna el alias "pd". Se utiliza para trabajar con datos estructurados y tabulares.

- `matplotlib.pyplot as plt`: Importa la subbiblioteca pyplot de la biblioteca matplotlib y se le asigna el alias "plt". Se utiliza para crear visualizaciones y gráficos a partir de los datos.

- `from sklearn.linear_model import LinearRegression`: Importa la clase LinearRegression del submódulo linear_model de la biblioteca scikit-learn (también conocida como sklearn). Se utiliza para construir modelos de regresión lineal.

Estas importaciones son necesarias para que el código pueda utilizar las funciones y clases de estas bibliotecas en las diferentes funciones que se han definido.

Una vez instaladas las librerías, se pueden llamar las funciones en el siguiente orden:

1. cargar_datos: cargar los datos desde un archivo CSV.
2. limpiar_datos: limpiar los datos.
3. visualizar_datos: visualizar los datos limpios.
4. analizar_datos: realizar el análisis de datos con regresión lineal.
5. comunicado: imprimir un mensaje en la consola.
