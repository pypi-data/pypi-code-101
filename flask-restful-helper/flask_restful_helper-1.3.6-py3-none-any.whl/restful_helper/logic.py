from flask_restful.utils import http_status_message

from flask_restful_helper.restful_helper.db_helper import DBHelper

db_helper = DBHelper()


class Logic(object):
    """
    Remember to call super() function in __init__ when inheriting this class.
    """
    _manager = None
    _schema = None

    def __init__(self):
        self.error_messages = {}
        if self._schema is not None:
            self.schema = self._schema()
        if self._manager is not None:
            self.manager = self._manager()

    def list(self, query_args, *args, **kwargs):

        page = query_args.pop('page')
        results_per_page = query_args.pop('results_per_page')
        sort = query_args.pop('sort', 'id:asc')
        data = self.manager.list(page=page, results_per_page=results_per_page, sort=sort, **query_args)
        return_obj = {
            'data': self.schema.dump(data, many=True) if data else [],
            'total': self.manager.count(),
            'sort': sort,
            'size': len(data)
        }
        return return_obj, 200

    def retrieve(self, pk, *args, **kwargs):

        data = self.manager.retrieve(pk=pk)
        if data is None:
            return {'message': http_status_message(404)}, 404
        return {'data': self.schema.dump(data)}, 200

    def create(self, data, query_args, *args, **kwargs):
        with db_helper.auto_commit():
            data = self.validate(data)
            data = self.manager.create(data)
        return {'data': self.schema.dump(data)}, 201

    def update(self, pk, data, partial=False, *args, **kwargs):

        with db_helper.auto_commit():
            data = self.validate(data, partial=partial)
            data = self.manager.update(pk, data)
        return {'data': self.schema.dump(data)}, 200

    def delete(self, pk, *args, **kwargs):
        with db_helper.auto_commit():
            self.manager.delete(targets=pk)

        return None, 204

    def validate(self, data, schema=None, *args, **kwargs):

        if schema is None:
            data = self.schema.load(data, partial=kwargs.get('partial', False))
        else:
            data = schema().load(data, partial=kwargs.get('partial', False))

        return data
