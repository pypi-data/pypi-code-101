# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Callable, List, Optional, Union
from time import sleep

# Pip
from ktg import Telegram

# Local


# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- class: Notifier ------------------------------------------------------- #

class Notifier:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        tg_token: str,
        tg_chat_id: str
    ):
        self.tg = Telegram(
            token=tg_token,
            chat_id=tg_chat_id
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def start(
        self,
        def_to_execute: Callable[
            [
                float,
                Optional[
                    Union[
                        List[str],
                        str
                    ]
                ]
            ],
            None
        ],
        *def_args,
        **def_kwargs
    ) -> None:
        self.tg.send('started')

        while True:
            sleep_seconds, resp = def_to_execute(*def_args, **def_kwargs)

            if isinstance(resp, str):
                resp = [resp]

            if resp:
                for _resp in resp:
                    self.tg.send(_resp)

            sleep(sleep_seconds)


# -------------------------------------------------------------------------------------------------------------------------------- #