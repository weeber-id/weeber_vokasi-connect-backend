from typing import List
from sqlalchemy import Column, Integer, String

from lib.connector import db, ma


class RuangPrestasiModel(db.Model):
  __tablename__ = "ruang_prestasi"

  id = Column(Integer, primary_key=True)
  nama = Column(String(255))
  jurusan = Column(String(255))
  angkatan = Column(String(255))
  prestasi = Column(String(255), nullable=False)

  @classmethod
  def find_by_id(cls, id) -> "RuangPrestasiModel":
    return cls.query.filter_by(id=id).first()

  @classmethod
  def get_all_from_db(cls) -> List["RuangPrestasiModel"]:
    return cls.query.all()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def update_to_db(self, params:dict):
    for key, value in params.items():
      setattr(self, key, value)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()


class RuangPrestasiSchema(ma.ModelSchema):
  class Meta:
    model = RuangPrestasiModel