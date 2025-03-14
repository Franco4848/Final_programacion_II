from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)
mysql = MySQL(app)

load_dotenv()

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')


@app.route("/", methods=['GET'])
def clientes_espanioles():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clientes WHERE Pais = "Spain"')
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return jsonify(data)

@app.route("/gama", methods=['GET'])
def gama_herramientas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM gamasproductos WHERE Gama = "Herramientas"')
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return jsonify(data)

#POST
@app.route("/add", methods=['POST'])
def add_ofice():
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO oficinas (CodigoOficina, Ciudad, Pais, Region, CodigoPostal, Telefono, LineaDireccion1, LineaDireccion2) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''', 
                    (data['CodigoOficina'], data['Ciudad'], data['Pais'], data['Region'], data['CodigoPostal'], 
                     data['Telefono'], data['LineaDireccion1'], data['LineaDireccion2']))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Pais agregado correctamente"})
    except Exception as e:
        return jsonify({"error":str(e)}), 500    

# Codigo de prueba para agregar oficina
'''{
    "CodigoOficina":"MDZ-AR", 
    "Ciudad":"Mendoza", 
    "Pais":"Argentina", 
    "Region":"Cuyo", 
    "CodigoPostal":"5515", 
    "Telefono":"26168779", 
    "LineaDireccion1":"Direccion ficticia 1", 
    "LineaDireccion2":"Direccion ficticia 1"
}'''


#traer pedido segun estado
@app.route("/pedidos", methods=['GET'])
def pedido_segun_estado():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM pedidos WHERE Estado = "Entregado"')
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)