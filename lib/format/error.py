from lib.format import message

def CustomExceptionResponse(e):
  return {
    "message": message.SERVER_ERROR,
    "error": str(e)
    }, 500