# -*- coding: utf-8 -*-

from django.db import models


def join_rhs(self, oref, compiler, connection):
  ''' Vrt. django.models.sql.datastructures.Join.as_sql '''
  join_conditions = []
  params = []
  qn = compiler.quote_name_unless_alias
  qn2 = connection.ops.quote_name

  # Add a join condition for each pair of joining columns.
  for lhs_col, rhs_col in self.join_cols:
    print(oref)
    join_conditions.append('%s.%s = %s.%s' % (
      qn(self.parent_alias),
      qn2(lhs_col),
      qn(self.table_alias),
      qn2(rhs_col),
    ))

  # Add a single condition inside parentheses for whatever
  # get_extra_restriction() returns.
  extra_cond = self.join_field.get_extra_restriction(
    compiler.query.where_class, self.table_alias, self.parent_alias)
  if extra_cond:
    extra_sql, extra_params = compiler.compile(extra_cond)
    join_conditions.append('(%s)' % extra_sql)
    params.extend(extra_params)
  if self.filtered_relation:
    extra_sql, extra_params = compiler.compile(self.filtered_relation)
    if extra_sql:
      join_conditions.append('(%s)' % extra_sql)
      params.extend(extra_params)
  if not join_conditions:
    # This might be a rel on the other end of an actual declared field.
    declared_field = getattr(self.join_field, 'field', self.join_field)
    raise ValueError(
      "Join generated an empty ON clause. %s did not yield either "
      "joining columns or extra restrictions." % declared_field.__class__
    )
  on_clause_sql = ' AND '.join(join_conditions)
  return '(%s)' % on_clause_sql, params
  # def join_rhs


def join_ehto(self, compiler, connection):
  pass


class Lumesarake(models.expressions.Col):
  '''
  Sarakeluokka, jonka arvo lasketaan kentälle määritetyn kyselyn mukaan.
  '''
  # pylint: disable=abstract-method

  def as_sql(self, compiler, connection):
    ''' Muodosta SELECT-lauseke ja siihen liittyvät SQL-parametrit. '''
    # pylint: disable=unused-argument
    join = compiler.query.alias_map.get(self.alias)
    if isinstance(join, models.sql.datastructures.Join):
      # Liitostaulu: muodosta alikysely tähän tauluun,
      # rajaa kysytty rivi liitostaulun primääriavaimen mukaan.
      #print(join.__dict__)
      #print(join.as_sql(compiler, connection))
      #print(join_rhs(join, compiler, connection))
      return compiler.compile(
        models.Subquery(
          self.target.model.objects.filter(
            #models.expressions.RawSQL(
            #  *join_rhs(join, compiler, connection),
            #  output_field=models.BooleanField()
            #),
            pk=models.expressions.RawSQL(
              #*join_rhs(join, models.OuterRef('pk'), compiler, connection),
              '%s.%s' % (
                compiler.quote_name_unless_alias(join.table_alias),
                connection.ops.quote_name(self.target.model._meta.pk.attname),
              ), ()
            ),
          ).values(**{
            # Käytetään kentän nimestä poikkeavaa aliasta.
            f'_{self.target.name}_join': self.target.kysely,
          }),
          output_field=self.field,
        ).resolve_expression(query=compiler.query)
      )
      # if isinstance(join, Join)

    elif isinstance(join, models.sql.datastructures.BaseTable):
      # Kyselyn aloitustaulu: suora kysely.
      return compiler.compile(self.target.kysely.resolve_expression(
        query=compiler.query
      ))
      # elif isinstance (join, BaseTable)

    elif join is None:
      raise NotImplementedError(f'{join!r} is None')

    else:
      # Muita kyselytyyppejä ei tueta.
      raise NotImplementedError(
        f'not isinstance({join!r}, (BaseTable, Join))'
      )
    # def as_sql

  # class Lumesarake
