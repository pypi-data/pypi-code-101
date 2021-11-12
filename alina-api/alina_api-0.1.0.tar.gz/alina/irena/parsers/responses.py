import abc
import asyncio

from bs4 import BeautifulSoup
from bs4.element import SoupStrainer

from alina.irena.parsers.containers import (
    IrenaContainerParser, IrenaAllocationContainerParser, IrenaAllocationDetailRowContainerParser,
    IrenaCrewMemberContainerParser
)
from alina.tools.expressions import (
    allocation_id_pattern, allocation_component_pattern
)


class IrenaRequestResponseParser(abc.ABC):
    container_parser: IrenaContainerParser

    @abc.abstractmethod
    def get_containers(self):
        """Returns containers which will parsed using parsers.
        """

    async def parse_response(self):
        """Tries to parse the response from a web service.
        Starts by getting all of the containers that are in the list and then creates an array of container parsers.
        Then it creates tasks for each parser, which will be executed in parallel.
        Each task is created with asyncio.create_task() and passed into parser's parse_container() method,
        which returns a parsed container object if successful or None otherwise.
        Once all of the tasks have been completed, they are gathered together using await asyncio.gather().
        """
        containers = self.get_containers()
        container_parsers = [self.container_parser(container) for container in containers]
        tasks = [asyncio.create_task(parser.parse_container()) for parser in container_parsers]
        parsed_containers = await asyncio.gather(*tasks)
        return [parsed_container for parsed_container in parsed_containers if parsed_container]


class IrenaAllocationTimetableRequestResponseParser(IrenaRequestResponseParser):
    container_parser = IrenaAllocationContainerParser

    def __init__(self, response):
        strainer = SoupStrainer(name='table', class_='duties calendar-table')
        self._soup = BeautifulSoup(markup=response.content, features='html.parser', parse_only=strainer)

    def get_containers(self):
        containers = self._soup.find_all(name='div', class_='allocation-day click-area clickable')
        return containers


class IrenaAllocationIDRequestResponseParser(IrenaRequestResponseParser):
    container_parser = None

    def __init__(self, response):
        strainer = SoupStrainer(name='div', class_='allocation-container display-full')
        soup = BeautifulSoup(markup=response.content, features='html.parser', parse_only=strainer)
        self._container = soup.find(name='div', class_='clickable')

    def get_containers(self):
        return

    def _get_id(self):
        attribute = 'data-url'
        data = self._container[attribute]
        id = allocation_id_pattern.search(data)['id']
        return id

    async def parse_response(self):
        try:
            return self._get_id()
        except AttributeError:
            return


class IrenaAllocationDetailsRequestResponseParser(IrenaRequestResponseParser):
    container_parser = IrenaAllocationDetailRowContainerParser

    def __init__(self, response):
        strainer = SoupStrainer(name='tbody')
        self._soup = BeautifulSoup(markup=response.content, features='html.parser', parse_only=strainer)

    def get_containers(self):
        return self._soup.find_all('tr', class_=allocation_component_pattern)


class IrenaTripCrewMembersRequestResponseParser(IrenaRequestResponseParser):
    container_parser = IrenaCrewMemberContainerParser

    def __init__(self, response):
        self._soup = BeautifulSoup(markup=response.content, features='html.parser')

    def get_containers(self):
        return self._soup.find_all('div', class_='crew-value')