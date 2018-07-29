from .remote import Remote

class Gitlab(Remote):

    BASE_PATH = '/tree/master'
    GIT_PROTOCOL = 'git@gitlab.com:'
    HTTPS_PROTOCOL = 'https://gitlab.com/'

    @staticmethod
    def handles(remote):
        return (
            remote.startswith(Gitlab.GIT_PROTOCOL) or
            remote.startswith(Gitlab.HTTPS_PROTOCOL)
        )

    def __init__(self, remote):
        self.https_root = self._parse_https(remote)

    def repo_url(self):
        return self.https_root + self.BASE_PATH

    def _parse_https(self, remote):
        https = remote.replace(self.GIT_PROTOCOL, self.HTTPS_PROTOCOL, 1)
        return https.split('.git')[0]
