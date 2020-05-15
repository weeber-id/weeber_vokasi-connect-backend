from flask import request
from flask_restful import Resource

from lib.format import message, error
from lib.model.file import ImageModel

class ImageGCS(Resource):
  def post(self):
    try:
      file = request.files["image"]
      folder_name = request.form.get("folder_name")

      if folder_name is None:
        raise Exception("component cannot be blank", 400)

      image = ImageModel(file)
      url = image.upload_publicly(folder_name=folder_name)
      return {
        "message": message.OK,
        "url": url}, 200
      
    except Exception as e:
      error.CustomExceptionResponse(e)