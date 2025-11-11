from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------------
# Página principal (menú)
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')


# -------------------------------
# Ejercicio 1: Formulario de Notas
# -------------------------------
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        try:
            # Capturamos los datos del formulario
            nota1 = float(request.form.get('nota1', 0))
            nota2 = float(request.form.get('nota2', 0))
            nota3 = float(request.form.get('nota3', 0))
            asistencia = float(request.form.get('asistencia', 0))

            # Validamos los rangos permitidos
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                resultado = {'error': 'Las notas deben estar entre 10 y 70.'}
            elif not (0 <= asistencia <= 100):
                resultado = {'error': 'La asistencia debe estar entre 0 y 100.'}
            else:
                promedio = (nota1 + nota2 + nota3) / 3

                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO ✅"
                else:
                    estado = "REPROBADO ❌"

                resultado = {
                    'promedio': round(promedio, 2),
                    'asistencia': asistencia,
                    'estado': estado
                }

        except ValueError:
            resultado = {'error': 'Por favor, ingrese valores válidos.'}

    return render_template('ejercicio1.html', resultado=resultado)


# -------------------------------
# Ejercicio 2: Formulario de Nombres
# -------------------------------
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        # Capturamos los nombres
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()

        # Validamos campos
        if not nombre1 or not nombre2 or not nombre3:
            resultado = {'error': 'Por favor, completa los tres nombres.'}
        elif len({nombre1, nombre2, nombre3}) < 3:
            resultado = {'error': 'Los nombres deben ser diferentes.'}
        else:
            nombres = [nombre1, nombre2, nombre3]
            nombre_mas_largo = max(nombres, key=len)
            longitud = len(nombre_mas_largo)
            resultado = {
                'nombre': nombre_mas_largo,
                'longitud': longitud
            }

    return render_template('ejercicio2.html', resultado=resultado)


# -------------------------------
# Ejecutar aplicación
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
