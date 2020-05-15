from typing import List
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, Integer, String, Date, Time, Text

from lib.connector import db, ma

class EventModel(db.Model):
  """
  +-------+--------------+------+-----+---------+----------------+
  | Field | Type         | Null | Key | Default | Extra          |
  +-------+--------------+------+-----+---------+----------------+
  | id    | int unsigned | NO   | PRI | NULL    | auto_increment |
  | title | varchar(255) | NO   |     | NULL    |                |
  | image | varchar(255) | YES  |     | NULL    |                |
  | url   | varchar(255) | YES  |     | NULL    |                |
  +-------+--------------+------+-----+---------+----------------+
  """
  __tablename__ = "event"

  id = Column(INTEGER(unsigned=True), primary_key=True)
  title = Column(String(255), nullable=False)
  image = Column(String(255))
  url = Column(String(255))


class EventSchema(ma.ModelSchema):
  class Meta:
    model = EventModel