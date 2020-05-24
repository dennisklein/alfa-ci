# PYTHON_ARGCOMPLETE_OK

import argcomplete
import argparse
import sys


class ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        self.print_help(sys.stderr)
        self.exit(2, '%s: error: %s\n' % (self.prog, message))


def print_shell_setup(args):
    """Print the argcomplete bash hook to be eval'ed by the user"""
    import subprocess
    print(
        subprocess.run(['register-python-argcomplete', 'alfa-ci'],
                       capture_output=True).stdout.decode('UTF-8'))


def print_version(args):
    """Print the package version defined in the setup.py metadata"""
    from alfaci.version import pkg_version
    print(pkg_version)


def main():
    """Main entry function called from the CLI"""
    parser = ArgumentParser(
        description='Manage alfa-ci environments.')
    subparsers = parser.add_subparsers(title='COMMANDS')

    shell_setup_parser = subparsers.add_parser(
        'shell-setup',
        add_help=False,
        help='run \'eval "$(alfa-ci shell-setup)"\' to enable shell completion'
        ', e.g. from your ~/.bashrc')
    shell_setup_parser.set_defaults(func=print_shell_setup)

    version_parser = subparsers.add_parser('version',
                                           add_help=False,
                                           help='show version number and exit')
    version_parser.set_defaults(func=print_version)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
        exit(0)
    else:
        parser.print_help()
        exit(2)

if __name__ == '__main__':
    main()
