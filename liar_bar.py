import six_shooter

class Bar():

    def __init__(self, num_players = 4, p1 = "Player 1",p2 = "Player 2",p3 = "Player 3",p4 = "Player 4"):

        self.num_players = num_players

        self.p1_name = p1
        self.p2_name = p2
        self.p3_name = p3
        self.p4_name = p4

        self.players = [self.p1_name, self.p2_name, self.p3_name, self.p4_name]

        self.p1_pew = six_shooter.Pew()
        self.p2_pew = six_shooter.Pew()
        self.p3_pew = six_shooter.Pew()
        self.p4_pew = six_shooter.Pew()

        self.pews = [self.p1_pew, self.p2_pew, self.p3_pew, self.p4_pew]

        self.reset()

    def reset(self):
        for pew in self.pews:
            pew.reset()