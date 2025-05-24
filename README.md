# Python sandpit

Just me poking about with some katas and things.

## Setup

```shell
poetry install
```

## Run tests

```
poetry run pytest
```

## Metrics

- [Codecov](https://app.codecov.io/gh/WillGibson/python-sandpit)
- [CodecovXX](https://app.codXXecov.io/gh/WillGibson/python-sandpit)

## Mutation testing

Using [mutmut](https://github.com/boxed/mutmut) as a tool to help identify gaps in our unit test coverage.

Every mutation that survives is a line of code that we can change without it being picked up by our unit tests.

To run the mutation tests:

```shell
poetry run mutmut run
```

The to review the mutants that survived:

```shell
poetry run mutmut browse
```
