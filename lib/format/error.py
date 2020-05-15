from lib.format import message


def CustomExceptionResponse(e):
  try:
    error = e.args[0]
    code = e.args[1]
    return {
      "message": error,
      "code": code }, code

  except:
    return {
      "message": message.SERVER_ERROR,
      "code": 500,
      "error": str(e)}, 500