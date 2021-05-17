from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

# DB connection info
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'nuspamdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

# endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        urlinfo = request.form['urlinfo']
        # search
        cursor.execute("SELECT url, sort from urlinfo WHERE url LIKE %s OR sort LIKE %s", (urlinfo, urlinfo))
        conn.commit()
        data = cursor.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

