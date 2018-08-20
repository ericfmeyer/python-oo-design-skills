"""Package: casino.roulette
Module: game

Implements the RouletteGame class.
"""


class RouletteGame(object):
    """RouletteGame runs the roulette game.

    It gets bets from the player, spins the wheel, collects losing bets
    and pays winning bets.

    Collaborators:
        - Wheel: Game spins the wheel.
        - Bin: wheel returns winning bin.
        - Table: Game collects losing and winning bets from table.
        - Player: Game notifies player of win/loss.
        - Outcome: Game determines wins/losses based on outcomes in the bin.
    """

    straight_bet_odds = 35
    split_bet_odds = 17
    street_bet_odds = 11
    corner_bet_odds = 8
    five_bet_odds = 6
    line_bet_odds = 5
    dozen_bet_odds = 2
    column_bet_odds = 2
    even_money_bet_odds = 1

    straight_bet_name = 'Number'
    split_bet_name = 'Split'
    street_bet_name = 'Street'
    corner_bet_name = 'Corner'
    five_bet_name = 'Five 00-0-1-2-3'
    line_bet_name = 'Line'
    dozen_bet_name = 'Dozen'
    column_bet_name = 'Column'
    black_bet_name = 'Black'
    red_bet_name = 'Red'
    even_bet_name = 'Even'
    odd_bet_name = 'Odd'
    high_bet_name = 'High'
    low_bet_name = 'Low'

    red_bins = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
