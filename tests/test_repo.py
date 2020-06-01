import sys
import pytest
from alfaci.repo import init_repo, Repo, Error


def test_load(empty_initialized_repo):
    Repo(empty_initialized_repo)


def test_load_unitialized(tmp_path):
    with pytest.raises(Error):
        Repo(tmp_path)


@pytest.mark.usefixtures('mock_subprocess_call')
def test_init_repo(tmp_path):
    init_repo(tmp_path)


def test_init_repo_existing(empty_initialized_repo):
    with pytest.raises(Error):
        init_repo(empty_initialized_repo)


def test_location(empty_initialized_repo):
    assert Repo(empty_initialized_repo).location == (empty_initialized_repo /
                                                     Repo.repo_dir)


def test_envs(empty_initialized_repo):
    if sys.platform.startswith('linux'):
        assert len(Repo(empty_initialized_repo).envs) == 5
    else:
        assert Repo(empty_initialized_repo).envs == []
