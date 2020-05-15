from marshmallow import ValidationError

from lib.format import message
from lib.connector import db

class CRUD:
  def __init__(self, Model, Schema):
    self.Model = Model
    self.Schema = Schema


  def find_all(self, exception:bool=False, dump:bool=False):
    rows = self.Model.query.all()
    if exception:
      if rows is None:
        raise Exception(message.DATA_NOT_FOUND, 404)
    
    if dump:
      return [self.Schema.dump(row) for row in rows]
    return rows


  def find_by_id(self, ID, exception:bool=False, dump:bool=False):
    row = self.Model.query.filter_by(id=ID).first()
    if exception:
      if row is None:
        raise Exception(message.DATA_NOT_FOUND, 404)

    if dump:
      return self.Schema.dump(row)
    return row


  def read_all(self):
    rows = self.find_all(dump=True)
    return {
      "message": message.OK,
      "data": rows
    }, 200


  def read_by_id(self, ID):
    row = self.find_by_id(ID, exception=True, dump=True)
    return {
      "message": message.OK,
      "data": row}, 200


  @staticmethod
  def commit():
    try:
      db.session.commit()
      return {"message": message.SAVE_DATABASE_SUCCESS}, 201
    except:
      raise Exception(message.SAVE_DATABASE_ERROR, 400)


  def create(self, params:dict):
    try:
      row = self.Schema.load(params)
    except ValidationError as e:
      raise Exception(e.messages, 400)

    db.session.add(row)
    return self.commit()


  @classmethod
  def create_from_model(cls, Model):
    db.session.add(Model)
    return cls.commit()


  def update_by_id(self, ID, params:dict):
    row = self.find_by_id(ID, exception=True)

    for key, value in params.items():
      setattr(row, key, value)
    return self.commit()


  @classmethod
  def update_from_model(cls, Model, params:dict):
    for key, value in params.items():
      setattr(Model, key, value)
    return cls.commit()


  def delete_by_id(self, ID):
    row = self.find_by_id(ID, exception=True)
    db.session.delete(row)
    return self.commit()