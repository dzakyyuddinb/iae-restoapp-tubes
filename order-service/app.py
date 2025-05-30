from flask import Flask, request, jsonify
from models import db
from gqlschema.schema import schema
from flask_graphql import GraphQLView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/restoapp_order'  # Ganti sesuai service
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()
    print("Database connected:", db.engine.url)


@app.route('/')
def index():
    return "Order Service GraphQL is running!"  # Ganti sesuai service

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # aktifkan UI browser GraphiQL
    )
)

if __name__ == "__main__":
    app.run(port=5003, debug=True)  # Ganti port sesuai service