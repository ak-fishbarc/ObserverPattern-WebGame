from os import path

from __init__ import create_app, create_blueprints, create_db, create_models, create_migrate, \
    initialize_migration, db_migrate, db_migrate_upgrade
from config import Config
import models

game_app = create_app(Config)
sql_database = create_db(game_app)
user_model = models.create_user_model(sql_database)
create_models(game_app, sql_database)
migration = create_migrate(game_app, sql_database)
create_blueprints(game_app, sql_database, user_model)

if not path.exists('./migrations'):
    initialize_migration(game_app)
    db_migrate(game_app)
    db_migrate_upgrade(game_app)

if __name__ == '__main__':
    game_app.run(debug=True)


