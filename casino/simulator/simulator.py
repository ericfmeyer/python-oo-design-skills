"""Implements the Simulator class."""


class Simulator(object):
    """The Simulator class will simulate playing strategies.

    Responsibilities include:
        - create the Game, Table and Wheel
        - simulate 100 sessions
        - save the maximum stack and length of each session
        - for each session, initialize the Player and Game, cycle the game
          a number of times, collect the size of the Player's stake after
          each cycle
        - write a final summary of results
    """

    NUMBER_OF_SESSIONS = 100

    def __init__(self, game, player):
        """Instance of a game simulation.

        :param game: (Game) the game to simulate
        :param player: (Player) the player

        Class members:
            - init_duration: (int) value used to initialize the number of
                                   cycles a player go through
            - init_stake:    (int) stake value used to initialize the player's
                                   stake
            - samples:       (int) number of games to simulate
            - durations:     (list) durations of each session
            - maxima:        (list) maximum stake at the end of each session
            - player:      (Player) the player / betting strategy
            - game:          (Game) the casino game being simulated
        """
        self.init_duration = 250
        self.init_stake = 100
        self.samples = 50

        self.durations = list()
        self.maxima = list()

        self.player = player
        self.game = game

    def session(self):
        """Return the list of the player's stake values from a game session."""
        self.player.set_stake(self.init_stake)
        self.player.set_rounds(self.init_duration)

        stake_values = list()
        while self.player.is_playing():
            self.game.cycle(self.player)
            stake_values.append(self.player.stake)
        return stake_values

    def gather(self):
        """Run through all the samples of the simulation.

        It gathers the maximum and the length of the stake values of each
        player's session.
        """
        for n in range(self.samples):
            print("Round #{}".format(n))
            session_result = self.session()
            self.maxima.append(max(session_result))
            self.durations.append(len(session_result))

