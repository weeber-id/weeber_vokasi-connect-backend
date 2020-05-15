from typing import List
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, Integer, String, Date, Time, Text

from lib.connector import db, ma

class DepartmentModel(db.Model):
  """
  +-------+--------------+------+-----+---------+----------------+
  | Field | Type         | Null | Key | Default | Extra          |
  +-------+--------------+------+-----+---------+----------------+
  | id    | int unsigned | NO   | PRI | NULL    | auto_increment |
  | name  | varchar(255) | NO   |     | NULL    |                |
  +-------+--------------+------+-----+---------+----------------+
  """
  __tablename__ = "department"

  id = Column(INTEGER(unsigned=True), primary_key=True)
  name = Column(String(255), nullable=False)


class DepartmentSchema(ma.ModelSchema):
  class Meta:
    model = DepartmentModel