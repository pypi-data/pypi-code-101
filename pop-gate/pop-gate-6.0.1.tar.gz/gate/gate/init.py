import json
from typing import Any
from typing import Dict
from typing import List


def __init__(hub):
    hub.pop.sub.add(dyne_name="tree")
    hub.pop.sub.add(dyne_name="matcher")
    hub.pop.sub.add(dyne_name="srv")


def cli(hub):
    hub.pop.config.load(["gate"], cli="gate")
    hub.pop.loop.create()
    coro = hub.gate.init.start(
        gate_server=hub.OPT.gate.server,
        host=hub.OPT.gate.host,
        port=hub.OPT.gate.port,
        matcher_plugin=hub.OPT.gate.matcher,
        prefix=hub.OPT.gate.prefix,
        refs=hub.OPT.gate.refs,
        limit_concurrency=hub.OPT.gate.limit_concurrency,
    )
    hub.pop.Loop.run_until_complete(coro)


async def start(
    hub,
    gate_server: str,
    host: str,
    port: int,
    matcher_plugin: str,
    prefix: str,
    refs: List[str],
    limit_concurrency: int = None,
):
    return await hub.srv[gate_server].start(
        host=host,
        port=port,
        matcher_plugin=matcher_plugin,
        prefix=prefix,
        refs=refs,
        limit_concurrency=limit_concurrency,
    )


async def tree(
    hub, prefix: str = None, refs: List[str] = None, matcher_plugin: str = None
) -> Dict[str, Any]:
    """
    Get details of all references that are exposed through the gate API
    """
    if prefix is None:
        prefix = hub.OPT.gate.prefix
    if matcher_plugin is None:
        matcher_plugin = hub.OPT.gate.matcher
    if refs is None:
        refs = hub.OPT.gate.refs

    _tree: Dict[str, Any] = await hub.tree.init.traverse()

    def _get_ref(t: Dict[str, Any]):
        rf = t.get("ref")
        if (
            rf
            and isinstance(rf, str)
            and hub.matcher[matcher_plugin].match(t["ref"], prefix=prefix, refs=refs)
        ):
            # This item has a ref and is available to the api
            return t
        else:
            r = {}
            for k, v in t.items():
                if isinstance(v, Dict):
                    sub_ref = _get_ref(v)
                    if sub_ref:
                        r[k] = sub_ref
            return r

    ret = _get_ref(_tree)

    return json.loads(hub.output.json.display(ret))


async def stop(hub, gate_server: str):
    hub.log.debug("Shutting down gate server")
    return await hub.srv[gate_server].stop()


async def join(hub, gate_server):
    return await hub.srv[gate_server].join()


async def test(hub, *args, **kwargs):
    """
    The test function for gate
    """
    return {"args": args, "kwargs": kwargs}
