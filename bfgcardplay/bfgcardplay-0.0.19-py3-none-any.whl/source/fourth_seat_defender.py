"""Fourth seat card play for defender."""

import random
from typing import List, Union, Tuple
from bridgeobjects.source.constants import CARD_VALUES
from termcolor import colored

import inspect
from ..logger import log

from bridgeobjects import SUITS, Card, Denomination, Suit
from bfgsupport import Board, Trick
import bfgcardplay.source.global_variables as global_vars

from .player import Player
from .fourth_seat import FourthSeat
from .defender_play import get_hilo_signal_card

MODULE_COLOUR = 'cyan'

class FourthSeatDefender(FourthSeat):
    def __init__(self, player: Player):
        super().__init__(player)
        self.player = player

    def selected_card(self) -> Card:
        """Return the card if the third seat."""
        player = self.player
        trick = player.board.tricks[-1]
        manager = global_vars.manager

        cards = player.cards_for_trick_suit(trick)

        # Void
        if not cards:
            return self._select_card_if_void(player, trick)

        # Singleton
        if len(cards) == 1:
            return log(inspect.stack(), cards[0])

        # play low if partner is winning trick
        if self._second_player_winning_trick(cards, trick, player.trump_suit):
            return log(inspect.stack(), cards[-1])

        # win trick if possible
        winning_card = self._winning_card(trick)
        unplayed_cards = player.total_unplayed_cards[trick.suit.name]
        if winning_card:
            value = winning_card.value
            play_winner = False
            while value > 0:
                value -= 1
                card = Card(CARD_VALUES[value], trick.suit.name)
                if card in unplayed_cards and card not in player.dummys_unplayed_cards[trick.suit.name]:
                    play_winner = True
                    break
            if play_winner:
                return log(inspect.stack(), winning_card)

        # Signal even/odd
        return get_hilo_signal_card(player, cards)

    def _select_card_if_void(self, player: Player, trick: Trick) -> Card:
        """Return card if cannot follow suit."""
        player.record_void(trick.suit)
        manager = global_vars.manager

        # Trump if appropriate
        if player.trump_suit:
            (value_0, value_1, value_2) = self._trick_card_values(trick, player.trump_suit)
            if player.trump_cards:
                if value_0 > value_1 or value_2 > value_1:
                    for card in player.trump_cards[::-1]:
                        if card.value + 13 > value_0 and card.value + 13 > value_2:
                            return log(inspect.stack(), card)

        # Signal best suit
        best_suit = self._best_suit()
        other_suit = player.other_suit_for_signals(best_suit)
        if player.dummy_on_right:
            suit_cards = player.suit_cards[best_suit.name]
            if not manager.like_dislike(player.seat, best_suit.name):
                manager.set_like_dislike(player.seat, best_suit.name, True)
                for card in suit_cards:
                    if not card.is_honour:
                        return log(inspect.stack(), card)

            retain_suit = {suit_name: False for suit_name in SUITS}
            for suit_name in SUITS:
                cards = player.unplayed_cards[suit_name]
                if cards:
                    if len(cards) == 1 and player.is_winner(cards[0]):
                        retain_suit[suit_name] = True

            other_suit_cards = player.suit_cards[other_suit]
            if other_suit_cards and not retain_suit[other_suit]:
                return log(inspect.stack(), other_suit_cards[-1])


        for suit_name in SUITS:
            if suit_name != best_suit.name and suit_name != other_suit:
                final_suit_cards = player.suit_cards[suit_name]
                if final_suit_cards:
                    return log(inspect.stack(), final_suit_cards[-1])

        cards = player.suit_cards[best_suit.name]
        if len(cards) == 1:
            return log(inspect.stack(), cards[0])

        for index, card in enumerate(cards[:-1]):
            if card.value > cards[index+1].value + 1:
                return log(inspect.stack(), card)
        if cards:
            return log(inspect.stack(), cards[-1])

        for suit_name in SUITS:
            if player.unplayed_cards[suit_name]:
                return log(inspect.stack(), player.unplayed_cards[suit_name][-1])

    def _best_suit(self) -> Suit:
        """Select suit for signal."""
        # TODO handle no points and equal suits
        player = self.player
        cards = player.hand_cards.list
        suit_points = player.get_suit_strength(cards)
        max_points = 0
        best_suit = self._strongest_suit()
        return best_suit
        for suit in SUITS:
            if suit != player.trump_suit.name:
                hcp = suit_points[suit]
                if hcp > max_points:
                    max_points = hcp
                    best_suit = suit
        if not best_suit:
            for suit in SUITS:
                if suit != player.trump_suit.name:
                    hcp = suit_points[suit]
                    if hcp > max_points:
                        max_points = hcp
                        best_suit = suit
        if not best_suit:
            return player.trump_suit
        return Suit(best_suit)

    def _strongest_suit(self) -> Union[Suit, None]:
        """Return the strongest_suit."""
        player = self.player
        suits = {suit: 0 for suit in SUITS}
        for suit in SUITS:
            cards = player.unplayed_cards[suit]
            for card in cards:
                suits[suit] += card.value
        if player.trump_suit:
            suits[player.trump_suit.name] = 0
        best_suits = player.get_list_of_best_scores(suits)
        # if not best_suits:
        #     return player.trump_suit
        return Suit(random.choice(best_suits))