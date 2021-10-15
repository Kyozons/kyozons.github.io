from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def main():
    return render_template('app.html')

@app.route("/calcular",  methods=['POST'])
def calcular():
    if float(request.form['nota1']) < 10:
        num1 = float(request.form['nota1']) * 10
    else:
        num1 = float(request.form['nota1'])

    porc1 = float(request.form['porc1'])

    if float(request.form['nota2']) < 10:
        num2 = float(request.form['nota2']) * 10
    else:
        num2 = float(request.form['nota2'])

    porc2 = float(request.form['porc2'])

    if float(request.form['nota3']) < 10:
        num3 = float(request.form['nota3']) * 10
    else:
        num3 = float(request.form['nota3'])

    porc3 = float(request.form['porc3'])

    if float(request.form['nota4']) < 10:
        num4 = float(request.form['nota4']) * 10
    else:
        num4 = float(request.form['nota4'])

    porc4 = float(request.form['porc4'])

    if float(request.form['nota5']) < 10:
        num5 = float(request.form['nota5']) * 10
    else:
        num5 = float(request.form['nota5'])

    porc5 = float(request.form['porc5'])
    
    if float(request.form['nota6']) < 10:
        num6 = float(request.form['nota6']) * 10
    else:
        num6 = float(request.form['nota6'])

    porc6 = float(request.form['porc6'])
       
    if float(request.form['nota7']) < 10:
        num7 = float(request.form['nota7']) * 10
    else:
        num7 = float(request.form['nota7'])

    porc7 = float(request.form['porc7'])
    
    if float(request.form['nota8']) < 10:
        num8 = float(request.form['nota8']) * 10
    else:
        num8 = float(request.form['nota8'])

    porc8 = float(request.form['porc8'])
    
    if float(request.form['nota9']) < 10:
        num9 = float(request.form['nota9']) * 10
    else:
        num9 = float(request.form['nota9'])

    porc9 = float(request.form['porc9'])
    
    if float(request.form['nota10']) < 10:
        num10 = float(request.form['nota10']) * 10
    else:
        num10 = float(request.form['nota10'])

    porc10 = float(request.form['porc10'])
    
    if float(request.form['nota11']) < 10:
        num11 = float(request.form['nota11']) * 10
    else:
        num11 = float(request.form['nota11'])

    porc11 = float(request.form['porc11'])
    
    if float(request.form['nota12']) < 10:
        num12 = float(request.form['nota12']) * 10
    else:
        num12 = float(request.form['nota12'])

    porc12 = float(request.form['porc12'])
    
    promedio = (num1 * (porc1 / 100)) + (num2 * (porc2 / 100)) + (num3 * (porc3 / 100)) + (num4 * (porc4 / 100)) + (num5 * (porc5 / 100)) + (num6 * (porc6 / 100)) + (num7 * (porc7 / 100)) + (num8 * (porc8 / 100)) + (num9 * (porc9 / 100)) + (num10 * (porc10 / 100)) + (num11 * (porc11 / 100)) + (num12 * (porc12 / 100))
    return render_template('app.html', promedio=promedio)

