from random import randint as r

class Pew():

    def __init__(self):
        
        self.chamber = ["safe","safe", "safe", "safe", "safe", "BANG"]
        self.trigger_pulled = 0
        self.status = True

        self.spin()
        

    def spin(self):
        chamber_settings = ["safe","safe", "safe", "safe", "safe", "safe"]

        bullet_pos = r(0,5)

        chamber_settings.pop(bullet_pos)
        chamber_settings.insert(bullet_pos, "BANG")

        self.chamber = chamber_settings

    def check_chamber(self):

        return self.chamber[self.trigger_pulled]

    def pull_trigger(self):
        
        if self.status:
            result = self.check_chamber()

            if result == "BANG":
                self.status = False

            self.trigger_pulled += 1

            return result
        return "BANG"
        

    
    def reset(self):

        self.spin()

        self.trigger_pulled = 0
        self.status = True
