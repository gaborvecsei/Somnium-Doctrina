# Somnium Doctrina - Learning in Dreams

In this repo we will try to teach an abstract representation of the world (we referr to this as the *dream*) to our agent and then
try to make it learn inside the dream.

## Grund integration and minimal documentation

The environment, which we are trying to learn is Match from grund.

To access it, grund has to be installed:

```
pip install https://github.com/csxeba/grund
```

A minimally configured Match environment can be set up and used to produce random states and rewards:

```python
import cv2
from grund.match import MatchConfig, Match

cfg = MatchConfig(
    canvas_size=[240, 180],
    players_per_side=3
)

env = Match(cfg)

for states, rewards in (env.random_state(batch_size=32) for _ in range(10)):
    for state, reward in zip(states, rewards):
        cv2.imshow("States", state)
        cv2.waitKey(100)
```
