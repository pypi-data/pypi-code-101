"""Methods to support Defender play."""
from typing import List, Dict, Tuple, Union
from termcolor import colored

import inspect
from ..logger import log

from bridgeobjects import Card, Suit, CARD_VALUES
from bfgsupport import Trick

import bfgcardplay.source.global_variables as global_vars
from .player import Player

MODULE_COLOUR = 'magenta'

def deduce_partner_void_in_trumps(player: Player) -> bool:
    """Return True if we can deduce that partner is void in trumps."""
    suit = player.trump_suit.name
    auction = player.board.auction
    opening_call = auction.seat_calls[player.declarer][0]
    if opening_call.level == 3 and opening_call.denomination == player.trump_suit:
        my_trumps = player.hand.cards_by_suit[suit]
        dummys_trumps = player.hands[player.dummy].cards_by_suit[suit]
        if len(my_trumps) + len(dummys_trumps) >= 5:
            return True
    return False

def dummy_is_short_trump_hand(player: Player) -> bool:
    """Return True if dummy is short trump hand."""
    return len(player.hands[player.dummy].cards_by_suit[player.trump_suit.name]) <= 4

def get_hilo_signal_card(player, cards: List[Card]) -> Card:
    manager = global_vars.manager
    """Return a signal card denoting even/odd"""
    trick = player.board.tricks[-1]
    if len(cards) % 2 == 0:
        if len(cards) == 2:
            if not cards[-2].is_honour:
                manager.set_even_odd(player.seat, trick.suit.name, 0)
                return log(inspect.stack(), cards[-2])
            return log(inspect.stack(), cards[-1])

    manager.set_even_odd(player.seat, trick.suit.name, 1)
    return log(inspect.stack(), cards[-1])
