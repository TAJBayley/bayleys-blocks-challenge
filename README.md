# Bayley's Blocks Challenge

![](assets/feature_graphic.png)

[Bayley's Blocks](https://bayleysblocks.com) is a web and mobile puzzle game with daily shareable challenges. This repository provides code to generate a set of puzzles and a template function to solve them using a brute force method.

The challenge is to replace the brute force method with a more efficient one. The template provides a way to measure the efficacy of any method by calculating the number of cycles using the [hwcounter](https://pypi.org/project/hwcounter/) library and the elapsed time.

---

## Setup

On Unix or MacOS, using the bash shell

```shell
$ source venv/bin/activate
```

Installing required packages

```shell
$ pip install -r requirements.txt
```

## Run

To run:

```shell
$ python3 main.py
```

## Adding Improved Method

The brute force method is located in `solver.py` and is implemented in the function `solve_puzzle()`. Replace `brute_force_method()` with your improved implementation making sure to pass in a deep copy of the puzzle.
