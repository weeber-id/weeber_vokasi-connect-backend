from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from lib.model.article import ArticleModel, ArticleSchema
from lib.format import message, date, error
from lib.controller.crud import CRUD

Schema = ArticleSchema()
article_crud = CRUD(ArticleModel, Schema)

class Articles(Resource):
  def get(self):
    try:
      return article_crud.read_all()

    except Exception as e:
      return error.CustomExceptionResponse(e)


class Article(Resource):
  def get(self):
    ID = request.args.get("id")

    try:
      return article_crud.read_by_id(ID)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def post(self):
    inpt = request.get_json()
    inpt["date_created"] = date.get_date_now()
    inpt["time_created"] = date.get_time_now()
    inpt["date_modified"] = date.get_date_now()
    inpt["time_modified"] = date.get_time_now()

    try:
      return article_crud.create(inpt)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def put(self):
    ID = request.args.get("id")
    inpt = request.get_json()
    inpt["date_modified"] = date.get_date_now()
    inpt["time_modified"] = date.get_time_now()

    try:
      return article_crud.update_by_id(ID, inpt)

    except Exception as e:
      return error.CustomExceptionResponse(e) 


  def delete(self):
    ID = request.args.get("id")

    try:
      return article_crud.delete_by_id(ID)
    
    except Exception as e: 
      return error.CustomExceptionResponse(e)