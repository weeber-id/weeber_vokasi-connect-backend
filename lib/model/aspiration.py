from typing import List
from sqlalchemy import Column, Integer, String, Date, Time, Text

from lib.connector import db, ma

class AspirationModel(db.Model):
  __tablename__ = "aspiration_center"

  id = Column(Integer, primary_key=True)
  nama = Column(String(255))
  npm = Column(String(255))
  prodi = Column(String(255))
  no_hp = Column(String(255))
  keluhan = Column(String(255))

  @classmethod
  def find_by_id(cls, id) -> "AspirationModel":
    return cls.query.filter_by(id=id).first()

  @classmethod
  def get_all_from_db(cls) -> List["AspirationModel"]:
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


class AspirationSchema(ma.ModelSchema):
  class Meta:
    model = AspirationModel