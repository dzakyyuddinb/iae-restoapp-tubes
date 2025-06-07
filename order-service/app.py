import os
import sys
import time
from flask import Flask, request, jsonify
from models import db
from gqlschema.schema import schema
from flask_graphql import GraphQLView
from flask_cors import CORS
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
CORS(app)

# Konfigurasi database dari environment variable
mysql_host = os.getenv('MYSQL_HOST', 'mysql')
mysql_db = os.getenv('MYSQL_DB', 'restoapp')
mysql_password = os.getenv('MYSQL_ROOT_PASSWORD', 'root')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{mysql_password}@{mysql_host}/{mysql_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Retry koneksi ke database
with app.app_context():
    for i in range(10):
        try:
            db.create_all()
            print("✅ Database connected:", db.engine.url)
            break
        except OperationalError as e:
            print(f"❌ Database not ready, retrying in 3s... ({i+1}/10)")
            time.sleep(3)
    else:
        print("🚫 Failed to connect to database after retries.")
        sys.exit(1)

@app.route('/')
def index():
    return "Order Service GraphQL is running!"

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == "__main__":
    port = 5000
    if 'FLASK_RUN_PORT' in os.environ:
        port = int(os.environ['FLASK_RUN_PORT'])
    for arg in sys.argv:
        if arg.startswith('--port='):
            port = int(arg.split('=')[1])
    app.run(host='0.0.0.0', port=port, debug=True)

# Note: This code is designed to be run in a Docker container with the necessary environment variables set.
# Ensure that the MySQL service is running and accessible from this container.