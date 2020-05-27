"""alfaci.cli test module"""

import pytest
from cli_test_helpers import ArgvContext
import alfaci
import alfaci.cli
import alfaci.version

CMD = 'alfa-ci'


def test_shell_setup():
    """Check the return code of shell-setup subcmd"""
    with ArgvContext(CMD, 'shell-setup'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 0


def test_version(capsys):
    """Check the return code and output of version subcmd"""
    with ArgvContext(CMD, 'version'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == alfaci.version.PKG_VERSION
    assert rc.value.code == 0


def test_no_subcmd():
    """Check the return code when no subcmd given"""
    with ArgvContext(CMD), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 2


def test_unknown_option():
    """Check the return code when unknown option given"""
    with ArgvContext(CMD, '--foobar'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 2


class MockEnv:
    """Mock-up for alfaci.env"""
    def install(self):
        pass


class MockRepo:
    """Mock-up for alfaci.repo.Repo"""
    def __init__(self, path):
        self._location = path / '.alfa-ci'
        self._envs = [MockEnv(), MockEnv()]

    @property
    def location(self):
        """prop"""
        return self._location

    @property
    def envs(self):
        """prop"""
        return self._envs


@pytest.fixture
def mock_init_repo(monkeypatch):
    """alfaci.repo.init_repo() mocked to return MockRepo"""
    monkeypatch.setattr(alfaci.cli, "init_repo", lambda path: MockRepo(path))


@pytest.fixture
def mock_repo(monkeypatch):
    """alfaci.repo.Repo mocked by MockRepo"""
    monkeypatch.setattr(alfaci.cli, "Repo", MockRepo)


@pytest.fixture
def mock_cwd(tmp_path, monkeypatch):
    """cwd mocked to tmp dir"""
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_init(capsys, mock_cwd, mock_init_repo):
    """Check output and return code of init subcmd"""
    with ArgvContext(CMD, 'init'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    captured = capsys.readouterr().out.strip()
    loc = mock_cwd / '.alfa-ci'
    expected = 'Initialized empty alfa-ci repository in %s' % loc
    assert captured == expected
    assert rc.value.code == 0


def test_list(capsys, mock_cwd, mock_repo):
    """Check output and return code of list subcmd"""
    with ArgvContext(CMD, 'list'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    captured = capsys.readouterr().out
    actual = len(captured.splitlines())
    assert actual == 2
    assert rc.value.code == 0


def test_install(mock_cwd, mock_repo):
    """Check return code of install subcmd"""
    with ArgvContext(CMD, 'install'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 0
