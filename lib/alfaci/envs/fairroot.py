"""FairRoot environments"""

import sys
from alfaci.env import Env
from alfaci.containers import get_singularity_definition


class FairRootEnv(Env):
    """FairRoot environment"""
    def __init__(self, repo, name):
        """ctor"""
        self._name = name
        self._definition = get_singularity_definition(name)
        super().__init__(repo)

    @property
    def definition(self):
        """prop"""
        return self._definition

    @property
    def name(self):
        """prop"""
        return self._name

    def install(self):
        """install"""

    def __repr__(self):
        return 'fairroot %s (%s)' % (self.name, 'installed'
                                     if self.installed else 'not installed')


def get_envs(repo):  # pragma: no cover
    """Return the list of FairRoot envs"""
    if sys.platform.startswith('linux'):
        return [
            FairRootEnv(repo, name) for name in
            ['centos7', 'debian10', 'fedora31', 'opensuse15.2', 'ubuntu18.04']
        ]
    return []
