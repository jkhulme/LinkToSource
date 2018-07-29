from .remote import Remote

class Github(Remote):

    BASE_PATH = '/tree/master'
    GIT_PROTOCOL = 'git@github.com:'
    HTTPS_PROTOCOL = 'https://github.com/'

    @staticmethod
    def handles(remote):
        return (
            remote.startswith(Github.GIT_PROTOCOL) or
            remote.startswith(Github.HTTPS_PROTOCOL)
        )

    def __init__(self, remote):
        self.https_root = self._parse_https(remote)

    def repo_url(self):
        return self.https_root + self.BASE_PATH

    def _parse_https(self, remote):
        https = remote.replace(self.GIT_PROTOCOL, self.HTTPS_PROTOCOL, 1)
        return https.split('.git')[0]
