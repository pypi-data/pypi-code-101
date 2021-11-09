from .elasticsearch import Elasticsearch


def inspect(index_name, auto_create=True, mappings=None):
    def _inspect(func):
        def wrapper(*args):

            _es = Elasticsearch().connection

            # index exists check
            if not _es.indices.exists(index=index_name):
                if auto_create:
                    if mappings is not None:
                        res = _es.indices.create(index=index_name,
                                                 body=mappings)
                    else:
                        res = _es.indices.create(index=index_name)

                    if not res["acknowledged"]:
                        raise f'Could not create "{index_name}" index.'

                else:
                    raise f'Could not found "{index_name}" index.'

            func(*args)

        return wrapper

    return _inspect

# EOF
