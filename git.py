def root_directory():
    git_root_directory = ['rev-parse', '--show-toplevel']
    return _git_command(git_root_directory)

def remote_raw():
    git_remote_origin = ['config', '--get', 'remote.origin.url']
    return _git_command(git_remote_origin)

def _git_command(command):
    git_command = ['git', '-C', self.cwd] + command
    return subprocess.check_output(git_command).strip().decode('utf-8')
