from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Cargar el modelo desde el archivo pickle
with open('pipeline_with_model.pkl', 'rb') as model_file:
    modelo = pickle.load(model_file)

# Mapa inverso para convertir 0 y 1 en etiquetas
mapa_inverso = {0: 'neutral or dissatisfied', 1: 'satisfied'}

# Ruta para mostrar el formulario
@app.route('/')
def formulario():
    return render_template('formulario.html')

# Ruta para procesar el formulario
@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    # Obtener los datos del formulario
    gender = request.form['Gender']
    customer_type = request.form['Customer Type']
    type_of_travel = request.form['Type of Travel']
    class_type = request.form['Class']
    age = int(request.form['Age'])
    flight_distance = int(request.form['Flight Distance'])

    # Crear un DataFrame de pandas con los datos del formulario
    data = {
        'Gender': [gender],
        'Customer Type': [customer_type],
        'Type of Travel': [type_of_travel],
        'Class': [class_type],
        'Age': [age],
        'Flight Distance': [flight_distance]
    }

    df = pd.DataFrame(data)

    # Obtener las calificaciones de servicios
    servicios = {}
    for servicio in request.form:
        if servicio not in data:
            servicios[servicio] = int(request.form[servicio])

    # Agregar las calificaciones de servicios al DataFrame
    df = df.assign(**servicios)

    # Realizar predicción con el modelo
    resultado_prediccion = modelo.predict(df)

    # Convertir la predicción a etiquetas
    etiqueta_prediccion = mapa_inverso[resultado_prediccion[0]]

    # Crear una tabla HTML para mostrar los datos y la predicción
    tabla_html = f'''
        <table>
            <tr><th>Dato</th><th>Valor</th></tr>
            <tr><td>Género</td><td>{gender}</td></tr>
            <tr><td>Tipo de Cliente</td><td>{customer_type}</td></tr>
            <tr><td>Tipo de Viaje</td><td>{type_of_travel}</td></tr>
            <tr><td>Clase</td><td>{class_type}</td></tr>
            <tr><td>Edad</td><td>{age}</td></tr>
            <tr><td>Distancia de Vuelo</td><td>{flight_distance}</td></tr>
            <tr><td>Predicción del Modelo</td><td>{etiqueta_prediccion}</td></tr>
        </table>
    '''

    # Renderizar la plantilla HTML y pasar la tabla como contexto
    return render_template('respuesta.html', tabla_html=tabla_html)

if __name__ == '__main__':
    app.run(debug=True)
