from ad_import.load_data import LoadWorkstations
from ad_import.management.commands import ADBaseCommand


class Command(ADBaseCommand):
    def handle(self, *args, **options):
        self.load(options, LoadWorkstations)
