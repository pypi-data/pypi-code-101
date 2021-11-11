"""Database main objects, functions and constants."""

from sys import exit as sys_exit
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy.exc import ProgrammingError, OperationalError
import zope.sqlalchemy

from ..lib.i18n import _, translate


DB_METADATA = MetaData(naming_convention={
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
})

ID_LEN = 32
NAME_LEN = 64
EMAIL_LEN = 64
LABEL_LEN = 128
DESCRIPTION_LEN = 255
VALUE_LEN = 255
MODULE_LEN = 128

DBDeclarativeClass = declarative_base(metadata=DB_METADATA)


# =============================================================================
def includeme(configurator):
    """Initialize the model for a Chrysalio application.

    :type configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    settings = configurator.get_settings()
    settings['tm.manager_hook'] = 'pyramid_tm.explicit_manager'

    # Use pyramid_tm to hook the transaction lifecycle to the request
    configurator.include('pyramid_tm')

    # Use pyramid_retry to retry a request when transient exceptions occur
    configurator.include('pyramid_retry')

    # Get database engine
    try:
        dbengine = get_dbengine(settings)
    except KeyError:
        sys_exit(translate(_('*** Database is not defined.')))
    DB_METADATA.bind = dbengine

    # Make request.dbsession available for use in Pyramid
    dbsession_factory = get_dbsession_factory(dbengine)
    configurator.registry['dbsession_factory'] = dbsession_factory
    configurator.add_request_method(
        # r.tm is the transaction manager used by pyramid_tm
        lambda r: get_tm_dbsession(dbsession_factory, r.tm),
        'dbsession', reify=True)


# =============================================================================
def get_dbengine(settings, prefix='sqlalchemy.'):
    """Get SQLAlchemy engine.

    :type  settings: pyramid.registry.Registry.settings
    :param settings:
        Application settings.
    :param str prefix: (default='sqlalchemy')
        Prefix in settings for SQLAlchemy configuration.
    :rtype: sqlalchemy.engine.base.Engine
    """
    return engine_from_config(settings, prefix)


# =============================================================================
def get_dbsession_factory(dbengine):
    """Get SQLAlchemy session factory.

    :type  dbengine: sqlalchemy.engine.base.Engine
    :param dbengine:
        Database engine.
    :rtype: :func:`sqlalchemy.orm.session.sessionmaker`
    """
    factory = sessionmaker()
    factory.configure(bind=dbengine)
    return factory


# =============================================================================
def get_tm_dbsession(dbsession_factory, transaction_manager):
    """Get a ``sqlalchemy.orm.Session`` instance backed by a transaction.

    :type  dbsession_factory: sqlalchemy.orm.session.sessionmaker
    :param dbsession_factory:
        Function to create session.
    :type transaction_manager: transaction._manager.ThreadTransactionManager
    :param transaction_manager:
        Transaction manager.
    :rtype: sqlalchemy.orm.session.Session

    This function will hook the session to the transaction manager which
    will take care of committing any changes.

    - When using pyramid_tm it will automatically be committed or aborted
      depending on whether an exception is raised.

    - When using scripts you should wrap the session in a manager yourself.

      For example::

          import transaction

          dbsession_factory = get_dbsession_factory(DB_METADATA.bind)
          with transaction.manager:
              dbsession = get_tm_dbsession(
                  dbsession_factory, transaction.manager)
    """
    dbsession = dbsession_factory()
    zope.sqlalchemy.register(
        dbsession, transaction_manager=transaction_manager)
    return dbsession


# =============================================================================
def add_column(table_class, column):
    """Add a column to a database table.

    :type  table_class: DBDeclarativeClass
    :param table_class:
        SQLAlchemy object of the table to proceed.
    :type  column: sqlalchemy.schema.Column
    :param column:
        Column to create.
    """
    table_class.__table__.append_column(column)

    dialect = DB_METADATA.bind.dialect
    table_name = str(column.compile(dialect=dialect))
    table_name = table_name.partition('.')[0] if '.' in table_name \
        else table_class.__table__.name
    try:
        DB_METADATA.bind.execute(
            'ALTER TABLE {table} ADD COLUMN {column} {type}'.format(
                table=table_name, column=column.name,
                type=column.type.compile(dialect=dialect)))
    except (ProgrammingError, OperationalError):  # pragma: nocover
        pass

    setattr(table_class, column.name, column)
