from flask_mysqldb import MySQL

def init_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'hrishi@2006'
    app.config['MYSQL_DB'] = 'restaurant_db'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    
    mysql = MySQL(app)
    return mysql
