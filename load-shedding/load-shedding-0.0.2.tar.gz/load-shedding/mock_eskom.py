#      A python library for getting Load Shedding schedules from Eskom.
#      Copyright (C) 2021  Werner Pieterson
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import List

from eskom import Eskom, AreaInfo, Province, Stage, Suburb, Municipality


class MockEskom(Eskom):
    def find_suburbs(self, search_text: str, max_results: int = 300) -> List[Suburb]:
        return [
            {
                'Id': 1058852,
                'MunicipalityName': 'City of Cape Town',
                'Name': 'Milnerton',
                'ProvinceName': 'Western Cape',
                'Total': 704
            }, {
                'Id': 1058853,
                'MunicipalityName': 'City of Cape Town',
                'Name': 'Milnerton Golf Course',
                'ProvinceName': 'Western Cape',
                'Total': 0
            }, {
                'Id': 1058854,
                'MunicipalityName': 'City of Cape Town',
                'Name': 'Milnerton Outlying',
                'ProvinceName': 'Western Cape',
                'Total': 0
            }, {
                'Id': 1058855,
                'MunicipalityName': 'City of Cape Town',
                'Name': 'Milnerton Ridge',
                'ProvinceName': 'Western Cape',
                'Total': 704
            }, {
                'Id': 1058856,
                'MunicipalityName': 'City of Cape Town',
                'Name': 'Milnerton SP',
                'ProvinceName': 'Western Cape',
                'Total': 2816
            }, {
                'Id': 1069144,
                'MunicipalityName': 'City of Cape Town',
                'Name': 'Milnerton SP 1',
                'ProvinceName': 'Western Cape',
                'Total': 3520
            }, {
                'Id': 1069145,
                'MunicipalityName': 'City of Cape Town',
                'Name': 'Milnerton SP 2',
                'ProvinceName': 'Western Cape',
                'Total': 700
            }
        ]

    def get_municipalities(self, province: Province) -> List[Municipality]:
        return [
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Beaufort West', 'Value': '336'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Bergrivier', 'Value': '337'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Bitou', 'Value': '338'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Breede Valley', 'Value': '339'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Cape Agulhas', 'Value': '340'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Cederberg', 'Value': '341'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'City of Cape Town', 'Value': '342'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Drakenstein', 'Value': '343'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'George', 'Value': '344'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Hessequa', 'Value': '345'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Kannaland', 'Value': '346'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Knysna', 'Value': '347'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Laingsburg', 'Value': '348'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Langeberg', 'Value': '349'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Matzikama', 'Value': '350'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Mossel Bay', 'Value': '351'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Oudtshoorn', 'Value': '352'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Overstrand', 'Value': '353'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Prince Albert', 'Value': '354'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Saldanha Bay', 'Value': '355'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Stellenbosch', 'Value': '356'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Swartland', 'Value': '357'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Swellendam', 'Value': '358'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Theewaterskloof', 'Value': '359'},
            {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'Witzenberg', 'Value': '360'}
        ]

    def get_schedule(self, province: Province, suburb: Suburb, stage: Stage) -> List[tuple]:
        return [
            ['2021-11-11 06:00', '2021-11-11 08:30'], ['2021-11-12 06:00', '2021-11-12 08:30'],
            ['2021-11-12 14:00', '2021-11-12 16:30'], ['2021-11-13 12:00', '2021-11-13 14:30'],
            ['2021-11-13 20:00', '2021-11-13 22:30'], ['2021-11-14 20:00', '2021-11-14 22:30'],
            ['2021-11-15 04:00', '2021-11-15 06:30'], ['2021-11-16 04:00', '2021-11-16 06:30'],
            ['2021-11-16 12:00', '2021-11-16 14:30'], ['2021-11-17 10:00', '2021-11-17 12:30'],
            ['2021-11-17 18:00', '2021-11-17 20:30'], ['2021-11-18 18:00', '2021-11-18 20:30'],
            ['2021-11-19 02:00', '2021-11-19 04:30'], ['2021-11-20 02:00', '2021-11-20 04:30'],
            ['2021-11-20 10:00', '2021-11-20 12:30'], ['2021-11-21 08:00', '2021-11-21 10:30'],
            ['2021-11-21 16:00', '2021-11-21 18:30'], ['2021-11-22 16:00', '2021-11-22 18:30'],
            ['2021-11-23 00:00', '2021-11-23 02:30'], ['2021-11-24 00:00', '2021-11-24 02:30'],
            ['2021-11-24 08:00', '2021-11-24 10:30'], ['2021-11-25 06:00', '2021-11-25 08:30'],
            ['2021-11-25 14:00', '2021-11-25 16:30'], ['2021-11-26 14:00', '2021-11-26 16:30'],
            ['2021-11-26 22:00', '2021-11-26 00:30'], ['2021-11-27 22:00', '2021-11-27 00:30'],
            ['2021-11-28 06:00', '2021-11-28 08:30'], ['2021-11-29 04:00', '2021-11-29 06:30'],
            ['2021-11-29 12:00', '2021-11-29 14:30'], ['2021-11-30 12:00', '2021-11-30 14:30'],
            ['2021-11-30 20:00', '2021-11-30 22:30'], ['2021-12-01 18:00', '2021-12-01 20:30'],
            ['2021-12-02 02:00', '2021-12-02 04:30'], ['2021-12-03 02:00', '2021-12-03 04:30'],
            ['2021-12-03 10:00', '2021-12-03 12:30'], ['2021-12-04 10:00', '2021-12-04 12:30'],
            ['2021-12-04 18:00', '2021-12-04 20:30'], ['2021-12-05 16:00', '2021-12-05 18:30'],
            ['2021-12-06 00:00', '2021-12-06 02:30'], ['2021-12-07 00:00', '2021-12-07 02:30'],
            ['2021-12-07 08:00', '2021-12-07 10:30'], ['2021-12-08 08:00', '2021-12-08 10:30'],
            ['2021-12-08 16:00', '2021-12-08 18:30'], ['2021-12-09 14:00', '2021-12-09 16:30'],
            ['2021-12-09 22:00', '2021-12-09 00:30']
        ]

    def get_schedule_area_info(self, suburb: Suburb) -> AreaInfo:
        return {
            'province': {'id': 9, 'name': 'Western Cape'},
            'city': {'id': 342, 'name': 'City of Cape Town'},
            'suburb': {'id': 1058852, 'name': 'Milnerton'},
            'period': ['11-11-2021', '08-12-2021']
        }

    def get_stage(self) -> Stage:
        return Stage.NO_LOAD_SHEDDING
