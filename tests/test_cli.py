from cli_test_helpers import ArgvContext
from alfaci import cli, version
import pytest


def test_shell_setup():
    with ArgvContext('alfa-ci', 'shell-setup'):
        with pytest.raises(SystemExit) as rc:
            cli.main()
            assert rc.value.code == 0


def test_version(capsys):
    with ArgvContext('alfa-ci', 'version'):
        with pytest.raises(SystemExit) as rc:
            cli.main()
            captured = capsys.readouterr()
            assert captured.out.strip() == version.pkg_version
            assert rc.value.code == 0


def test_no_subcmd(capsys):
    with ArgvContext('alfa-ci'):
        with pytest.raises(SystemExit) as rc:
            cli.main()
            assert rc.value.code == 0


def test_unknown_option(capsys):
    with ArgvContext('alfa-ci', '--foobar'):
        with pytest.raises(SystemExit) as rc:
            cli.main()
            assert rc.value.code == 2
