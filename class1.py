class Hello:
    def __init__(self, str):
        self.str = str

class Salam(Hello):
    def __init__(self, str):
        Hello.__init__(self, str)

    def tprint(self):
        pass