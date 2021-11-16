import logging
import os
import json
from websockets import connect
import asyncio
import graphyte
import math

class Tempest:
    def __init__(self, **config):
        self.token = os.environ.get('TEMPEST_TOKEN', config.get('token',None))
        self.device_id = os.environ.get('TEMPEST_DEVICE_ID', config.get('device_id', None))
        self.url = os.environ.get("TEMPEST_WS_URI", 'wss://ws.weatherflow.com/swd/data')
        self.uri = "{}?api_key={}".format(self.url, self.token)
        self.graphite_host = os.environ.get("GRAPHITE_HOST", config.get('graphite_host', '127.0.0.1'))
        self.socket_id = os.environ.get("TEMPEST_WS_ID", '17084482-45b9')

    def Listen(self):
        asyncio.run(self._establish_websocket())

    async def _establish_websocket(self):
        listen_message = {
            'type': 'listen_start',
            'device_id': self.device_id,
            'id': self.socket_id
        }
        async with connect(self.uri) as websocket:
            await websocket.send(json.dumps(listen_message))
            while True:
                message = json.loads(await websocket.recv())
                logging.debug("Received message type {}".format(message['type']))
                if message['type'] == 'obs_st':
                    logging.info("Received observation message...")
                    self._send_graphite(message['obs'][0])

    def _send_graphite(self, metrics):
        logging.debug(json.dumps(metrics))
        ## https://weatherflow.github.io/Tempest/api/ws.html
        values = {
            'wind_lull': metrics[1],
            'wind_avg': metrics[2],
            'wind_guest': metrics[3],
            'wind_direction': metrics[4],
            'wind_sample_interval': metrics[5],
            'station_pressure': metrics[6],
            'air_temprature': metrics[7],
            'relative_humidity': metrics[8],
            'illuminance': metrics[9],
            'uv': metrics[10],
            'solar_radiation': metrics[11],
            'rain_accumulated': metrics[12],
            'precipitation_type': metrics[13],
            'lightning_strike_avg_distance': metrics[14],
            'lightning_strike_count': metrics[15],
            'battery': metrics[16],
            'report_interval': metrics[17],
            'local_daily_rain_accumulation': metrics[18],
            'dew_point': self._get_dew_point_c(metrics[7], metrics[8])
        }
        graphyte.init(self.graphite_host)
        for value in values:
            logging.debug("Sending tempest.{}: {}".format(value, values[value]))
            graphyte.send("tempest.{}".format(value), values[value])

    def _get_dew_point_c(self, t_air_c, rel_humidity):
        ### https://gist.github.com/sourceperl/45587ea99ff123745428
        """Compute the dew point in degrees Celsius
        :param t_air_c: current ambient temperature in degrees Celsius
        :type t_air_c: float
        :param rel_humidity: relative humidity in %
        :type rel_humidity: float
        :return: the dew point in degrees Celsius
        :rtype: float
        """
        A = 17.27
        B = 237.7
        alpha = ((A * t_air_c) / (B + t_air_c)) + math.log(rel_humidity/100.0)
        return (B * alpha) / (A - alpha)


