from sqlalchemy import desc
from marshmallow import ValidationError

from lib.format import message
from lib.connector import db

class CRUD:
  def __init__(self, Model, Schema):
    self.Model = Model
    self.Schema = Schema


  def find(self, filter:dict, many=False, reverse_id=False, exception:bool=False, dump:bool=False):
    if many:
      if reverse_id:
        row = self.Model.query.filter_by(**filter).order_by(desc(self.Model.id))
      else:
        row = self.Model.query.filter_by(**filter)
    
    else:
      row = self.Model.query.filter_by(**filter).first()


    if exception:
      if row is None:
        raise Exception(message.DATA_NOT_FOUND, 404)

    if dump:
      if many:
        return [self.Schema.dump(item) for item in row]
      else:
        return self.Schema.dump(row)
    return row


  def find_all(self, reverse_id:bool=False, exception:bool=False, dump:bool=False):
    if reverse_id:
      rows = self.Model.query.order_by(desc(self.Model.id)).all()
    else:
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


  def read_all(self, reverse_id=False):
    rows = self.find_all(reverse_id=reverse_id, dump=True)
    return {
      "message": message.OK,
      "data": rows
    }, 200


  def read_by_id(self, ID):
    row = self.find_by_id(ID, exception=True, dump=True)
    return {
      "message": message.OK,
      "data": row}, 200


  def read(self, filter:dict, many=False, reverse_id=False):
    row = self.find(filter, many=many, exception=False, dump=True, reverse_id=reverse_id)
    return {
      "message": message.OK,
      "data": row}, 200


  @staticmethod
  def commit(headers:list=None):
    try:
      db.session.commit()
      if headers:
        return {"message": message.SAVE_DATABASE_SUCCESS}, 201, headers
      return {"message": message.SAVE_DATABASE_SUCCESS}, 201
    except Exception as e:
      raise Exception(str(e), 400)


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