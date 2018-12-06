"""Implements the RouletteGame class."""


class Game(object):
    """Game runs the roulette game.

    It gets bets from the player, spins the wheel, collects losing bets
    and pays winning bets.

    Collaborators:
        - Wheel: Game spins the wheel.
        - Bin: wheel returns winning bin.
        - Table: Game collects losing and winning bets from table.
        - Player: Game notifies player of win/loss.
        - Outcome: Game determines wins/losses based on outcomes in the bin.
    """

    STRAIGHT_BET_ODDS = 35
    SPLIT_BET_ODDS = 17
    STREET_BET_ODDS = 11
    CORNER_BET_ODDS = 8
    FIVE_BET_ODDS = 6
    LINE_BET_ODDS = 5
    DOZEN_BET_ODDS = 2
    COLUMN_BET_ODDS = 2
    EVEN_MONEY_BET_ODDS = 1

    STRAIGHT_BET_NAME = 'Number'
    SPLIT_BET_NAME = 'Split'
    STREET_BET_NAME = 'Street'
    CORNER_BET_NAME = 'Corner'
    FIVE_BET_NAME = 'Five 00-0-1-2-3'
    LINE_BET_NAME = 'Line'
    DOZEN_BET_NAME = 'Dozen'
    COLUMN_BET_NAME = 'Column'
    BLACK_BET_NAME = 'Black'
    RED_BET_NAME = 'Red'
    EVEN_BET_NAME = 'Even'
    ODD_BET_NAME = 'Odd'
    HIGH_BET_NAME = 'High'
    LOW_BET_NAME = 'Low'

    RED_BINS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19,
                21, 23, 25, 27, 30, 32, 34, 36]

    def __init__(self, wheel, table):
        """Construct a new game using the given Wheel and Table.

        :param wheel: (Wheel) the Wheel instance which produces random events.
        :param table: (Table) the Table instance which holds bets to be
                              resolved.
        """
        self.wheel = wheel
        self.table = table
        self.player = None

    def cycle(self, player):
        """Execute a single cycle of play with a given Player.

        :param player: (Player) the individual Player that places bets,
                                receives winnings and pays losses.
        """
        if player.is_playing():
            player.place_bets()
            winning_bin = self.wheel.next()
            for bet in self.table:
                if bet.outcome in winning_bin:
                    player.win(bet)
                else:
                    player.lose(bet)
