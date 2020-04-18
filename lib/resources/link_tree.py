from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from lib.model.link_tree import Link_tree_model, Link_tree_schema
from lib.format import message

schema = Link_tree_schema()

class Link_tree(Resource):
  def get(self):
    try:
      items = Link_tree_model.get_all_from_db()
      return {
        "message": message.OK,
        "data": [schema.dump(deal) for deal in items]}, 200
    except: 
      return {"message": message.SERVER_ERROR}, 500

  def post(self):
    inpt = request.get_json()

    try:
      try:
        item = schema.load(inpt)
      except ValidationError as err:
        return {"message": err.messages}, 400

      try:
        item.save_to_db()
        return {"message": message.SAVE_DATABASE_SUCCESS}, 201
      except:
        return {"message": message.SAVE_DATABASE_ERROR}, 400

    except: 
      return {"message": message.SERVER_ERROR}, 500

  def put(self):
    inpt = request.get_json()

    try:
      if "id" not in inpt.keys():
        return {"message": "id cannot be blank"}, 400

      item = Link_tree_model.find_by_id(inpt["id"])
      if item is None:
        return {"message": message.DATA_NOT_FOUND}, 404

      try:
        item.update_to_db(inpt)
        return {"message": message.SAVE_DATABASE_SUCCESS}, 201
      except:
        return {"message": message.SAVE_DATABASE_ERROR}, 400

    except: 
      return {"message": message.SERVER_ERROR}, 500

  def delete(self):
    ID = request.args.get("id")

    try:
      if ID is None:
        return {"message": "id cannot be blank"}, 400

      item = Link_tree_model.find_by_id(ID)
      if item is None:
        return {"message": message.DATA_NOT_FOUND}, 404

      item.delete_from_db()
      return {"message": message.DELETE_DATABASE_SUCCESS}, 200
    
    except: 
      return {"message": message.SERVER_ERROR}, 500