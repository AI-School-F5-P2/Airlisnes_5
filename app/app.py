from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Cargar el modelo desde el archivo pickle
with open('pipeline_with_model.pkl', 'rb') as model_file:
    modelo = pickle.load(model_file)

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

    # Obtener las calificaciones de servicios
    servicios = {}
    for servicio in request.form:
        if servicio != 'Gender' and servicio != 'Customer Type' and servicio != 'Type of Travel' and servicio != 'Class' and servicio != 'Age' and servicio != 'Flight Distance':
            servicios[servicio] = int(request.form[servicio])

    # Crear un DataFrame con los datos del formulario
    data = {
        'Gender': [gender],
        'Customer Type': [customer_type],
        'Type of Travel': [type_of_travel],
        'Class': [class_type],
        'Age': [age],
        'Flight Distance': [flight_distance]
    }
    data.update(servicios)
    df = pd.DataFrame(data)

    # Preprocesar los datos con el mismo preprocesador utilizado para entrenar el modelo
    with open('preprocessor.pkl', 'rb') as preprocessor_file:
        preprocessor = pickle.load(preprocessor_file)

    X = preprocessor.transform(df)

    # Realizar predicción con el modelo
    resultado_prediccion = modelo.predict(X)

    # Guardar los datos en un archivo
    with open('respuestas_clientes.csv', 'a') as nuevos_datos:
        nuevos_datos.write(f'Género: {gender}, Tipo de Cliente: {customer_type}, Tipo de Viaje: {type_of_travel}, Clase: {class_type}, Edad: {age}, Distancia de Vuelo: {flight_distance}, Predicción del Modelo: {resultado_prediccion[0]}\n')

    return jsonify({'mensaje': 'Formulario procesado con éxito'})

if __name__ == '__main__':
    app.run(debug=True)
