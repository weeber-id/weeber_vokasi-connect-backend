import os

MYSQL_ADDRESS = os.environ.get("MYSQL_ADDRESS")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")


database_URI = "mysql+pymysql://{}:{}@{}/{}".format(
  MYSQL_USER,
  MYSQL_PASSWORD,
  MYSQL_ADDRESS,
  MYSQL_DATABASE,
  )