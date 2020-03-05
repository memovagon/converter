import json

class JSONResponse():
    def __init__(self, status, message, data):
        self.success = status // 100 == 2
        self.message = message
        self.data = data

    def __str__(self):
        return json.dumps({"success": self.success, "message": self.message, "data": self.data})