import json
import os

from bvx_env import values as envs
from bvx_oop import Singleton
from bvx_pytest.es import BVX_PYTEST_DOCKER_ES_PORT_ENV_KEY, \
    BVX_PYTEST_DOCKER_ES_HOST_ENV_KEY
from elasticsearch import Elasticsearch as OrgElasticsearch


class Elasticsearch(Singleton):
    # connection
    __conn = None

    # host
    __hosts = None

    # maxsize
    __maxsize = 25

    # sniff_on_start
    __sniff_on_start = True

    # sniffer_timeout
    __sniffer_timeout = 10.0

    # sniff_on_connection_fail
    __sniff_on_connection_fail = True

    # sniff_timeout
    __sniff_timeout = 10.0

    # max_retries
    __max_retries = 3

    # retry_on_status
    __retry_on_status = (502, 503, 504)

    # retry_on_timeout
    __retry_on_timeout = True

    @property
    def pytest_host(self):
        """
        get hosts

        :return:
        """
        return str(os.environ.get(BVX_PYTEST_DOCKER_ES_HOST_ENV_KEY))

    @property
    def pytest_port(self):
        """
        get hosts

        :return:
        """
        return int(os.environ.get(BVX_PYTEST_DOCKER_ES_PORT_ENV_KEY))

    @property
    def maxsize(self):
        """
        get hosts

        :return:
        """
        return self.__maxsize

    @property
    def sniff_on_start(self):
        """
        get hosts

        :return:
        """
        return self.__sniff_on_start

    @property
    def sniffer_timeout(self):
        """
        get hosts

        :return:
        """
        return self.__sniffer_timeout

    @property
    def sniff_on_connection_fail(self):
        """
        get hosts

        :return:
        """
        return self.__sniff_on_connection_fail

    @property
    def sniff_timeout(self):
        """
        get hosts

        :return:
        """
        return self.__sniff_timeout

    @property
    def max_retries(self):
        """
        get hosts

        :return:
        """
        return self.__max_retries

    @property
    def retry_on_timeout(self):
        """
        get hosts

        :return:
        """
        return self.__retry_on_timeout

    @property
    def hosts(self):
        """
        get hosts

        :return:
        """

        if self.__hosts:
            return self.__hosts

        # get environs
        _env = envs()

        # init hosts list
        _hosts = []

        if _env.get('ES_HOSTS') is None:

            if _env.PYTEST_RUN_CONFIG:

                _hosts.append({
                    'host': self.pytest_host,
                    'port': self.pytest_port,
                })

            else:

                _hosts.append({
                    'host': '127.0.0.1',
                    'port': 9200
                })

        else:

            _hosts = json.loads(_env['ES_HOSTS'])

        return _hosts

    @property
    def connection(self):
        """
        get connection

        :return:
        """

        if self.__conn is None:
            self.__conn = OrgElasticsearch(
                hosts=self.hosts,
                maxsize=self.maxsize,
                sniff_on_start=self.sniff_on_start,
                sniff_on_connection_fail=self.sniff_on_connection_fail,
                sniffer_timeout=self.sniffer_timeout,
                sniff_timeout=self.sniff_timeout,
                max_retries=self.max_retries,
                retry_on_timeout=self.retry_on_timeout
            )

        return self.__conn

# EOF
