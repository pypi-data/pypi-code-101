from typing import Union, List, Tuple, Dict

class Base:

    def field2sql(self, field:str):
        ''' 字段名解析
        情况：'id','a.id','id as i', 'a.id as ai'
        '''
        # return '%s' % field.strip().replace('.', '.').replace(' as ', ' as ')
        return field
    
    def fields2sql(self, fields:Union[str, List[str], Tuple[str]]):
        ''' 解析fields
        情况： 'id, a.name, imlf.phone as ip', 
               ['id', 'a.name', 'imlf.phone as ip'], 
               ('id', 'a.name', 'imlf.phone as ip')
        '''
        # if isinstance(fields, str):
        #     fields = fields.strip()
        #     if fields == '*':
        #         return fields
        #     fields = fields.split(',')
        # return ','.join([self.field2sql(field) for field in fields])
        if isinstance(fields, str):
            return fields
        else: 
            return ','.join(list(fields))


    def table2sql(self, table:str):
        ''' 字段名解析
        情况：'graphs','imlf.graphs','graphs as g', 'imlf.graphs as ig'
        '''
        return '%s' % table.strip().replace('.', '.').replace(' as ', ' as ')
    
    def tables2sql(self, tables:Union[str, List[str], Tuple[str]]):
        ''' 解析tables
        情况： 'graphs, imlf.nodes, imlf.graphs as ig', 
               ['graphs', 'imlf.nodes', 'imlf.graphs as ig'], 
               ('graphs', 'imlf.nodes', 'imlf.graphs as ig')
        '''
        if isinstance(tables, str):
            tables = tables.split(',')
        return ','.join([self.table2sql(table) for table in tables])
    
    def key2sql(self, k:str) -> str:
        ''' where中的key转sql语句
        情况：'name', 'a.name'
        '''
        return '%s' % k.strip().replace('.', '.')

    def value2sql(self, v):
        ''' where中value为非tuple时
        情况: 'value', 'value "name"'
        '''
        if isinstance(v, str):
            return "'%s'" % self._dbo.escape(v)
        elif isinstance(v, (int, float)):
            return str(v)
        elif v == None:
            return 'NULL'
        else:
            return "'%s'" % str(v)

    def append_where_args(self, v):
        ''' 添加where_args值 '''
        self._where_args.append(v)
        return "%s"

    def append_values_args(self, v):
        ''' 添加values_args的值 '''
        self._values_args.append(v)
        return "%s"

    def where_value_tuple2sql(self, v:tuple) -> str:
        ''' where中value为tuple时
        情况：('in', ['12', 1])
              ('not in', ['12', 1])
              ('between', ['time1', 'time2'])
              ('like', '%time1%')
              ('like', 'time1%')
        '''
        assert len(v) == 2
        op, item = v
        assert isinstance(op, str)
        op = op.strip()
        if op.endswith('in'):
            assert isinstance(item, (list, tuple))
            self._where_args.append(item)
            return op + ' %s'
        elif op == 'between':
            assert isinstance(item, (list, tuple)) and len(item) == 2
            self._where_args.append(item[0])
            self._where_args.append(item[1])
            return op + ' %s and %s'
        else:
            assert isinstance(item, str)
            self._where_args.append(item)
            return op + ' %s'

    def where2sql(self, where:dict):
        '''where值解析'''
        kv = lambda k,v: self.key2sql(k)+' '+self.where_value_tuple2sql(v) \
            if isinstance(v, tuple) else self.key2sql(k)+'='+self.append_where_args(v)
        return ' and '.join([kv(k, v) for k, v in where.items()])

    def on2sql(self, where:Dict[str, str]):
        '''where值解析'''
        kv = lambda k,v: self.key2sql(k)+'='+self.key2sql(v)
        return ' and '.join([kv(k, v) for k, v in where.items()])

    def values2sql(self, values:dict):
        '''values值解析'''
        kv = lambda k, v:self.key2sql(k)+'='+self.append_values_args(v)
        return ','.join([kv(k, v) for k, v in values.items()])

    def other2sql(self, other:Union[tuple, str]):
        if isinstance(other, str):
            return other
        else:
            assert len(other) == 2
            op, item = other
            assert isinstance(op, str)
            op = op.strip()
            if op.endswith('limit'):
                if isinstance(item, int):
                    return op + ' %s' % item
                else:
                    assert isinstance(item, (list, tuple, set)) and len(item) == 2
                    return op+' %s,%s' % (tuple(item))
            elif op == 'order by':
                if isinstance(item, str):
                    return op+' %s' % self.key2sql(item)
                else:
                    assert isinstance(item, (list, tuple, set)) and len(item) == 2
                    assert item[-1] in ['asc', 'desc']
                    return op+ ' %s %s' % (self.key2sql(item[0]), item[1])
            elif op == 'group by':
                if isinstance(item, str):
                    return op+' %s' % self.key2sql(item)
                else:
                    assert isinstance(item, (list, tuple, set))
                    return op+' %s' % ','.join([self.key2sql(i) for i in item])
            elif op == 'sql':
                assert isinstance(item, str)
                return item
    
    def values2insert(self, values:dict) -> str:
        '''insert中的values转sql'''
        keys = list(values.keys())
        return '(%s) values (%s)' % (
            ','.join([self.key2sql(k) for k in keys]), 
            ','.join([self.append_values_args(values[k]) for k in keys])
        )

    def valueslist2insert(self, values_list:List[dict]) -> str:
        '''批量insert转sql'''
        keys = list(values_list[0].keys())
        return '(%s) values (%s)' % (
            ','.join([self.key2sql(k) for k in keys]),
            '),('.join(
                [','.join([self.append_values_args(values[k]) for k in keys]) for values in values_list]
            )
        )
        
class WhereMixin:
    def where(self, **kwargs):
        self._where = kwargs
        return self

class ValuesMixin:
    def values(self, **kwargs):
        self._values = kwargs
        return self

class OtherMixin:
    def other(self, other):
        self._other = other
        return self


class SelectHelper(Base, WhereMixin, OtherMixin):
    def __init__(
        self, 
        dbo,
        tables, 
        fields='*', 
        join_type='inner',
        join_table=None,
        on=None,
        where=None, 
        where_args=None,
        group_by=None, 
        order_by=None, 
        limit=None, 
        other=None):
        self._dbo = dbo
        self._tables = tables
        self._fields = fields
        self._join_type = join_type
        self._join_table = join_table
        self._on = on
        self._where = where
        self._where_args = where_args or list()
        self._group_by = group_by
        self._order_by = order_by
        self._limit = limit
        self._other = other


    def sql(self, fill_args=True):
        sql = "select %s from %s" % (
            self.fields2sql(self._fields), 
            self.tables2sql(self._tables)
        )
        if self._join_table and self._on:
            sql += " %s join %s on %s" % (
                self._join_type,
                self.table2sql(self._join_table),
                self.on2sql(self._on)
            )
        if self._where:
            sql += " where %s" % self.where2sql(self._where)
        if self._group_by:
            sql += " group by %s" % self.fields2sql(self._group_by)
        if self._order_by:
            sql += " order by %s" % self.fields2sql(self._order_by)
        if self._limit:
            sql += " limit %s" % self.fields2sql(self._limit)
        if self._other:
            sql += ' %s' % self.other2sql(self._other)
        if fill_args:
            return self._dbo.mogrify(sql, self._where_args)
        return sql

    def fields(self, *args):
        self._fields = args
        return self

    def join(self, table, on, join_type=None):
        assert isinstance(on, dict), "'on' must be dict"
        self._on = on
        self._join_table = table
        if join_type:
            self._join_type = join_type
        return self
    
    def left_join(self, table, on):
        return self.join(table, on, join_type='left')

    def right_join(self, table, on):
        return self.join(table, on, join_type='right')

    def group_by(self, *args):
        self._group_by = args
        return self

    def order_by(self, *args):
        assert len(args) <= 2, "'order_by' accept 1 or 2 parameters"
        self._order_by = args
        return self

    def limit(self, *args):
        assert len(args) <= 2, "'limit' accept 1 or 2 parameters"
        self._limit = (str(i) for i in args)
        return self

    def all(self, isdict=True):
        sql = self.sql(fill_args=False)
        return self._dbo.query(sql, self._where_args or None, isdict=isdict)

    def first(self, isdict=True):
        sql = self.sql(fill_args=False)
        if sql.find('limit') == -1:
            sql += ' limit 1'
        return self._dbo.get(sql, self._where_args or None, isdict=isdict)


class InsertHelper(Base, ValuesMixin, OtherMixin):
    def __init__(self, dbo, table, values=None, values_args=None, many=None, other=None):
        self._dbo = dbo
        self._table = table
        self._values = values
        self._values_args = values_args or list()
        self._many = many
        self._other = other
    
    def many(self, _dict_list):
        self._many = _dict_list
        return self

    def sql(self, fill_args=True):
        assert not (self._values and self._many), \
            "'values' and 'many' cannot exist at the same time"
        assert self._values or self._many, \
            "'values' or 'many' must be used"
        sql = 'insert into %s %s' % (
            self.table2sql(self._table), 
            self.values2insert(self._values) if self._values else self.valueslist2insert(self._many)
            )
        if self._other:
            sql += ' %s' % self.other2sql(self._other)
        if fill_args:
            return self._dbo.mogrify(sql, self._values_args)
        return sql
    
    def execute(self):
        sql = self.sql(fill_args=False)
        res = self._dbo.execute_insert(sql, self._values_args or None)
        return res
    
    def from_select(self):
        # TODO
        return self


class UpdateHelper(Base, WhereMixin, ValuesMixin, OtherMixin):
    def __init__(self, dbo, table, where=None, where_args=None, values=None, values_args=None, other=None):
        self._dbo = dbo
        self._table = table
        self._where = where
        self._where_args = where_args or list()
        self._values = values
        self._values_args = values_args or list()
        self._other = other
    
    def sql(self, fill_args=True):
        sql = 'update %s set %s' % (
            self.table2sql(self._table), 
            self.values2sql(self._values)
            )
        if self._where:
            sql += " where %s" % self.where2sql(self._where)
        if self._other:
            sql += ' %s' % self.other2sql(self._other)
        if fill_args:
            return self._dbo.mogrify(sql, self._values_args)
        return sql

    def execute(self):
        sql = self.sql(fill_args=False)
        args = self._values_args + self._where_args
        self._dbo.execute(sql, args or None)

class DeleteHelper(Base, WhereMixin, OtherMixin):
    def __init__(self, dbo, table, where=None, where_args=None, other=None):
        self._dbo = dbo
        self._table = table
        self._where = where
        self._where_args = where_args or list()
        self._other= other

    def sql(self, fill_args=True):
        sql = 'delete from %s' % self.table2sql(self._table)
        if self._where:
            sql += " where %s" % self.where2sql(self._where)
        if self._other:
            sql += ' %s' % self.other2sql(self._other)
        if fill_args:
            return self._dbo.mogrify(sql, self._values_args)
        return sql

    def execute(self):
        sql = self.sql(fill_args=False)
        self._dbo.execute(sql, self._where_args or None)
