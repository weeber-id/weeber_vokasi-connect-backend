from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
import jwt
import hashlib
import datetime

from lib.controller.crud import CRUD
from lib.format.error import CustomExceptionResponse
from lib.environtment.address import JWT_SECRET_KEY
from lib.model.user import UserAdminModel, UserAdminSchema

useradmin_schema = UserAdminSchema()

crud_useradmin = CRUD(UserAdminModel, useradmin_schema)

class LoginAdmin(Resource):
  def post(self):
    try:
      inpt = request.form
      user = crud_useradmin.find({"username": inpt["username"]}, exception=True)

      pass_encrypt = hashlib.md5(inpt["password"].encode()).hexdigest()

      if user.password != pass_encrypt:
        raise Exception("Invalid credential", 400)

      access_token = create_access_token(identity=user.username, expires_delta=datetime.timedelta(days=1))
      return {"message": "Login success", "access_token": access_token}, 200

    except Exception as e:
      return CustomExceptionResponse(e)


# class LogoutAdmin(Resource):
#   def get(self):
#     try:
#       headers = [
#         ("Set-Cookie", "access_token_cookie=''; Path=/; Max-Age=1")
#       ]
#       return {"message": "Logout success"}, 200, headers
#     except Exception as e:
#       return CustomExceptionResponse(e)


class Admin(Resource):
  @jwt_required
  def get(self):
    try:
      return crud_useradmin.read_all()
    except Exception as e:
      return CustomExceptionResponse(e)

  @jwt_required
  def post(self):
    try:
      inpt = request.form

      admin = crud_useradmin.find({"username": get_jwt_identity()})
      if admin.role != 1:
        raise Exception("Only super administrator can access this", 400)

      if crud_useradmin.find({"username": inpt["username"]}):
        raise Exception("Username has been exists", 400)

      pass_encrypt = hashlib.md5("admin".encode()).hexdigest()

      return crud_useradmin.create({
        "username": inpt["username"],
        "password": pass_encrypt,
        "role": 2,
      })
    except Exception as e:
      return CustomExceptionResponse(e)


  @jwt_required
  def put(self):
    try:
      inpt = request.form

      admin = crud_useradmin.find({"username": get_jwt_identity()})
      
      old_pass_encrypt = hashlib.md5(inpt["old_password"].encode()).hexdigest()
      if old_pass_encrypt != admin.password:
        raise Exception("Wrong old password", 400)

      new_pass_encrypt = hashlib.md5(inpt["new_password"].encode()).hexdigest()
      admin.password = new_pass_encrypt
      return crud_useradmin.commit()
    except Exception as e:
      return CustomExceptionResponse(e)


  @jwt_required
  def delete(self):
    try:
      inpt = request.form

      admin = crud_useradmin.find({"username": get_jwt_identity()})
      if admin.role != 1:
        raise Exception("Only super administrator can access this", 400)

      user = crud_useradmin.find({"username": inpt["username"]}, exception=True)
      return crud_useradmin.delete_by_id(user.id)
    except Exception as e:
      return CustomExceptionResponse(e)