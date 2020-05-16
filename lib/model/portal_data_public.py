from typing import List
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, Integer, String, Date, Time, Text, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import fields

from lib.connector import db, ma
from lib.model.category import CategorySchema

class PortalDataModel(db.Model):
  """
  +-------------+--------------+------+-----+---------+----------------+
  | Field       | Type         | Null | Key | Default | Extra          |
  +-------------+--------------+------+-----+---------+----------------+
  | id          | int unsigned | NO   | PRI | NULL    | auto_increment |
  | title       | varchar(255) | NO   |     | NULL    |                |
  | tanggal     | date         | NO   |     | NULL    |                |
  | link        | varchar(255) | NO   |     | NULL    |                |
  | category_id | int unsigned | NO   | MUL | NULL    |                |
  +-------------+--------------+------+-----+---------+----------------+
  """
  __tablename__ = "portal_data_public"

  id = Column(INTEGER(unsigned=True), primary_key=True)
  title = Column(String(255), nullable=False)
  tanggal = Column(Date, nullable=False)
  link = Column(String(255), nullable=False)
  category_id = Column(INTEGER(unsigned=True), ForeignKey("category.id"), nullable=False)
  
  category = relationship("CategoryModel")


class PortalDataSchema(ma.ModelSchema):
  class Meta:
    model = PortalDataModel
  category = fields.Nested(CategorySchema)