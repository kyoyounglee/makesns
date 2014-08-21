from application import app

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///sns_db?instance=amabile076:amabile076db',
    migration_directory = 'migrations'
))
