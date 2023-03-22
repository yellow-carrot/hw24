class Config:
    DB_NAME = 'db_name'
    DB_USER = 'db_user'
    DB_PASSWORD = 'db_password'
    DB_HOST = 'db'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'