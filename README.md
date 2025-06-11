#Sprint7
Análisis Exploratorio de Datos de Anuncios de Coches
Este proyecto presenta una aplicación web interactiva construida con Streamlit para realizar un análisis exploratorio de datos (EDA) sobre un conjunto de datos de anuncios de venta de vehículos en Estados Unidos.

 Descripción
El objetivo principal de esta aplicación es proporcionar una herramienta visual y sencilla para explorar las relaciones y distribuciones dentro de los datos de vehículos. En lugar de ejecutar código en un notebook estático, la aplicación permite a los usuarios generar visualizaciones interactivas con solo hacer clic en un botón, facilitando la obtención de insights rápidos sobre el mercado de coches de segunda mano.

 Funcionalidad
La aplicación web ofrece la siguiente funcionalidad:

Carga de Datos: Lee y procesa el conjunto de datos vehicles_us.csv utilizando la librería pandas.

Visualizaciones Interactivas: Permite a los usuarios generar dos tipos de gráficos interactivos creados con plotly-express:

Histograma de Odómetro: Al hacer clic en el primer botón, se genera un histograma que muestra la distribución del kilometraje (odómetro) de los vehículos en el conjunto de datos. Esto ayuda a entender qué rangos de kilometraje son más comunes.

Gráfico de Dispersión (Precio vs. Año): Al hacer clic en el segundo botón, se construye un gráfico de dispersión que revela la relación entre el precio de un vehículo y su año de fabricación. Esto permite visualizar tendencias, como si los coches más nuevos son consistentemente más caros.