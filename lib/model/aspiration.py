from typing import List
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, Integer, String, Date, Time, Text

from lib.connector import db, ma

class AspirationModel(db.Model):
  """
  +---------+---------------+------+-----+---------+----------------+
  | Field   | Type          | Null | Key | Default | Extra          |
  +---------+---------------+------+-----+---------+----------------+
  | id      | int unsigned  | NO   | PRI | NULL    | auto_increment |
  | nama    | varchar(255)  | YES  |     | NULL    |                |
  | npm     | varchar(255)  | YES  |     | NULL    |                |
  | prodi   | varchar(255)  | YES  |     | NULL    |                |
  | no_hp   | varchar(20)   | YES  |     | NULL    |                |
  | keluhan | varchar(1000) | YES  |     | NULL    |                |
  +---------+---------------+------+-----+---------+----------------+
  """
  __tablename__ = "aspiration_center"

  id = Column(INTEGER(unsigned=True), primary_key=True)
  nama = Column(String(255))
  npm = Column(String(255))
  prodi = Column(String(255))
  no_hp = Column(String(255))
  keluhan = Column(String(255))


class AspirationSchema(ma.ModelSchema):
  class Meta:
    model = AspirationModel