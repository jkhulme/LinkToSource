from .repositories.github import Github
from .repositories.gitlab import Gitlab

class RemoteFactory:

    repos = [Github, Gitlab]

    def __new__(self, remote):
        for repo in self.repos:
            if repo.handles(remote):
                return repo(remote)
        raise NotImplementedError('No handler for remote {}'.format(remote))
