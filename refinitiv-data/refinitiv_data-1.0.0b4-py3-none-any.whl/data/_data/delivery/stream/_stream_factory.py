import itertools
from typing import TYPE_CHECKING, Dict, Union, Type, Optional, List

from . import OMMStreamConnection, RDPStreamConnection
from ._omm_stream import _OMMStream
from ._protocol_type import ProtocolType
from ._rdp_stream import _RDPStream
from ... import log
from ...content._content_type import ContentType
from ...content._types import OptDict, OptStr, Strings, ExtendedParams, OptCall

if TYPE_CHECKING:
    from . import StreamConnection
    from ...core.session.stream_service_discovery.stream_connection_configuration import (
        StreamConnectionConfiguration,
    )
    from ...core.session import Session

logger = log.root_logger.getChild("stream-factory")

stream_class_by_protocol_type: Dict[
    ProtocolType, Type[Union[_OMMStream, _RDPStream]]
] = {
    ProtocolType.OMM: _OMMStream,
    ProtocolType.RDP: _RDPStream,
}

id_iterator = itertools.count(1)  # cannot be 0


def create_stream(
    protocol_type: ProtocolType, **kwargs
) -> Union[_OMMStream, _RDPStream]:
    stream_class = stream_class_by_protocol_type.get(protocol_type)
    stream_id = next(id_iterator)
    stream = stream_class(stream_id=stream_id, **kwargs)
    return stream


def convert_api_to_content_type(api: str) -> ContentType:
    content_type = content_type_by_api.get(api)
    if content_type:
        return content_type

    # check if api has in config
    # if has
    # append to ContentType enum and return
    # else raise error


def create_omm_stream(
    content_type: ContentType,
    session: "Session",
    name: str,
    api: str = "",
    domain: OptStr = None,
    service: OptStr = None,
    fields: Optional[Strings] = None,
    key: OptDict = None,
    extended_params: "ExtendedParams" = None,
    on_refresh: OptCall = None,
    on_status: OptCall = None,
    on_update: OptCall = None,
    on_complete: OptCall = None,
    on_error: OptCall = None,
) -> _OMMStream:
    if content_type is ContentType.NONE:
        content_type = convert_api_to_content_type(api)

    if not content_type and not api:
        content_type = ContentType.PRICING

    stream_id = next(id_iterator)
    stream = _OMMStream(
        stream_id=stream_id,
        content_type=content_type,
        session=session,
        name=name,
        domain=domain,
        service=service,
        fields=fields,
        key=key,
        extended_params=extended_params,
        on_refresh=on_refresh,
        on_status=on_status,
        on_update=on_update,
        on_complete=on_complete,
        on_error=on_error,
    )
    logger.debug(f" + Created stream={stream.classname}")
    return stream


def create_rdp_stream(
    content_type: ContentType,
    session: "Session",
    service: str,
    universe: list,
    view: list,
    parameters: dict,
    extended_params: "ExtendedParams",
    api: str = "",
    on_ack: OptCall = None,
    on_response: OptCall = None,
    on_update: OptCall = None,
    on_alarm: OptCall = None,
) -> _RDPStream:
    if content_type is ContentType.NONE:
        content_type = convert_api_to_content_type(api)
    stream_id = next(id_iterator)
    stream = _RDPStream(
        stream_id=stream_id,
        content_type=content_type,
        session=session,
        service=service,
        universe=universe,
        view=view,
        parameters=parameters,
        extended_params=extended_params,
        on_ack=on_ack,
        on_response=on_response,
        on_update=on_update,
        on_alarm=on_alarm,
    )
    logger.debug(f" + Created stream={stream.classname}")
    return stream


protocol_type_by_name: Dict[str, ProtocolType] = {
    "OMM": ProtocolType.OMM,
    "RDP": ProtocolType.RDP,
}

content_type_by_api: Dict[str, ContentType] = {
    "streaming/pricing/main": ContentType.PRICING,
    "streaming/trading-analytics/redi": ContentType.TRADING,
    "streaming/quantitative-analytics/financial-contracts": ContentType.CONTRACTS,
}

api_by_content_type: Dict[ContentType, str] = {
    ContentType.CHAINS: "streaming/pricing/main",
    ContentType.PRICING: "streaming/pricing/main",
    ContentType.TRADING: "streaming/trading-analytics/redi",
    ContentType.CONTRACTS: "streaming/quantitative-analytics/financial-contracts",
}


def get_protocol_type_by_name(protocol_name: str) -> ProtocolType:
    protocol_type = protocol_type_by_name.get(protocol_name)

    if not protocol_type:
        raise ValueError(f"Can't find protocol type by name: {protocol_name}")

    return protocol_type


cxn_class_by_protocol_type: Dict[
    ProtocolType,
    Type[Union[OMMStreamConnection, RDPStreamConnection]],
] = {
    ProtocolType.OMM: OMMStreamConnection,
    ProtocolType.RDP: RDPStreamConnection,
}

_max_reconnect_default = 5

_subprotocol_by_content_by_protocol = {
    ContentType.CHAINS: {
        ProtocolType.OMM: "tr_json2",
    },
    ContentType.PRICING: {
        ProtocolType.OMM: "tr_json2",
    },
    ContentType.TRADING: {
        ProtocolType.OMM: "tr_json2",
        ProtocolType.RDP: "rdp_streaming",
    },
    ContentType.CONTRACTS: {
        ProtocolType.RDP: "rdp_streaming",
    },
}

_protocols_by_content = {
    ContentType.CHAINS: [ProtocolType.OMM],
    ContentType.PRICING: [ProtocolType.OMM],
    ContentType.TRADING: [ProtocolType.OMM, ProtocolType.RDP],
    ContentType.CONTRACTS: [ProtocolType.RDP],
}


def get_protocols(content_type: ContentType) -> List[ProtocolType]:
    protocols = _protocols_by_content.get(content_type)
    if not protocols:
        raise ValueError(f"Can't find protocol by content type: {content_type}")
    return protocols


def get_subprotocol(content_type: ContentType, protocol_type: ProtocolType) -> str:
    by_protocol = _subprotocol_by_content_by_protocol.get(content_type, {})

    if not by_protocol:
        raise ValueError(f"Can't find protocol for content type={content_type}")

    subprotocol = by_protocol.get(protocol_type)

    if not subprotocol:
        raise ValueError(
            f"Can't find subprotocol for content type={content_type}, "
            f"protocol type={protocol_type}"
        )

    return subprotocol


async def create_stream_cxn_async(
    content_type: ContentType,
    protocol_type: ProtocolType,
    session: "Session",
) -> "StreamConnection":
    api = api_by_content_type.get(content_type)
    config: "StreamConnectionConfiguration" = (
        await session._connection.get_stream_connection_configuration(api)
    )
    session_id = session.session_id
    stream_id = next(id_iterator)
    name = (
        f"WebSocket-{protocol_type.name}-{content_type.name} "
        f"id={session_id}.{stream_id}"
    )
    cxn_class = cxn_class_by_protocol_type.get(protocol_type)
    subprotocol = get_subprotocol(content_type, protocol_type)
    cxn = cxn_class(
        stream_id=stream_id,
        name=name,
        session=session,
        config=config,
        subprotocol=subprotocol,
        max_reconnect=_max_reconnect_default,
    )
    logger.debug(f" + Created cxn={cxn}")
    return cxn
