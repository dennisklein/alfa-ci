"""FairRoot environments"""

import sys
from alfaci.env import Env


class FairRootEnv(Env):
    """FairRoot environment"""
    def __init__(self, repo, name):
        """ctor"""
        self._name = name
        super().__init__(repo)

    @property
    def name(self):
        """getter"""
        return self._name

    def install(self):
        """install"""

    def __repr__(self):
        return 'fairroot %s (%s)' % (self.name, 'installed'
                                     if self.installed else 'not installed')


def get_envs(repo):  # pragma: no cover
    """Return the list of FairRoot envs"""
    if sys.platform.startswith('linux'):
        return [FairRootEnv(repo, 'debian10'), FairRootEnv(repo, 'fedora31')]
    return []
