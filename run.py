from config import Config
from app import create_app, db
from flask_migrate import Migrate

app = create_app(Config)
Migrate(app, db)

if __name__ == '__main__':
    app.run()
