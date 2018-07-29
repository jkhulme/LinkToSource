from .github import Github

class RemoteFactory:

    repos = [Github]

    def __new__(self, remote):
        for repo in self.repos:
            if repo.handles(remote):
                return repo(remote)
        raise NotImplementedError('No handler for remote {}'.format(remote))
