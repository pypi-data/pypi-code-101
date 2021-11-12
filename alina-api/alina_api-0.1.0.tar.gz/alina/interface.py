from alina.irena.client import IrenaClient
from alina.irena.factories import (
    IrenaAllocationTimetableFactory, IrenaAllocationIDFactory, IrenaAllocationDetailsFactory,
    IrenaTripCrewMembersFactory
)


class Alina:
    """Init creates an instance of the class with the following parameters: username, password, and authenticate.
    These are passed to the constructor function which creates an instance of IrenaClient with these values
    as its parameters. The 'authenticate' parameter represents whether or not authentication was required when creating
    this object from IrenaClient(). If True, then authentication must have been performed before being able to create
    an instance of Alina using this constructor; otherwise, it can be left as False and there will be no need for
    any additional code.
    """
    def __init__(self, username, password, authenticate=True):
        self._client = IrenaClient(username, password, authenticate)

    def authenticate(self):
        return self._client.authenticate()

    async def allocation_timetable(self, date):
        """Returns timetable which is actually a allocations list.
        """
        factory = IrenaAllocationTimetableFactory(self._client, date)
        timetable = await factory.produce()
        return timetable

    async def allocation_identifier(self, title, date):
        """Returns id of an allocation.
        """
        factory = IrenaAllocationIDFactory(self._client, title, date)
        id = await factory.produce()
        return id

    async def allocation_details(self, title, date):
        """Returns details about an allocation.
        """
        id = await self.allocation_identifier(title, date)
        factory = IrenaAllocationDetailsFactory(self._client, id, date)
        details = await factory.produce()
        return details

    async def trip_crew(self, trip, date):
        """Trip is usually a train number. Returns crew.
        """
        factory = IrenaTripCrewMembersFactory(self._client, trip, date)
        crew = await factory.produce()
        return crew