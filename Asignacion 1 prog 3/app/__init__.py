from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def bienvenida():
    return render_template('hola.html')

@app.route('/comision', methods= ["POST"])
def comisiones():
    nombre = request.form['nombre']
    ventas = float(request.form['ventas'])

    if ventas < 25000:
            comisiones = ventas * 0.03
    elif ventas >= 25000 and ventas < 50000:
            comisiones = ventas * 0.05
    elif ventas >= 50000 and ventas < 75000:
            comisiones = ventas * 0.07
    elif ventas >= 75000 and ventas < 100000:
            comisiones = ventas * 0.1
    elif ventas >= 100000:
            comisiones = ventas * 0.15
    elif ventas == 0 :
            print("El vendedor deberia realizar mas ventas en el mes!")

    guardar =(nombre,+ ventas,+ comisiones)
    comsion = open("comisiones1.csv", "a+")
    comsion.write(nombre + "\n")
    comsion.close()

    return render_template('comision.html', nom=nombre, com=comisiones)


if __name__ == "__main__":
    app.run(debug=True)
