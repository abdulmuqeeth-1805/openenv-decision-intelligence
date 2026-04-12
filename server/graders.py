class EasyGrader:
    def __init__(self):
        pass

    def grade(self, action, state):
        return {"score": 0.8, "reward": 0.8}

class MediumGrader:
    def __init__(self):
        pass

    def grade(self, action, state):
        return {"score": 0.6, "reward": 0.6}

class HardGrader:
    def __init__(self):
        pass

    def grade(self, action, state):
        return {"score": 0.4, "reward": 0.4}