from flask import Flask, request, jsonify
import joblib

app = Flask(name)

Cargar el modelo entrenado y el preprocesador
model = joblib.load('modelo_entrenado.pkl')
preprocessor = joblib.load('preprocesador.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos de entrada de la solicitud JSON
        data = request.get_json()

        # Preprocesar los datos de entrada
        features = preprocessor.transform(data['features'])

        # Realizar la predicción con el modelo
        predictions = model.predict(features)

        # Devolver las predicciones en formato JSON
        response = {'predictions': predictions.tolist()}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if name == 'main':
    app.run(debug=True)