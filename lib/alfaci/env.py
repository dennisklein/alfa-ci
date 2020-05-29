class Env:
    """environment base class"""
    def __init__(self, repo):
        self._repo = repo

    @property
    def repo(self):
        return self._repo

    @property
    def installed(self):
        return False

    def install(self):
        raise NotImplementedError('<override me>')

    def __repr__(self):
        return '<override me>'
