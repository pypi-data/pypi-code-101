import abc
import logging

from cosmics.domain import model
from cosmics.repository import database

logger = logging.getLogger(__name__)

DatabaseModel = model.AbstractModel


class NotFoundInDatabaseError(Exception):
    """Raised when a requested entry was not found in the database."""


class AbstractRepository(abc.ABC):
    """Represents an abstract database target.

    Parameters
    ----------
    client : cosmics.database.AbstractClient
        Client for interaction with the database.

    A target can e.g. be a table in an SQL database.

    """

    _target: str
    _model: type[DatabaseModel]

    def __init__(self, client: database.AbstractClient):
        """Initialize the repository."""
        self._client = client
        self.added: list[DatabaseModel] = []
        self.fetched: list[DatabaseModel] = []
        self.updated: list[DatabaseModel] = []
        self.deleted: list[DatabaseModel] = []

    @property
    def target(self) -> str:
        """Construct target name."""
        return self._target

    @property
    def items(self) -> list[DatabaseModel]:
        """Get all items from the repository."""
        return self.get_all()

    def add(self, item: DatabaseModel) -> None:
        """Add item to database.

        Parameters
        ----------
        item : model.AbstractModel
            The item to add.

        """
        logger.debug("Adding to target %s item %s", self.target, item)
        self._add(item)
        self.added.append(item)

    def get(self, identifier: database.Info) -> DatabaseModel:
        """Get item as model instance.

        Parameters
        ----------
        identifier : dict
            Identifier by which to select the item(s).

        Raises
        ------
        NotFoundInDatabaseError
            If the respective identifier was not found.

        """
        logger.debug(
            "Trying to get item from target %s by identifier %s",
            self.target,
            identifier,
        )
        match = self._get(identifier)
        item = self._model(**match)
        logger.debug("Found matching item %s for identifier %s", item, identifier)
        self.fetched.append(item)
        return item

    def get_all(self) -> list[DatabaseModel]:
        """Get all items as model instances."""
        logger.debug("Getting all items in %s", self.target)
        items = [self._model(**item) for item in self._get_all()]
        self.fetched.extend(items)
        logger.debug("Items are: %s", items)
        return items

    def update(self, item: DatabaseModel) -> None:
        """Update item.

        Parameters
        ----------
        item : model.AbstractModel
            The item to update.

        """
        logger.debug("Updating item in %s to %s", self.target, item)
        self._update(item)
        self.updated.append(item)

    def delete(self, item: DatabaseModel, force: bool = False) -> None:
        """Delete item(s).

        Parameters
        ----------
        item : model.AbstractModel
            The item to delete.
        force : bool, default False
             Whether to force the deletion.

        """
        logger.debug("Deleting from target %s item %s", self.target, item)
        self._delete(item, force=force)
        self.deleted.append(item)

    def _add(self, item: DatabaseModel) -> None:
        with self._client as client:
            client.insert(
                target=self.target,
                data=item.to_dict(),
            )

    def _get(self, identifier: database.Info) -> database.Info:
        with self._client as client:
            try:
                [match] = client.select(target=self.target, where=identifier)
            except ValueError:
                raise NotFoundInDatabaseError(
                    "No entry in target %s with identifier(s) %s",
                    self.target,
                    identifier,
                )
            else:
                return match

    def _get_all(self) -> list[database.Info]:
        with self._client as client:
            return client.select(target=self.target)

    def _update(self, item: DatabaseModel) -> None:
        with self._client as client:
            client.update(
                target=self.target,
                data=item.to_dict(),
                where=item.identifier,
            )

    def _delete(self, item: DatabaseModel, force: bool) -> None:
        with self._client as client:
            client.delete(
                target=self.target,
                where=item.identifier,
                force=force,
            )
