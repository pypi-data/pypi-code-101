import json
 



def jsonConvert(data):
    """Método para refrescar el formato JSON de un diccionario

    Args:
        data (dict): Valor a retornar

    Returns:
        json: Diccionario con formato JSON
    """  
    return json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))


def ErrorResponse(e):
    """Método para retornar un error dentro diccionario con estado OK en la capa Fachade 

    Args:
        e (any): error a retornar

    Returns:
        res: Diccionario con estado OK enmascarando el error
    """  
    if isinstance(e, ValueError): 
        
        return {'data': None, 'state': False, 'code': 400, 'message': e.args[0]}
    if isinstance(e, TypeError):
        return {'data': None, 'state': False, 'code': 500, 'message': e.args[0]}
    if isinstance(e, dict):
        return e
    print(str(e))
    error = eval(str(e))
    data = {'data': None, 'state': False,
            'code': error[0], 'message': error[1]}
    res = jsonConvert(data)
    return res


def Ok(e):
    """Método para retornar un diccionario con estado OK en la capa Fachade 

    Args:
        e (any): Valor a retornar

    Returns:
        res: Diccionario con estado OK
    """    
    if isinstance(e, dict):
        return {'data': e, 'state': True, 'code': None, 'message': None}
    if isinstance(e, list):
        l = []
        for i in e:
            l.append(json.loads(i))
        return {'data': l, 'state': True, 'code': None, 'message': None}
    data = e
    data = {'data': data, 'state': True, 'code': None, 'message': None}
    res = jsonConvert(data)
    return res


def getValue(input, key):
    """Método para obtener el valor 
    de un diccionario especial de 2 niveles 
    donde input tiene un atributo llamado data

    Args:
        input (dict): Diccionario
        key (str): Llave del diccionario

    Returns:
        any: Valor de la llave
    """    
    data = input.get('data')
    if isinstance(data, dict):
        if key in data:
            return data[key]
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    pass
