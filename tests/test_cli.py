import pytest
from cli_test_helpers import ArgvContext
import alfaci
import alfaci.cli
import alfaci.version

CMD = 'alfa-ci'


def test_shell_setup():
    with ArgvContext(CMD, 'shell-setup'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 0


def test_version(capsys):
    with ArgvContext(CMD, 'version'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == alfaci.version.PKG_VERSION
    assert rc.value.code == 0


def test_no_subcmd():
    with ArgvContext(CMD), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 2


def test_unknown_option():
    with ArgvContext(CMD, '--foobar'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 2


@pytest.mark.usefixtures('mock_init_repo')
def test_init(capsys, mock_cwd):
    with ArgvContext(CMD, 'init'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    captured = capsys.readouterr().out.strip()
    loc = mock_cwd / '.alfa-ci'
    expected = 'Initialized empty alfa-ci repository in %s' % loc
    assert captured == expected
    assert rc.value.code == 0


@pytest.mark.usefixtures('mock_cwd', 'mock_repo')
def test_list(capsys):
    with ArgvContext(CMD, 'list'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    captured = capsys.readouterr().out
    actual = len(captured.splitlines())
    assert actual == 6
    assert rc.value.code == 0


@pytest.mark.usefixtures('mock_cwd', 'mock_repo')
def test_install():
    with ArgvContext(CMD, 'install'), pytest.raises(SystemExit) as rc:
        alfaci.cli.main()
    assert rc.value.code == 0
