import os

MYSQL_ADDRESS = os.environ.get("MYSQL_ADDRESS")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")


database_URI = "mysql+pymysql://{}:{}@{}/{}".format(
  MYSQL_USER,
  MYSQL_PASSWORD,
  MYSQL_ADDRESS,
  MYSQL_DATABASE,
  )