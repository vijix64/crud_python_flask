from flask import Flask, render_template,request, redirect, url_for
import os
import database as db

temp_dir= os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
temp_dir = os.path.join(temp_dir,'src', 'temp')

app = Flask(__name__, template_folder = temp_dir)


#rutas de la aplicacion 

@app.route('/')
def home():
    cursor = db.conexion.cursor()
    cursor.execute("SELECT * FROM usersTemp")
    result = cursor.fetchall()

    #convertir los idatos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in result:
        insertObject.append(dict(zip(columnNames, record)))

    cursor.close()
    return render_template('index.html', data=insertObject)

@app.route('/user', methods=['POST'])
def addUser():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor = db.conexion.cursor()
        sql = "INSERT INTO usersTemp (username, name, password) VALUES (%s, %s, %s)"
        data = (username,name,password)
        cursor.execute(sql, data)
        db.conexion.commit()

    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.conexion.cursor()
    sql = "DELETE FROM usersTemp WHERE iduser=%s"
    data =(id,)
    cursor.execute(sql, data)
    db.conexion.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor = db.conexion.cursor()
        sql = "UPDATE usersTemp SET username = %s, name =%s, password =%s WHERE iduser = %s"
        data = (username,name,password, id)
        cursor.execute(sql, data)
        db.conexion.commit()

    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True, port=4000)