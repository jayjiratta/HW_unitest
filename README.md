﻿# HackerRank Challenges Unit Tests

This repository contains unit tests for solving HackerRank challenges using Python. The tests are performed using the `nose2` framework for testing all modules at once with coverage analysis, and also using `python -m unittest` for testing individual test files.

## Challenges

1. [Funny String](https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true)
2. [Alternating Characters](https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true)
3. [Caesar Cipher 1](https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true)
4. [Two Characters](https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true)
5. [Grid Challenge](https://www.hackerrank.com/challenges/grid-challenge/problem?isFullScreen=true)

## Test Coverage

Below is the coverage report for the implemented functions:

| Name                              | Stmts | Miss | Cover |
|-----------------------------------|-------|------|-------|
| functions_def\alternative_char.py| 8     | 0    | 100%  |
| functions_def\caesar_cipher.py   | 10    | 0    | 100%  |
| functions_def\funny_or_not.py    | 22    | 0    | 100%  |
| functions_def\grid.py            | 18    | 0    | 100%  |
| functions_def\twochar.py         | 11    | 0    | 100%  |
| tests\test_al.py                 | 78    | 0    | 100%  |
| tests\test_caesar.py             | 75    | 0    | 100%  |
| tests\test_funny.py              | 58    | 0    | 100%  |
| tests\test_grid.py               | 73    | 0    | 100%  |
| tests\test_twochar.py            | 168   | 0    | 100%  |
| TOTAL                            | 521   | 0    | 100%  |


## Usage

### Running all tests with coverage analysis

To run all tests and generate coverage analysis, use `nose2` with coverage:

```bash
nose2 -v --with-coverage

python -m unittest -v .\tests\test_[filename].py
