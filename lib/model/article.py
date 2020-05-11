from typing import List
from sqlalchemy import Column, Integer, String, Date, Time, Text

from lib.connector import db, ma

class ArticleModel(db.Model):
  __tablename__ = "article"

  id = Column(Integer, primary_key=True)
  title = Column(String(255), nullable=False)
  author = Column(String(255), nullable=False)
  date_created = Column(Date, nullable=False)
  time_created = Column(Time, nullable=False)
  date_modified = Column(Date, nullable=False)
  time_modified = Column(Time, nullable=False)
  content = Column(Text, nullable=False)
  thumbnail = Column(String(255))

  @classmethod
  def find_by_id(cls, id) -> "ArticleModel":
    return cls.query.filter_by(id=id).first()

  @classmethod
  def get_all_from_db(cls) -> List["ArticleModel"]:
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


class ArticleSchema(ma.ModelSchema):
  class Meta:
    model = ArticleModel