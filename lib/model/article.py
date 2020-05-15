from typing import List
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import Column, Integer, String, Date, Time, Text

from lib.connector import db, ma

class ArticleModel(db.Model):
  """
  +---------------+--------------+------+-----+---------+----------------+
  | Field         | Type         | Null | Key | Default | Extra          |
  +---------------+--------------+------+-----+---------+----------------+
  | id            | int unsigned | NO   | PRI | NULL    | auto_increment |
  | title         | varchar(255) | NO   |     | NULL    |                |
  | author        | varchar(255) | NO   |     | NULL    |                |
  | date_created  | date         | NO   |     | NULL    |                |
  | time_created  | time         | NO   |     | NULL    |                |
  | date_modified | date         | NO   |     | NULL    |                |
  | time_modified | time         | NO   |     | NULL    |                |
  | content       | text         | NO   |     | NULL    |                |
  | thumbnail     | varchar(255) | YES  |     | NULL    |                |
  +---------------+--------------+------+-----+---------+----------------+
  """
  __tablename__ = "article"

  id = Column(INTEGER(unsigned=True), primary_key=True)
  title = Column(String(255), nullable=False)
  author = Column(String(255), nullable=False)
  date_created = Column(Date, nullable=False)
  time_created = Column(Time, nullable=False)
  date_modified = Column(Date, nullable=False)
  time_modified = Column(Time, nullable=False)
  content = Column(Text, nullable=False)
  thumbnail = Column(String(255))


class ArticleSchema(ma.ModelSchema):
  class Meta:
    model = ArticleModel