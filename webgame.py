from os import path

from __init__ import create_app, create_blueprints, create_db, create_models, create_migrate, \
    initialize_migration, db_migrate, db_migrate_upgrade, create_mail, create_mongodb
from config import Config
import models


game_app = create_app(Config)
sql_database = create_db(game_app)
nosql_database = create_mongodb(game_app)
user_model = models.create_user_model(sql_database)
create_models(game_app, sql_database)
migration = create_migrate(game_app, sql_database)
mail = create_mail(game_app)
create_blueprints(game_app, sql_database, nosql_database, user_model, mail)

if not path.exists('./migrations'):
    initialize_migration(game_app)
    db_migrate(game_app)
    db_migrate_upgrade(game_app)


if __name__ == '__main__':
    game_app.run(debug=True)


