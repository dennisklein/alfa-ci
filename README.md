# `alfa-ci` environment manager  ![Test](https://github.com/FairRootGroup/alfa-ci/workflows/Test/badge.svg?event=push) [![codecov](https://codecov.io/gh/FairRootGroup/alfa-ci/branch/master/graph/badge.svg)](https://codecov.io/gh/FairRootGroup/alfa-ci)

requires Python 3.6+

## install

latest release
```bash
python -m pip install --user alfa-ci
```

HEAD without git clone
```bash
python -m pip install --user git+https://github.com/FairRootGroup/alfa-ci
```

for development in git clone:
```bash
python -m pip install --user -e .
```

## usage

setup shell completion (optional)
```bash
eval "$(alfa-ci shell-setup)"
```

learn about subcommands
```bash
alfa-ci -h
```

## run unit tests

quick
```bash
python -m pip install --user pytest cli-test-helpers
python -m pytest -v
```

with coverage report
```bash
python -m pip install --user pytest coverage cli-test-helpers
python -m coverage run -m pytest && python -m coverage report -m
```

exhaustive
```bash
python -m pip install --user tox
python -m tox
```
