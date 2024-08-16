from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Crea la instancia de la aplicación
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cinesapiens:cinesapiens2024@localhost/cinesapiens-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crea la instancia de SQLAlchemy
db = SQLAlchemy(app)

# Importa las rutas después de configurar db
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
