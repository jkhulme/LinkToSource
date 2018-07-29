class Remote:

    @staticmethod
    def handles(remote):
        raise NotImplementedError

    def __init__(self, remote):
        raise NotImplementedError

    def repo_url(self):
        raise NotImplementedError
