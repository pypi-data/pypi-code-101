"""Main classes for dsinfluxlogger"""
from __future__ import annotations

import asyncio
from typing import cast, Optional, List, Any, Dict
from dataclasses import dataclass, field
import logging

import aiohttp
from aioinflux import InfluxDBClient, InfluxDBError  # type: ignore
from flatten_dict import flatten  # type: ignore
from datastreamcorelib.pubsub import PubSubMessage, Subscription
from datastreamcorelib.datamessage import PubSubDataMessage
from datastreamservicelib.service import SimpleService

LOGGER = logging.getLogger(__name__)


@dataclass
class InfluxLoggerService(SimpleService):
    """Main class for dsinfluxlogger"""

    _client: Optional[InfluxDBClient] = field(init=False, default=None)
    _error_count: int = field(init=False, default=0)

    async def teardown(self) -> None:
        """teardown"""
        if self._client:
            await self._client.close()
        await super().teardown()

    def reload(self) -> None:
        """Load configs, restart sockets"""
        super().reload()
        self.create_task(self.reload_async())

    async def reload_client(self) -> None:
        """Reload the influxdb client"""
        if self._client:
            await self._client.close()
        self._client = InfluxDBClient(**self.config["db"])
        self._error_count = 0

    async def reload_async(self) -> None:
        """async reload"""
        await self.reload_client()
        # die early if db cannot be contacted
        if not self._client:
            raise RuntimeError("No client, this should not happen")
        await self._client.ping()

        for subinfo in self.config["subscriptions"]:
            sub = Subscription(
                subinfo["zmq"][0],
                subinfo["zmq"][1],
                self.message_callback,
                decoder_class=PubSubDataMessage,
                metadata={"config": subinfo},
            )
            self.psmgr.subscribe_async(sub)

    async def retry_point(self, point: Dict[str, Any]) -> None:
        """Retry writing of point, but with rate-limit"""
        await asyncio.sleep(0.1)
        await self.write_point(point)

    async def write_point(self, point: Dict[str, Any]) -> None:
        """Wrap the write to a task"""
        if self._client is None:
            LOGGER.error("No client, trying to reload")
            await self.reload_client()
            if not self._client:
                raise RuntimeError("No client even after reload")
        LOGGER.debug("About to write {}".format(repr(point)))
        try:
            await self._client.write(point)
            self._error_count = 0
        except InfluxDBError as exc:
            self._error_count += 1
            LOGGER.error("DB error {}".format(exc))
            LOGGER.warning("Failed to write {}".format(repr(point)))
        except aiohttp.ClientError as exc:
            self._error_count += 1
            LOGGER.error("Client error {}".format(exc))
            LOGGER.warning("Failed to write {}".format(repr(point)))
            # Retry on HTTP client errors
            self.create_task(self.retry_point(point))
        if self._error_count >= 5:
            LOGGER.error("Too many errors ({})".format(self._error_count))
            self.quit(1)

    @classmethod
    def message_to_point(cls, config: Dict[str, Any], msg: PubSubDataMessage) -> Dict[str, Any]:
        """Convert message to a point"""
        tag_fields: List[str] = config.get("tag_fields", [])
        exclude_fields: List[str] = config.get("exclude_fields", [])
        include_fields: Optional[List[str]] = config.get("include_fields", None)
        # start creating the point
        # FIXME: use dataframes for batched writes
        #  see https://aioinflux.readthedocs.io/en/stable/usage.html#writing-dictionary-like-objects
        point = {"time": msg.data["systemtime"], "measurement": config["measurement"], "tags": {}, "fields": {}}
        # resolve tags
        for name in tag_fields:
            point["tags"][name] = msg.data[name]
        # resolve fields to include
        if include_fields is None:
            include_fields = []
            for name in msg.data.keys():
                if name in exclude_fields + ["systemtime"]:
                    continue
                include_fields.append(name)
        # Start adding values
        values_dict: Dict[str, Any] = {}
        for name in include_fields:
            values_dict[name] = msg.data[name]
        # Flatten the values
        point["fields"] = flatten(values_dict, reducer="underscore", enumerate_types=(list, tuple))
        return point

    async def message_callback(self, sub: Subscription, msg: PubSubMessage) -> None:
        """Callback for the example subscription"""
        msg = cast(PubSubDataMessage, msg)
        point = InfluxLoggerService.message_to_point(sub.metadata["config"], msg)
        self.create_task(self.write_point(point))
