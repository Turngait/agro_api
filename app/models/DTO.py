class DTO:
  _status = 100
  _message = ''
  _errorMessage = ''
  _data = None


  def _setStatus(self, status):
    self._status = status


  def _setMessage(self, message):
    self._message = message


  def setSuccess(self):
    self._setStatus(200)
    self._setMessage('Success')
  

  def setSuccessCreate(self):
    self._setStatus(204)
    self._setMessage('Success create')
  

  def setAccesDenied(self):
    self._setStatus(403)
    self._setMessage('Access denied')


  def setServerError(self):
    self._setStatus(503)
    self._setMessage('Server error')

  def setData(self, data):
    self._data = data


  def getResponce(self):
    return {
      'data': self._data,
      'status': self._status,
      'message': self._message,
      'error': self._errorMessage
    }

