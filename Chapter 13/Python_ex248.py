class PublicPrivateExample:
    def __init__(self):
        self.public = 'safe'
        self._unsafe = 'unsafe'
    def public_method(self):
        # It can be used without problems
        pass
    def _unsafe_method(self):
        # This method should not be used
        pass
        self.public = 'safe'
        self. _unsafe = 'unsafe'
