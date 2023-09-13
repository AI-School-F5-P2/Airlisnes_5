from flask import Flask, request, render_template
from flask import Flask, render_template, request

app = Flask(name)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los datos del formulario enviado por el usuario
        nombre = request.form['nombre']
        edad = request.form['edad']
        opinion = request.form['opinion']

        # Aquí puedes procesar los datos como desees, por ejemplo, guardarlos en una base de datos o realizar predicciones con tu modelo

        # En este ejemplo, simplemente los imprimimos
        print(f'Nombre: {nombre}')
        print(f'Edad: {edad}')
        print(f'Opinión: {opinion}')

    return render_template('formulario.html')


if name == 'main':
    app.run(debug=True)


app = Flask(name)


@app.route('/', methods=['GET', 'POST'])
def opinion_form():
    if request.method == 'POST':
        # Obtener los datos del formulario
        gender = request.form['gender']
        customer_type = request.form['customer_type']
        type_of_travel = request.form['type_of_travel']
        class_choice = request.form['class']
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])

        # Validar los campos de calificación de servicios
        services = [
            'inflight_wifi_service',
            'departure_arrival_time_convenient',
            # Agregar más campos de servicios aquí
        ]

        service_ratings = {}
        for service in services:
            rating = int(request.form[service])
            if rating < 1 or rating > 5:
                return rendertemplate('form.html', error=f'El valor de {service.replace("", " ").title()} debe estar entre 1 y 5.')

            service_ratings[service] = rating

        # Aquí puedes hacer más con los datos, como guardarlos en una base de datos o realizar análisis

        return '¡Formulario enviado con éxito!'

    return render_template('form.html')


if name == 'main':
    app.run(debug=True)
