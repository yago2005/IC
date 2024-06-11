#Cargando Bibliotecas
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#Agregar un título
st.title("Aplicación para cargar archivos de Excel")

#Agregando una imagen
st.image("https://icontinental.edu.pe/wp-content/uploads/2020/07/Logo-instituto-continental.svg", caption="Logo IC", use_column_width=True)

#Subir un archivo en excel
archivo_excel = st.file_uploader("Selecciona un archivo Excel", type="xlsx")

if archivo_excel:
    try:
        df = pd.read_excel(archivo_excel)

        #Mostrar el contenido del df (DataFrame)
        st.dataframe(df)

        #Opciones adicionales
        #1. Mostrar información específica del DF
        st.write("Información del DataFrame:")
        st.write("Número de filas:", df.shape[0])
        st.write("Número de columnas:", df.shape[1])
        st.write("Nombres de las columnas:", df.columns.tolist())

        #2. Seleccionar las columnas para mostrar
        columnas_seleccionadas = st.multiselect("Selecciona las columnas para mostrar:", df.columns)
        if columnas_seleccionadas:
            st.dataframe(df[columnas_seleccionadas])
        #3. Filtrar datos por rango de fechas
        if 'Fecha' in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df['Fecha']):
                fecha_inicio = st.date_input("Fecha de inicio")
                fecha_fin = st.date_input("Fecha fin")
                if fecha_inicio and fecha_fin:
                    fecha_inicio = pd.to_datetime(fecha_inicio)
                    fecha_fin = pd.to_datetime(fecha_fin)
                    df_filtrado = df[(df['Fecha'] >= fecha_inicio) & (df['Fecha'] <= fecha_fin)]
                    st.dataframe(df_filtrado)
            else:
                st.write("La columna 'Fecha' no es de tipo datatime")
        else:
            st.write("La columna 'Fecha' no está presente en el archivo Excel")



        #4. Graficar desde una columna seleccionada
        columna_grafico = st.selectbox("slecciona una columna para graficar:", df.columns)
        if columna_grafico:
            st.write(f"Graficando Columna: {columna_grafico}")
            fig, ax = plt.subplots()
            plt.plot(df[columna_grafico])
            plt.xlabel('Índice')
            plt.ylabel(columna_grafico)
            plt.title(f'Gráfico de {columna_grafico}')
            st.pyplot(fig)


    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
