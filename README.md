# `alfa-ci` environment manager

## install

latest release
```bash
pip install --user alfa-ci
```

for development in git clone:
```bash
pip install --user -e .
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
pip install --user pytest
pytest
```

exhaustive
```bash
pip install --user tox
tox
```
