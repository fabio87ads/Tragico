from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'mysql669.umbler.com'
app.config['MYSQL_PORT'] = 41890
app.config['MYSQL_USER'] = 'tragicocrud'
app.config['MYSQL_PASSWORD'] = 'Tragico123'
app.config['MYSQL_DB'] = 'tragicocrud'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM produtos")
    data = cur.fetchall()
    cur.close()

    return render_template('index2.html', produtos=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Produto Adicionado Com Sucesso")
        nome = request.form['nome']
        codigo = request.form['codigo']
        preco = request.form['preco']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO produtos (nome, codigo, preco,descricao) VALUES (%s,%s, %s, %s)", (nome, codigo,preco, descricao))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Produto foi excluído com sucesso")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM produtos WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        nome = request.form['nome']
        codigo = request.form['codigo']
        preco = request.form['preco']
        descricao = request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE produtos
               SET nome=%s, codigo=%s, preco=%s, descricao=%s 
               WHERE id=%s
            """, (nome, codigo, preco,descricao, id_data))
        flash("Produto atualizado com sucesso")
        mysql.connection.commit()
        return redirect(url_for('Index'))



@app.route('/login')
def Login():
  
    return render_template('login.html' )





if __name__ == "__main__":
    app.run(debug=True)
