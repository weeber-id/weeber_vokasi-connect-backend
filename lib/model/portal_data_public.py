from typing import List
from sqlalchemy import Column, Integer, String, Date, Time, Text, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import fields

from lib.connector import db, ma
from lib.model.department import DepartmentSchema

class PortalDataModel(db.Model):
  """
  +---------------+--------------+------+-----+---------+----------------+
  | Field         | Type         | Null | Key | Default | Extra          |
  +---------------+--------------+------+-----+---------+----------------+
  | id            | int unsigned | NO   | PRI | NULL    | auto_increment |
  | title         | varchar(255) | NO   |     | NULL    |                |
  | department_id | int unsigned | NO   | MUL | NULL    |                |
  | link          | varchar(255) | NO   |     | NULL    |                |
  +---------------+--------------+------+-----+---------+----------------+
  """
  __tablename__ = "portal_data_public"

  id = Column(Integer, primary_key=True)
  title = Column(String(255), nullable=False)
  department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
  link = Column(String(255), nullable=False)
  
  department = relationship("DepartmentModel")


class PortalDataSchema(ma.ModelSchema):
  class Meta:
    model = PortalDataModel
  department = fields.Nested(DepartmentSchema)