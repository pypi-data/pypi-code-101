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

import json
import logging
from datetime import datetime
from typing import Dict

from .eskom import Eskom, Province, Stage, Suburb


def get_area_schedule(provider: Eskom, province: Province, suburb: Suburb, cached: bool = False) -> Dict[Stage, list]:
    stage_schedule = {}

    if cached:
        try:
            cache_file = ".cache/{suburb_id}.json".format(suburb_id=suburb.id)
            with open(cache_file, "r") as cache:
                stage_schedule = json.loads(cache.read(), object_pairs_hook=lambda pairs: {Stage(int(k)).value: v for k, v in pairs})

            today = datetime.now().date()
            first = datetime.strptime(stage_schedule.get(Stage.STAGE_1.value)[0][0], "%Y-%m-%d %H:%M").date()
            if today > first:
                stage_schedule = {}
        except Exception as e:
            logging.log(logging.ERROR, "Unable to get result from cache. {e}".format(e=e))

    if not stage_schedule:
        for stage in range(Stage.STAGE_1.value, Stage.STAGE_5.value):
            stage_schedule[stage] = provider.get_schedule(province=province, suburb=suburb, stage=stage)

        if cached:
            cache_file = ".cache/{suburb_id}.json".format(suburb_id=suburb.id)
            with open(cache_file, "w") as cache:
                cache.write(json.dumps(stage_schedule))

    return stage_schedule


def get_schedule(provider: Eskom, province: Province, suburb: Suburb, stage: Stage = None, cached: bool = True) -> Dict[int, list]:
    if not stage:
        try:
            stage = provider.get_stage()
        except Exception as e:
            logging.log(logging.ERROR, "Unknown status".format(e=e))
        else:
            if stage == Stage.NO_LOAD_SHEDDING:
                raise Exception("Schedule not available for stage: {stage}".format(stage=Stage.NO_LOAD_SHEDDING))

    area_schedule = get_area_schedule(provider, province, suburb, cached=cached)
    return area_schedule.get(stage.value)


def list_to_dict(schedule: list) -> Dict:
    schedule_dict = {}
    now = datetime.now()
    for item in schedule:
        start = datetime.strptime(item[0], "%Y-%m-%d %H:%M")
        end = datetime.strptime(item[1], "%Y-%m-%d %H:%M")

        schedule_dict[start.strftime("%Y-%m-%d")] = (
            now.replace(month=start.month, day=start.day, hour=start.hour, minute=start.minute, microsecond=0).strftime(
                "%H:%M"),
            now.replace(month=end.month, day=end.day, hour=end.hour, minute=end.minute, microsecond=0).strftime(
                "%H:%M"),
        )
    return schedule_dict


if __name__ == "__main__":
    eskom = Eskom()
    suburb = "Milnerton"
    suburbs = eskom.find_suburbs(search_text=suburb)
    print("Searching suburbs for {suburb}: {suburbs}".format(suburb=suburb, suburbs=suburbs))
    schedule = eskom.get_schedule(province=suburbs[0].province, suburb=suburbs[0], stage=Stage.STAGE_2)
    print("Schedule for {suburb}: {schedule}".format(suburb=suburb, schedule=schedule))
