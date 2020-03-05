from flask import Flask
import service_converter
from utils.responses import JSONResponse

app = Flask(__name__)

@app.route('/yard_to_meter/<yard>')
def yard_to_meter(yard):
    try:
        value = service_converter.yard_to_meter(yard)
        response = JSONResponse(200, 'Converted successfully', value)
    except AssertionError as err:
        response = JSONResponse(400, str(err), False)
        return str(response), 400
    return str(response), 200

@app.route('/meter_to_yard/<meter>')
def meter_to_yard(meter):
    return service_converter.meter_to_yard(meter)


if __name__ == '__main__':
    app.run(host='0.0.0.0')