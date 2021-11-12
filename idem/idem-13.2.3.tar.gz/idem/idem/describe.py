import asyncio
import fnmatch
from typing import Any
from typing import Dict

import jmespath
import pop.contract
import pop.hub
import pop.loader
import tqdm


async def run(
    hub,
    desc_glob: str,
    acct_file: str,
    acct_key: str,
    acct_profile: str = "default",
    progress: bool = False,
    search_path: str = None,
    hard_fail: bool = False,
) -> Dict[str, Dict[str, Any]]:
    """
    :param hub:
    :param desc_glob:
    :param acct_file:
    :param acct_key:
    :param acct_profile:
    :param progress:
    :return:
    """
    ctx = await hub.idem.ex.ctx(
        path=desc_glob,
        acct_file=acct_file,
        acct_key=acct_key,
        acct_profile=acct_profile,
    )
    result = {}
    coros = [_ async for _ in hub.idem.describe.recurse(ctx, hub.states, desc_glob)]
    progress_bar = None
    if progress:
        progress_bar = tqdm.tqdm(total=len(coros))

    for ret in asyncio.as_completed(coros):
        if progress:
            progress_bar.update(1)
        try:
            result.update(await ret)
        except Exception as e:
            hub.log.error(f"Error during describe: {e.__class__.__name__}: {e}")
            if hard_fail:
                raise
    if progress:
        progress_bar.close()
    if search_path:
        return jmespath.search(search_path, result)
    return result


async def recurse(
    hub, ctx, mod: pop.loader.LoadedMod or pop.hub.Sub, glob: str, ref: str = ""
):
    if hasattr(mod, "_subs"):
        for sub in mod._subs:
            if ref:
                r = ".".join([ref, sub])
            else:
                r = sub
            async for c in hub.idem.describe.recurse(ctx, mod[sub], glob, r):
                yield c
    if hasattr(mod, "_loaded"):
        for loaded in mod._loaded:
            if ref:
                r = ".".join([ref, loaded])
            else:
                r = loaded
            async for c in hub.idem.describe.recurse(ctx, mod[loaded], glob, r):
                yield c

    if hasattr(mod, "_funcs"):
        if "describe" not in mod._funcs:
            return
        if fnmatch.fnmatch(ref, glob):
            if isinstance(mod.describe, pop.contract.ContractedAsync):
                coro = mod.describe(ctx)
            else:
                coro = hub.pop.loop.wrap(mod.describe, ctx)
            yield hub.pop.Loop.create_task(coro)
