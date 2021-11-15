import os
import json

def convert_forbidden_expression(request):
    form = request.form

    json_forbiden_expression = form['forbiddenExpressions'] if 'forbiddenExpressions' in form else "[]"
    
    forbidden_expressions = json.loads(json_forbiden_expression)
    return forbidden_expressions

def convertFormOrJsonRequestToDict(request):

    if request.is_json:
        return request.get_json()

    return request.form

def build_data_files(request):
    
    data_files = []

    for data in request.files.values():
        data_files.append(data)

    return data_files



def launch_flask(app, port):

    debug = os.getenv('debug_runner', False)

    app.run(debug=debug, host='0.0.0.0', port=port)