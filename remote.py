import re

class Remote:

    def __init__(self, remote):
        self.remote = remote

    def repo_url(self, branch):
        return self._add_path(self._remove_dot_git(self._parse_https(self.remote)), branch)

    def _parse_https(self, remote):
        match = re.search('^git@(.*?):', remote)
        if match:
            to_replace = match.group(0)
            domain = 'https://{}/'.format(match.group(1))
            remote = remote.replace(to_replace, domain)

        return remote

    def _remove_dot_git(self, url):
        if url.endswith('.git'):
            return url[:-len('.git')]
        return url

    def _add_path(self, url, branch):
        return '{}/tree/{}'.format(url, branch)
