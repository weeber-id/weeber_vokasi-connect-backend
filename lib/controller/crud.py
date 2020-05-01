from marshmallow import ValidationError

from lib.format import message


class CRUD:
  def __init__(self, Model, Schema):
    self.Model = Model
    self.Schema = Schema


  def read_all(self):
    rows = self.Model.get_all_from_db()
    return {
      "message": message.OK,
      "data": [self.Schema.dump(row) for row in rows]
    }, 200


  def read_by_id(self, ID):
    row = self.Model.find_by_id(ID)
    if row is None:
      return { "message": message.DATA_NOT_FOUND}, 404

    return {
      "message": message.OK,
      "data": self.Schema.dump(row)}, 200
    

  def create(self, params:dict):
    try:
      row = self.Schema.load(params)
    except ValidationError as e:
      return {"message": e.messages}, 400

    try:
      row.save_to_db()
      return {"message": message.SAVE_DATABASE_SUCCESS}, 201
    except:
      return {"message": message.SAVE_DATABASE_ERROR}, 400


  def update_by_id(self, ID, params:dict):
    if ID is None:
      return {"message": "id cannot be blank"}, 400

    row = self.Model.find_by_id(ID)
    if row is None:
      return {"message": message.DATA_NOT_FOUND}, 404

    try:
      row.update_to_db(params)
      return {"message": message.SAVE_DATABASE_SUCCESS}, 201
    except:
      return {"message": message.SAVE_DATABASE_ERROR}, 400


  def delete_by_id(self, ID):
    if ID is None:
      return {"message": "id cannot be blank"}, 400

    row = self.Model.find_by_id(ID)
    if row is None:
      return {"message": message.DATA_NOT_FOUND}, 404

    row.delete_from_db()
    return {"message": message.DELETE_DATABASE_SUCCESS}, 200