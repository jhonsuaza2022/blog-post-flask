SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:abuelarufina@localhost:5432/blogposts_db"

class Config:
    DEBUG = False
    SECRET_KEY = 'devblog'

    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    CKEDITOR_PKG_TYPE = 'full'
