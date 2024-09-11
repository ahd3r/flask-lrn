import os
from flask import request, jsonify
from flask_migrate import upgrade

from db.db import app, logger
import router.user
import router.task
from util.errors import InternalError

@app.route('/check', methods=["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"])
def check():
    query = f"?{request.query_string.decode()}" if request.query_string.decode() != '' else ''
    if request.get_data().decode() != '' and request.headers.get('Content-Type') == 'application/json':
        logger.info(request.get_json())
    return jsonify({
        "data": {
            "method": request.method,
            "body": request.get_data().decode(),
            "url": f"{request.path}{query}",
            "header": str(request.headers)
        }
    }), 200

@app.route('/')
def healthcheck():
    return jsonify({"data": "Working!"}), 200

@app.before_request
def logging_request():
    query = f"?{request.query_string.decode()}" if request.query_string.decode() != '' else ''
    logger.info({
        "type": "request",
        "method": request.method,
        "body": request.get_data().decode(),
        "url": f"{request.path}{query}",
        "header": str(request.headers)
    })

@app.after_request
def logging_response(response):
    query = f"?{request.query_string.decode()}" if request.query_string.decode() != '' else ''
    logger.info({
        "type": "response",
        "status": response.status_code,
        "method": request.method,
        "response": response.data.decode(),
        "url": f"{request.path}{query}",
        "header": str(request.headers)
    })
    return response

@app.errorhandler(Exception)
def handler(error):
    if not hasattr(error, "status"):
        if hasattr(error.args, '__len__') and len(error.args) == 1:
            error = InternalError(error.args[0])
        else:
            error = InternalError(error.args)
    logger.error({
        "error": error.message,
        "type": error.type_error,
        "status": error.status
    })
    return jsonify({
        "error": error.message,
        "type": error.type_error,
        "status": error.status
    }), error.status

if __name__ == '__main__':
    with app.app_context():
        upgrade()
    app.run()
