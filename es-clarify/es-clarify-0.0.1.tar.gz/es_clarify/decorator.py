def clarify(es, index_name, auto_create=True, mappings=None):
    def _clarify(func):
        def wrapper(*args):

            # index exists check
            if not es.indices.exists(index=index_name):
                if auto_create:
                    if mappings is not None:
                        res = es.indices.create(index=index_name,
                                                body=mappings)
                    else:
                        res = es.indices.create(index=index_name)

                    if not res["acknowledged"]:
                        raise f'Could not create "{index_name}" index.'

                else:
                    raise f'Could not found "{index_name}" index.'

            return func(*args)

        return wrapper

    return _clarify

# EOF
