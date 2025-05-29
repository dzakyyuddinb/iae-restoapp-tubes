from flask import Flask, request, jsonify
from models import db
from gqlschema.schema import schema
from flask_graphql import GraphQLView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/restoapp_user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return "User Service GraphQL is running!"

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # aktifkan UI browser GraphiQL
        
    ),
)

if __name__ == "__main__":
    app.run(port=5001, debug=True)