from abc import ABC
from typing import Type

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.db.models import ProtectedError

from ad_import.load_data import LoadAd
from ad_import.models import Directory


class ADBaseCommand(BaseCommand, ABC):
    load_class: Type[LoadAd] = None

    def add_arguments(self, parser):
        directories = Directory.objects.all().values_list('name', flat=True)
        parser.add_argument('directory', nargs='+',
                            choices=list(directories), help='AD')

    @staticmethod
    def get_directories(options):
        if type(options['directory']) == list:
            directories = []
            for directory_string in options['directory']:
                directory = Directory.find_directory(directory_string)
                directories.append(directory)
            return directories
        elif type(options['directory']) == str:
            return Directory.find_directory(options['directory'])

    @staticmethod
    def run_queries(directory: Directory, load_class: Type[LoadAd]):
        print('Loading from %s' % directory)
        load = load_class()
        load.connect(directory=directory)
        for query in load.queries:
            print('Run query %s' % query)
            load.load(query)

        if hasattr(load, 'get_inactive'):
            inactive = load.get_inactive()
            try:
                inactive.delete()
            except ProtectedError:
                print('Protected relations')
            except IntegrityError:
                print('Integrity error')

    def load(self, options: dict, load_class: Type[LoadAd]):
        for directory in self.get_directories(options):
            self.run_queries(directory, load_class)
