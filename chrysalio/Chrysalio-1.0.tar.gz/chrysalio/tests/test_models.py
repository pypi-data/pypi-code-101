# pylint: disable = import-outside-toplevel
"""Tests of ``models`` functions and class."""

from unittest import TestCase

from sqlalchemy import Column, Integer
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy.engine.base import Engine
import transaction

from pyramid import testing

from . import DBUnitTestCase


# =============================================================================
class UModelsIncludeme(TestCase):
    """Unit test class for :func:`models.includeme`."""

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        from ..models import DB_METADATA

        testing.tearDown()
        transaction.manager.abort()
        if DB_METADATA.bind:
            DB_METADATA.drop_all()

    # -------------------------------------------------------------------------
    def test_not_defined(self):
        """[u:models.includeme] not defined"""
        from ..models import includeme

        configurator = testing.setUp()
        self.assertRaises(SystemExit, includeme, configurator)

    # -------------------------------------------------------------------------
    def test_defined(self):
        """[u:models.includeme] defined"""
        from ..models import DB_METADATA

        configurator = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'})
        configurator.include('..models')
        self.assertIn('dbsession_factory', configurator.registry)
        self.assertIsNotNone(configurator.registry['dbsession_factory'])
        self.assertIsInstance(
            configurator.registry['dbsession_factory'], sessionmaker)
        self.assertIsNotNone(DB_METADATA.bind)
        self.assertIsInstance(DB_METADATA.bind, Engine)


# =============================================================================
class UModelsGetDBEngine(TestCase):
    """Unit test class for :func:`models.get_dbengine`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.get_dbengine]"""
        from ..models import get_dbengine

        dbengine = get_dbengine({'sqlalchemy.url': 'sqlite:///:memory:'})
        self.assertIsInstance(dbengine, Engine)


# =============================================================================
class UModelsGetDBSessionFactory(TestCase):
    """Unit test class for :func:`models.get_dbsession_factory`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.get_dbsession_factory]"""
        from ..models import get_dbengine, get_dbsession_factory

        dbsession_factory = get_dbsession_factory(
            get_dbengine({'sqlalchemy.url': 'sqlite:///:memory:'}))
        self.assertIsInstance(dbsession_factory, sessionmaker)


# =============================================================================
class UModelsGetTMDBSession(DBUnitTestCase):
    """Unit test class for :func:`models.get_tm_dbsession`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.get_tm_dbsession]"""
        from ..models import get_tm_dbsession

        with transaction.manager:
            dbsession = get_tm_dbsession(
                self.configurator.registry['dbsession_factory'],
                transaction.manager)
        self.assertIsInstance(dbsession, Session)


# =============================================================================
class UModelsAddColumn(DBUnitTestCase):
    """Unit test class for :func:`models.add_column`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:models.add_column]"""
        from ..models import add_column
        from ..models.dbuser import DBUser

        # pylint: disable = no-member
        counter = len(DBUser.__table__.columns)
        add_column(DBUser, Column('Age', Integer))
        self.assertEqual(len(DBUser.__table__.columns), counter + 1)
