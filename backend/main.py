from flask import Flask
from extensions import *
from routes import book_routes

def create_app():
    app = Flask(__name__)
    CORS(app)
    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(book_routes)

    with app.app_context():
        db.create_all()  # Ensure database tables are created

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
