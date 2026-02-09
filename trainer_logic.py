class Trainer:
    def __init__(self, data):
        self.data = data
        self.current = None

    def next(self):
        import random
        self.current = random.choice(self.data)
        return self.current["question"]

    def check(self, user_input):
        correct = self.current["answer"]
        return user_input.strip() == correct, correct
