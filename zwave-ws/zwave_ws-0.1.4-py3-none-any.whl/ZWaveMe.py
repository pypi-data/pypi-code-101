import json
import logging
import threading
from .WebsocketListener import WebsocketListener


class ZWaveMe:
    """Main controller class"""
    def __init__(self, hass, config):
        self._config = config
        self._hass = hass
        self._devices = []
        self.entities = {}
        self._ws = None
        self._wshost = None
        self._configured = False
        self.start_ws()
        self.thread = None

    def start_ws(self):
        """get/find the websocket host"""
        self.thread = threading.Thread(target=self.init_websocket)
        self.thread.daemon = True
        self.thread.start()
        _LOGGER.debug("STARTED THREAD")

    def send_command(self, device_id, command):
        self._ws.send(
            json.dumps(
                {
                    "event": "httpEncapsulatedRequest",
                    "data": {
                        "method": "GET",
                        "url": "/ZAutomation/api/v1/devices/{}/command/{}".format(
                            device_id, command
                        ),
                    },
                }
            )
        )

    def get_devices(self):
        return self._devices

    def get_devices_by_device_type(self, device_type):
        return [
            device for device in self._devices if device["deviceType"] == device_type
        ]

    def init_websocket(self):
        # keep websocket open indefinitely
        while True:
            _LOGGER.debug("(re)init websocket")
            self._ws = WebsocketListener(
                ZWaveMe=self,
                on_message=self.on_message,
                on_error=self.on_error,
                on_close=self.on_close,
                token=self._config.data["token"],
                url=self._config.data["url"],
            )

            try:
                self._ws.run_forever(ping_interval=5)
            finally:
                self._ws.close()

    def on_message(self, _, utf):
        if utf:
            _LOGGER.debug("websocket msg: %s", utf)

            dict_data = json.loads(utf)
            _LOGGER.debug("websocket msg: %s", utf)
            if "type" not in dict_data.keys():
                return
            try:
                if dict_data["type"] == "ws-reply":
                    body = json.loads(dict_data["data"]["body"])
                    if body["data"]:
                        self._devices = [
                            device
                            for device in body["data"]["devices"]
                            if device["deviceType"] in ZWAVEPLATFORMS
                        ]
                        for device in self._devices:
                            _LOGGER.debug("CREATING DEVICE: %s", device)
                        if not self._configured:
                            self._hass.config_entries.async_setup_platforms(
                                self._config, PLATFORMS
                            )
                            self._configured = True
                elif dict_data["type"] == "me.z-wave.devices.level":
                    _LOGGER.debug("NEW DEVICE LEVEL: %s", self._devices)
                    for device in self._devices:
                        if device["id"] == dict_data["data"]["id"]:
                            device["visibility"] = dict_data["data"]["visibility"]
                            if device["deviceType"] == "sensorMultilevel":
                                device["metrics"]["level"] = round(
                                    float(dict_data["data"]["metrics"]["level"]), 1
                                )
                            else:
                                device["metrics"]["level"] = dict_data["data"][
                                    "metrics"
                                ]["level"]

                            if DOMAIN + "." + dict_data["data"]["id"] in self.entities:
                                self.entities[
                                    DOMAIN + "." + dict_data["data"]["id"]
                                ].schedule_update_ha_state()

            except Exception as e:
                _LOGGER.error("ERROR: %s", e)

    def on_error(self, *args, **kwargs):
        error = args[-1]
        _LOGGER.error("websocket error: %s" % str(error))

    def on_close(self, _, *args):
        _LOGGER.debug("websocket closed")
        for device in self._devices:
            device["visibility"] = False
        self._ws.connected = False

    def update_devices(self):
        return self._devices

    def get_device(self, deviceid):
        for device in self.get_devices():
            if "id" in device and device["id"].lower() == deviceid.lower():
                return device

    def get_ws(self):
        return self._ws

    def get_wshost(self):
        return self._wshost

    async def async_update(self):
        devices = self.update_devices()
