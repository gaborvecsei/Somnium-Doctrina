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
