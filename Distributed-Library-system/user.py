class user(object):
    def __init__(self, user_name):
        self.user_name = user_name
        #history stores the users loan history
        self.history = []