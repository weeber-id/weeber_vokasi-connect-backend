import os
import uuid
from werkzeug.datastructures import FileStorage
from google.cloud import storage

from lib.environtment.gcs import BUCKET_NAME, PARENT_FILE_PATH

class ImageModel:
  def __init__(self, file:FileStorage):
    self.__file = file
    self.__data_bytes = file.read()

  @property
  def extension(self) -> str:
    return self.__file.filename.split(".")[-1]

  def upload_publicly(self, folder_name:str) -> str:
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    
    full_path = os.path.join(
      PARENT_FILE_PATH, 
      folder_name, 
      str(uuid.uuid4().hex) + "." + self.extension)

    blob = bucket.blob(full_path)
    blob.upload_from_string(
      self.__data_bytes, 
      content_type="image/"+self.extension)
    
    blob.make_public()
    return blob.public_url