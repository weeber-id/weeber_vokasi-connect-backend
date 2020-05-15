from typing import List
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, Integer, String

from lib.connector import db, ma


class RuangPrestasiModel(db.Model):
  """
  +----------+--------------+------+-----+---------+----------------+
  | Field    | Type         | Null | Key | Default | Extra          |
  +----------+--------------+------+-----+---------+----------------+
  | id       | int unsigned | NO   | PRI | NULL    | auto_increment |
  | nama     | varchar(255) | YES  |     | NULL    |                |
  | jurusan  | varchar(255) | YES  |     | NULL    |                |
  | angkatan | varchar(255) | YES  |     | NULL    |                |
  | prestasi | varchar(255) | NO   |     | NULL    |                |
  +----------+--------------+------+-----+---------+----------------+
  """
  __tablename__ = "ruang_prestasi"

  id = Column(INTEGER(unsigned=True), primary_key=True)
  nama = Column(String(255))
  jurusan = Column(String(255))
  angkatan = Column(String(255))
  prestasi = Column(String(255), nullable=False)


class RuangPrestasiSchema(ma.ModelSchema):
  class Meta:
    model = RuangPrestasiModel