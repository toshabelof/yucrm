from Constants import Compare


class InvalidCondition(Exception):
    def __init__(self, message=f"The passed condition does not satisfy the set of constants: {[e.name for e in Compare]}"):
        self.message = message
        super().__init__(self.message)

