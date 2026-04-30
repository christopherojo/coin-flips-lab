# coin-flip-lab

A clean, minimal Python project for fast coin-flip simulations and pattern
detection experiments.

The initial experiment simulates many sequences of coin flips and searches for
specific length-10 streak patterns, including overlapping matches. Flip
generation and pattern matching use vectorized numpy operations for performance.

## Requirements

- Python 3.10+
- numpy

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Run the example experiment:

```bash
python main.py
```

The example searches for these patterns across 10 simulations of 1,000,000
flips each:

- `HHHHHHHHHH`
- `TTTTTTTTTT`
- `HTHTHTHTHT`
- `HHTTHHTTHH`

For each pattern, the output reports total matches, how many simulations saw at
least one match, where the first match appeared, per-simulation counts, and the
estimated probability of seeing the pattern in a simulation.
