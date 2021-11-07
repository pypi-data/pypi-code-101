

import sqlite3 as sl



def init_db():

    global con
    con = sl.connect('test-db.db')

    con.row_factory = sl.Row
    global c 
    c = con.cursor()


    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS OBSERVATIONS (
                observation_id TEXT PRIMARY KEY,
                record_type TEXT,
                record_id TEXT,
                key INTEGER,
                value TEXT,
                credibility FLOAT,
                date DATE,
                datasource TEXT
            );
        """)

    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS ENTITIES (
                entity_id TEXT PRIMARY KEY,
                record_type TEXT,
                record_id TEXT,
                created DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated DATETIME
            );
        """)
    
    return True



def get(record_type, record_id = None, **kwargs): 
    """Read an entity from file

    if kwarg, start by searching for condition, retrieving record_ids, then searching again for all record_ids.
    """

    init_db()


    # if record_id and kwargs, return observations
    if record_id and kwargs:
        records = search_observations(record_type, record_id, **kwargs)
        return records
        
    # if not record_id and if kwargs, search record_ids first, then retrieve all records
    if not record_id and kwargs:
        records = search_observations(record_type, record_id, **kwargs)
        record_ids = _get_record_ids(records)

        records = search_observations(record_type, record_ids)

        return records

    # if only record_type:
    if record_type and not record_id and not kwargs:

        # Get entities from entity table first:
        entities = search_entities(record_type, record_id, **kwargs)
        record_ids = _get_record_ids(entities)

        records = search_observations(record_type, record_ids)

        return records



    if not record_type and not record_id and not kwargs:
    # return list of schema families

        return get_types()


    return 



def get_types():
    """Return list of schemas
    """

    init_db()

    query = 'SELECT DISTINCT record_type FROM ENTITIES '  

    c.execute(query)

    result = [dict(row) for row in c.fetchall()]

    print(result)



    return result

def search_observations(record_type, record_id, **kwargs):
    """Search records matching kwargs
    """

    limit = kwargs.get('limit', None)
    offset = kwargs.get('offset', None)


    search_items = []

    # Build where sql statement
    if record_type:
        search_items.append('record_type = "{record_type}" '.format(record_type = record_type))

    if record_id:

        if isinstance(record_id, list) and not isinstance(record_id, str):

            list_ids = []
            for i in record_id:
                if i:
                    list_ids.append('"{i}"'.format(i=i))

            list_ids2 = ','.join(list_ids)

            search_items.append('record_id in ({record_ids}) '.format(record_ids = list_ids2))
        else:
            search_items.append('record_id = "{record_id}" '.format(record_id = record_id))

    if kwargs:

        comp = '='

        for key, value in kwargs:
            if key not in ['limit', 'offset']:
                search_items.append('{key} {comp} "{value}"'.format(key = key, comp = comp, value = value))
                
    # Finalize sql stateent and run
    query = 'SELECT * FROM OBSERVATIONS WHERE '  

    if search_items:
        query += ' AND '.join(search_items) 

    if limit:
        query += ' LIMIT {limit}'.format(limit=limit)

    if offset:
        query += ' OFFSET {offset}'.format(offset=offset)

    query += ' ORDER BY record_id ASC, observation_id ASC'


    c.execute(query)
    records = [dict(row) for row in c.fetchall()]



    """

    data = con.execute(query)


    records = _db_to_observations(data)

    """

    return records



def search_entities(record_type, record_id, **kwargs):
    """Search records matching kwargs
    """

    limit = kwargs.get('limit', None)
    offset = kwargs.get('offset', None)


    search_items = []

    # Build where sql statement
    if record_type:
        search_items.append('record_type = "{record_type}" '.format(record_type = record_type))

    if record_id:

        if isinstance(record_id, list):
            record_ids = str(tuple(record_id))
            search_items.append('record_id in "{record_ids}" '.format(record_ids = record_ids))
        else:
            search_items.append('record_id = "{record_id}" '.format(record_id = record_id))
                

    # Finalize sql statement and run
    query = 'SELECT * FROM ENTITIES WHERE ' 

    if search_items:
        query += ' AND '.join(search_items) 

    if limit:
        query += ' LIMIT {limit}'.format(limit=limit)

    if offset:
        query += ' OFFSET {offset}'.format(offset=offset)

    query += ' ORDER BY updated DESC'


    c.execute(query)
    records = [dict(row) for row in c.fetchall()]

    """
    data = con.execute(query)

    records = _db_to_entities(data)
    """

    return records





def post(records):
    """Save an entity to file
    """

    init_db()

    if not isinstance(records, list):
        records = [records]

    # Post observation
    sql = 'INSERT OR IGNORE INTO OBSERVATIONS (observation_id, record_type, record_id, key, value, credibility, date, datasource) values(?, ?, ?, ?, ?, ?, ?, ?)'

    datapoints = _observations_to_db(records)

    with con:
        con.executemany(sql, datapoints)

    # Post entity
    sql = ''
    for record in records:
        record_type = record.get('record_type', '')
        record_id = record.get('record_id', '')
        entity_id = record_type + '_' + record_id
        
        if not record_type or not record_id:
            continue
        

        sql += 'INSERT OR IGNORE INTO ENTITIES (entity_id, record_type, record_id, updated) values("{entity_id}", "{record_type}", "{record_id}", CURRENT_TIMESTAMP);'.format(entity_id = entity_id, record_type=record_type, record_id = record_id)

        sql += ' UPDATE ENTITIES SET updated = CURRENT_TIMESTAMP WHERE entity_id = "{entity_id}";'.format(entity_id = entity_id)


    #datapoints = _entities_to_db(records)


    c.executescript(sql)
    
    """
    with con:
        con.executescript(sql)
        #con.execute(sql)
    """

    return True

    
def _db_to_entities(data):
    
    records = []
    for d in data:

        record = {}
        record['entity_id'], record['record_type'],record['record_id'], record['created'], record['updated'] = d

        records.append(record)

    return records


def _entities_to_db(records):

    """Transforms records into list of tuple
    """

    datapoints = []

    for record in records:

        record_type = record.get('record_type', '')
        record_id = record.get('record_id', '')
        entity_id = record_type + '/' + record_id

        datapoint = (
            entity_id,
            record_type,
            record_id
        )
        datapoints.append(datapoint)
    
    return datapoints


def _db_to_observations(data):
    """Transforms db query result into records
    """

    records = []
    for d in data:

        record = {}
        record['observation_id'], record['record_type'],record['record_id'],record['key'],record['value'],record['credibility'],record['date'],record['datasource'] = d

        records.append(record)

    return records


def _observations_to_db(records):
    """Transforms records into list of tuple
    """

    datapoints = []

    for record in records:
        datapoint = (
            record.get('observation_id', None),
            record.get('record_type', None),
            record.get('record_id', None),
            record.get('key', None),
            record.get('value', None),
            record.get('credibility', None),
            record.get('date', None),
            record.get('datasource', None)
        )
        datapoints.append(datapoint)
    
    return datapoints


def _get_record_ids(records):
    """Given records, returns record_ids in a list
    """

    record_ids = []
    for record in records:
        record_id = record.get('record_id', None)
        record_ids.append(record_id)

    return record_ids