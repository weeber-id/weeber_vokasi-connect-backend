from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.mysql import INTEGER

from lib.connector import db, ma

class UserAdminModel(db.Model):
  """
  +----------+--------------+------+-----+---------+----------------+
  | Field    | Type         | Null | Key | Default | Extra          |
  +----------+--------------+------+-----+---------+----------------+
  | id       | int unsigned | NO   | PRI | NULL    | auto_increment |
  | username | varchar(255) | NO   |     | NULL    |                |
  | password | varchar(255) | NO   |     | NULL    |                |
  | role     | int          | NO   |     | NULL    |                |
  +----------+--------------+------+-----+---------+----------------+
  """
  __tablename__ = "user_admin"
  
  id = Column(INTEGER(unsigned=True), primary_key=True)
  username = Column(String(255), nullable=False)
  password = Column(String(255), nullable=False)
  role = Column(Integer, nullable=False)


class UserAdminSchema(ma.ModelSchema):
  class Meta:
    model = UserAdminModel