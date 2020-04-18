from typing import List

from lib.connector import db, ma

class Link_tree_model(db.Model):
  __tablename__ = "link_tree"

  id = db.Column(db.Integer, primary_key=True)
  link = db.Column(db.String(255), nullable=False)
  short_link = db.Column(db.String(255))

  @classmethod
  def find_by_id(cls, id) -> "Link_tree_model":
    return cls.query.filter_by(id=id).first()

  @classmethod
  def get_all_from_db(cls) -> List["Link_tree_model"]:
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


class Link_tree_schema(ma.ModelSchema):
  class Meta:
    model = Link_tree_model