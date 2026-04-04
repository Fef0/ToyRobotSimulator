# ToyRobotSimulator
A Toy Robot Simulator

## How to run

```bash
python main.py
```

# How to provide input and where to expect output

Input is expected to be in `data/input.txt` and output will be in `data/output.txt`.
Logs are expected to be in `logs/log.log`.

## Valid commands in input file

```
PLACE x,y,direction
MOVE
LEFT
RIGHT
REPORT
```

# Valid directions in PLACE command

```
NORTH
SOUTH
EAST
WEST
```

## Output format

```
x,y,direction
```

## Unit Tests

```bash
pytest
```
