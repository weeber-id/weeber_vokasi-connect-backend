from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, String

from lib.connector import db, ma


class CategoryModel(db.Model):
  """
  +-------+--------------+------+-----+---------+-------+
  | Field | Type         | Null | Key | Default | Extra |
  +-------+--------------+------+-----+---------+-------+
  | id    | int unsigned | NO   | PRI | NULL    |       |
  | name  | varchar(255) | NO   |     | NULL    |       |
  +-------+--------------+------+-----+---------+-------+
  """
  __tablename__ = "category"

  id = Column(INTEGER(unsigned=True), primary_key=True)
  name = Column(String(255), nullable=False)


class CategorySchema(ma.ModelSchema):
  class Meta:
    model = CategoryModel