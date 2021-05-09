from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'nuspamdb'
app.config['MYSQL_DATABASE_HOST'] = 'database-2.cnr20hoyd3cu.ap-northeast-2.rds.amazonaws.com'

mysql.init_app(app)

@app.route('/')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from nuspamdb.urlinfo''')
    r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'URL_INFORMATION' : r})

if __name__ == '__main__':
    app.run()
