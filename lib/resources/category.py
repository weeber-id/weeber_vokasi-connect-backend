from flask import request
from flask_restful import Resource

from lib.controller.crud import CRUD
from lib.format.error import CustomExceptionResponse
from lib.model.category import CategoryModel, CategorySchema

category_schema = CategorySchema()

crud_category = CRUD(CategoryModel, category_schema)


class Categories(Resource):
  def get(self):
    try:
      return crud_category.read_all()
    except Exception as e:
      return CustomExceptionResponse(e)


class Category(Resource):
  def get(self):
    ID = request.args.get("id")

    try:
      return crud_category.read_by_id(ID)
    except Exception as e:
      return CustomExceptionResponse(e)

  def post(self):
    inpt = request.get_json()

    try:
      return crud_category.create(inpt)
    except Exception as e:
      return CustomExceptionResponse(e)

  def put(self):
    ID = request.args.get("id")
    inpt = request.get_json()

    try:
      return crud_category.update_by_id(ID, inpt)
    except Exception as e:
      return CustomExceptionResponse(e)

  def delete(self):
    ID = request.args.get("id")

    try:
      return crud_category.delete_by_id(ID)
    except Exception as e:
      return CustomExceptionResponse(e)