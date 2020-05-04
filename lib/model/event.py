from typing import List
from sqlalchemy import Column, Integer, String, Date, Time, Text

from lib.connector import db, ma

class EventModel(db.Model):
  __tablename__ = "event"

  id = Column(Integer, primary_key=True)
  title = Column(String(255), nullable=False)
  image = Column(String(255))

  @classmethod
  def find_by_id(cls, id) -> "EventModel":
    return cls.query.filter_by(id=id).first()

  @classmethod
  def get_all_from_db(cls) -> List["EventModel"]:
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


class EventSchema(ma.ModelSchema):
  class Meta:
    model = EventModel