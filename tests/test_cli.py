import pytest
from cli_test_helpers import ArgvContext
import alfaci
import alfaci.cli
import alfaci.version

cmd = 'alfa-ci'


def test_shell_setup():
    with ArgvContext(cmd, 'shell-setup'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 0


def test_version(capsys):
    with ArgvContext(cmd, 'version'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == alfaci.version.PKG_VERSION
    assert rc.value.code == 0


def test_no_subcmd():
    with ArgvContext(cmd), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 2


def test_unknown_option():
    with ArgvContext(cmd, '--foobar'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 2


class MockRepo:
    def __init__(self, path):
        self._location = path / '.alfa-ci'

    @property
    def location(self):
        return self._location


@pytest.fixture
def mock_init_repo(monkeypatch):
    """alfaci.repo.init_repo() mocked to return MockRepo"""
    monkeypatch.setattr(alfaci.cli, "init_repo", lambda path: MockRepo(path))


@pytest.fixture
def mock_cwd(tmp_path, monkeypatch):
    """cwd mocked to tmp dir"""
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_init(capsys, mock_cwd, mock_init_repo):
    with ArgvContext(cmd, 'init'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    captured = capsys.readouterr().out.strip()
    loc = mock_cwd / '.alfa-ci'
    expected = 'Initialized empty alfa-ci repository in %s' % loc
    assert captured == expected
    assert rc.value.code == 0
