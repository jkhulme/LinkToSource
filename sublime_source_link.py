import sublime
import sublime_plugin
import subprocess
import re
from .remote_factory import RemoteFactory

class SublimeSourceLinkCommand(sublime_plugin.TextCommand):
    root = ''
    repo_url = ''
    cwd = ''

    def run(self, edit):
        self.cwd = self._cwd()
        self.root = self._project_root()
        self.repo_url = self._repo_url()
        sublime.set_clipboard(self._link())

    def _link(self):
        return '{}{}'.format(self.repo_url, self._relative_path())

    def _relative_path(self):
        path_to_file = self.view.file_name()
        return path_to_file.replace(self.root, '', 1)

    def _cwd(self):
        return '/'.join(self.view.file_name().split('/')[:-1])

    def _repo_url(self):
        return RemoteFactory(self._remote_origin()).repo_url()

    def _project_root(self):
        git_root_directory = ['rev-parse', '--show-toplevel']
        return self._git_command(git_root_directory)

    def _remote_origin(self):
        git_remote_origin = ['config', '--get', 'remote.origin.url']
        return self._git_command(git_remote_origin)

    def _git_command(self, command):
        git_command = ['git', '-C', self.cwd] + command
        return subprocess.check_output(git_command).strip().decode('utf-8')
