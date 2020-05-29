def test_env(mock_env):
    assert not mock_env.installed
    assert mock_env.repo


def test_fairroot_env(mock_fairroot_env):
    assert mock_fairroot_env.name == 'fedora31'
    assert mock_fairroot_env.definition
    mock_fairroot_env.install()
