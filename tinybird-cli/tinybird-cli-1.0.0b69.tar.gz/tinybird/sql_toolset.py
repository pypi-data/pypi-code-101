from chtoolset import query as chquery
from collections import defaultdict
from toposort import toposort


def format_where_for_mutation_command(where_clause):
    """
    >>> format_where_for_mutation_command("numnights = 99")
    'DELETE WHERE numnights = 99'
    >>> format_where_for_mutation_command("\\nnumnights = 99")
    'DELETE WHERE numnights = 99'
    >>> format_where_for_mutation_command("reservationid = 'foo'")
    "DELETE WHERE reservationid = \\\\'foo\\\\'"
    >>> format_where_for_mutation_command("reservationid = '''foo'")
    "DELETE WHERE reservationid = \\\\'\\\\\\\\\\\\'foo\\\\'"
    >>> format_where_for_mutation_command("reservationid = '\\\\'foo'")
    "DELETE WHERE reservationid = \\\\'\\\\\\\\\\\\'foo\\\\'"
    """
    formatted_condition = chquery.format(f"""SELECT {where_clause}""").split('SELECT ')[1]
    formatted_condition = formatted_condition.replace("\\", "\\\\").replace("'", "''")
    quoted_condition = chquery.format(f"SELECT '{formatted_condition}'").split('SELECT ')[1]
    return f"DELETE WHERE {quoted_condition[1:-1]}"


def sql_get_used_tables(sql, raising=False, default_database=''):
    """
    >>> sql_get_used_tables("SELECT 1 FROM the_table")
    [('', 'the_table')]
    >>> sql_get_used_tables("SELECT 1 FROM the_database.the_table")
    [('the_database', 'the_table')]
    """
    try:
        return chquery.tables(sql, default_database=default_database)
    except ValueError as e:
        if raising:
            raise e
        return [(default_database, sql)]


class ReplacementsDict(dict):
    def __getitem__(self, key):
        v = super().__getitem__(key)
        if isinstance(v, tuple):
            k, r = v
            if callable(r):
                r = r()
                super().__setitem__(key, (k, r))
            return (k, r)
        if callable(v):
            v = v()
            super().__setitem__(key, v)
        return v


def _tables_or_sql(replacement):
    try:
        return set(chquery.tables(replacement[1], default_database=replacement[0]))
    except Exception as e:
        if replacement[1][0] == '(':
            raise e
        return set([replacement])


def _separate_as_tuple_if_contains_database_and_table(definition: str) -> str:
    if "." in definition:
        database_and_table_separated = definition.split(".")
        definition = (database_and_table_separated[0], database_and_table_separated[1])
    return definition


def replacements_to_tuples(replacements):
    parsed_replacements = {}
    for k, v in replacements.items():
        parsed_replacements[_separate_as_tuple_if_contains_database_and_table(k)] \
            = _separate_as_tuple_if_contains_database_and_table(v)
    return parsed_replacements


def replace_tables(sql, replacements, default_database=''):
    if not replacements:
        return chquery.format(sql)

    _replacements = ReplacementsDict()
    for k, r in replacements.items():
        rk = k if isinstance(k, tuple) else (default_database, k)
        _replacements[rk] = r if isinstance(r, tuple) else (default_database, r)

    deps = defaultdict(set)
    _tables = chquery.tables(sql, default_database=default_database)
    seen_tables = set()
    while _tables:
        table = _tables.pop()
        seen_tables.add(table)
        if table in _replacements:
            replacement = _replacements[table]
            dependent_tables = _tables_or_sql(replacement)
            deps[table] |= dependent_tables
            for dependent_table in list(dependent_tables):
                if dependent_table not in seen_tables:
                    _tables.append(dependent_table)
    deps_sorted = list(reversed(list(toposort(deps))))

    if not deps_sorted:
        return chquery.format(sql)

    for current_deps in deps_sorted:
        current_replacements = {}
        for r in current_deps:
            if r in _replacements:
                replacement = _replacements[r]
                current_replacements[r] = replacement
                dt = chquery.table_if_is_simple_query(replacement[1], default_database=replacement[0])
                if dt:
                    current_replacements[r] = dt
        if current_replacements:
            sql = chquery.replace_tables(sql, current_replacements, default_database=default_database)
    return sql


if __name__ == '__main__':
    print(replace_tables("select joinGet('abcd', 'test', 1)", {'abcd': 'testing'}))
