"""Linux containers"""

from textwrap import dedent, indent

_COMMON_PKGS = [
    'autoconf', 'automake', 'bison', 'binutils', 'bzip2', 'ca-certificates',
    'cmake', 'cmake-data', 'curl', 'elfutils', 'flex', 'hostname', 'git',
    'gzip', 'libtool', 'make', 'patch', 'sed', 'subversion', 'tar', 'unzip',
    'wget'
]

CONTAINER_DATA = {
    'centos7': {
        'bootstrap': 'docker',
        'from': 'centos:7',
        'packages': _COMMON_PKGS + [
            'gcc', 'gcc-c++', 'gcc-gfortran', 'glibc-devel', 'python2-devel',
            'pkgconf', 'procps', 'redhat-lsb-core', 'which', 'xz'
        ],
        'install': dedent("""\
            yum -y update
            yum -y install {packages}
            yum -y clean all
            """)
    },
    'debian10': {
        'bootstrap': 'docker',
        'from': 'debian:10',
        'packages': _COMMON_PKGS + [
            'build-essential', 'debianutils', 'g++', 'gcc', 'gfortran'
            'libc6-dev', 'lsb-release', 'python-dev', 'xz-utils'
        ],
        'install': dedent("""\
            apt-get update
            apt-get -y upgrade
            apt-get -y install {packages}
            apt-get -y clean
            """)
    },
    'fedora31': {
        'bootstrap': 'docker',
        'from': 'fedora:31',
        'packages': _COMMON_PKGS + [
            'gcc', 'gcc-c++', 'gcc-gfortran', 'glibc-devel', 'python2-devel',
            'pkgconf', 'procps', 'redhat-lsb-core', 'which', 'xz'
        ],
        'install': dedent("""\
            dnf -y update
            dnf -y install {packages}
            dnf -y clean all
            """)
    },
    'opensuse15.2': {
        'bootstrap': 'docker',
        'from': 'opensuse/leap:15.2',
        'packages': _COMMON_PKGS + [
            'gcc', 'gcc-c++', 'gcc-gfortran', 'glibc-devel', 'python2-devel',
            'pkgconf', 'procps', 'lsb-release', 'which', 'xz'
        ],
        'install': dedent("""\
            zypper refresh
            zypper update -y
            zypper install -y --no-recommends {packages}
            zypper clean
            """)
    },
    'ubuntu18.04': {
        'bootstrap': 'docker',
        'from': 'ubuntu:18.04',
        'packages': _COMMON_PKGS + [
            'build-essential', 'debianutils', 'g++', 'gcc', 'gfortran'
            'libc6-dev', 'lsb-release', 'python-dev', 'xz-utils'
        ],
        'install': dedent("""\
            apt-get update
            apt-get -y upgrade
            apt-get -y install {packages}
            apt-get -y clean
            """)
    }
}

CONTAINER_DEF = """\
Bootstrap: {bootstrap}
From: {from}

%post
{install}
"""


def get_singularity_definition(name):
    """Generate a singularity container definition"""
    data = CONTAINER_DATA[name]
    data['packages'] = ' '.join(data['packages'])
    data['install'] = indent(data['install'].format(**data), '    ')
    return CONTAINER_DEF.format(**data)
