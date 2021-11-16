# pylint: disable=broad-except, invalid-name
import os
from resources.models.database import SqlConnection


class DutDatabase(SqlConnection):

    def __init__(self):
        super(DutDatabase, self).__init__(db_name="dutdb")
        self.agent_table = "agent"
        self.slot_table = "slot"

    def get_all_dut(self):
        agents = self.get_all_agent()
        for agent in agents:
            agent["slots"] = self.get_slots_by_agent(agent["name"])
        return agents

    def get_all_agent(self):
        cmd = "SELECT * FROM {}".format(self.agent_table)
        agents = self.execute_sql_command(cmd)
        agents_dict = [self._convert_to_agent_dict(item) for item in agents]
        return agents_dict

    @staticmethod
    def _convert_to_agent_dict(agent_item):
        agent = {
            "name": agent_item[0],
            "os": agent_item[1],
            "ip": agent_item[2],
            "port": agent_item[3],
            "label": agent_item[4],
            "description": agent_item[5],
            "platform": agent_item[6],
            "update_time": agent_item[7],
        }
        return agent

    def get_slots_by_agent(self, agent):
        cmd = "SELECT * FROM {} WHERE `agent`='{}'".format(self.slot_table, agent)
        slots = self.execute_sql_command(cmd)
        slots_dict = [self._convert_to_slot_dict(slot) for slot in slots]
        return slots_dict

    @staticmethod
    def _convert_to_slot_dict(slot_item):
        slot_dict = {
            "name": slot_item[0],
            "config_name": slot_item[1],
            "slot": slot_item[2],
            "vendor": slot_item[3],
            "fw_version": slot_item[4],
            "commit": slot_item[5],
            "ise/sed": slot_item[6],
            "sn": slot_item[7],
            "cap": slot_item[8],
            "bb": slot_item[9],
            "max_ec": slot_item[10],
            "status": slot_item[11],
            "update_time": slot_item[12],
        }
        return slot_dict

