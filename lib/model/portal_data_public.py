from typing import List
from sqlalchemy import Column, Integer, String, Date, Time, Text, ForeignKey
from sqlalchemy.orm import relationship

from lib.connector import db, ma

class PortalDataModel(db.Model):
  __tablename__ = "portal_data_public"

  id = Column(Integer, primary_key=True)
  title = Column(String(255), nullable=False)
  department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
  link = Column(String(255), nullable=False)
  
  department = relationship("DepartmentModel")

  @classmethod
  def find_by_id(cls, id) -> "PortalDataModel":
    return cls.query.filter_by(id=id).first()

  @classmethod
  def get_all_from_db(cls) -> List["PortalDataModel"]:
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


class PortalDataSchema(ma.ModelSchema):
  class Meta:
    model = PortalDataModel