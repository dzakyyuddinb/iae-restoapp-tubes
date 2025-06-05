import os
import sys
from flask import Flask, request, jsonify
from models import db
from gqlschema.schema import schema
from flask_graphql import GraphQLView
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ← letakkan setelah membuat app

# Konfigurasi database
import os
mysql_host = os.getenv('MYSQL_HOST', 'mysql')
mysql_db = os.getenv('MYSQL_DB', 'restoapp')
mysql_password = os.getenv('MYSQL_ROOT_PASSWORD', 'root')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{mysql_password}@{mysql_host}/{mysql_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi SQLAlchemy
db.init_app(app)

# Tambahkan route untuk pengecekan sederhana
@app.route('/')
def index():
    return "Menu Service GraphQL is running!"

# Tambahkan GraphQL endpoint
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Aktifkan UI GraphiQL
    )
)

# Jalankan aplikasi
if __name__ == "__main__":
    port = 5000
    if 'FLASK_RUN_PORT' in os.environ:
        port = int(os.environ['FLASK_RUN_PORT'])
    for arg in sys.argv:
        if arg.startswith('--port='):
            port = int(arg.split('=')[1])
    app.run(host='0.0.0.0', port=port, debug=True)
