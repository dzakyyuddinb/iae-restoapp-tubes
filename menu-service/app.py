from flask import Flask, request, jsonify
from models import db
from gqlschema.schema import schema
from flask_graphql import GraphQLView
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ← letakkan setelah membuat app

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/restoapp_menu'
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
    app.run(port=5002, debug=True)
