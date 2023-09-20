class InvalidBodyException(Exception):

    def __init__(self, message="Invalid request body"):
        self.message = message
        super().__init__(self.message)
