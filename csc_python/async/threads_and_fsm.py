import heapq
import random
import sys
import time
from enum import Enum, auto
from threading import Thread


def random_delay() -> float:
    """Generate delay time."""
    return random.random() * 5


def random_countdown() -> int:
    """Generate countdown time."""
    return random.randrange(5)


def rockets() -> list:
    """Generate rockets with their parameters."""
    n = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(n)
    ]


def launch_rocket(delay: float, countdown: int):
    """Launch rockets sequentially."""
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        time.sleep(1)
    print("Rocket launched!")


def run_threads(rockets_list: list):
    """Launch rockets in parallel using threads."""
    threads = [
        Thread(target=launch_rocket, args=(d, c))
        for d, c in rockets_list
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# -------------------------------
# Finite State Machine approach
# -------------------------------


class State(Enum):
    """State constants."""
    WAITING = auto()
    COUNTING = auto()
    LAUNCHING = auto()


class Op(Enum):
    """Operation constants."""
    WAIT = auto()
    STOP = auto()


class Launch:
    """Launch class displaying current state of rocket."""
    def __init__(self, delay, countdown):
        self._state = State.WAITING
        self._delay = delay
        self._countdown = countdown

    def step(self):

        if self._state is State.WAITING:
            self._state = State.COUNTING
            return Op.WAIT, self._delay

        elif self._state is State.COUNTING:

            if self._countdown == 0:
                self._state = State.LAUNCHING

            else:
                print(f"{self._countdown}...")
                self._countdown -= 1
                return Op.WAIT, 1

        if self._state is State.LAUNCHING:
            print("Rocket launched!")
            return Op.STOP, None

        assert False, self._state


def now():
    """Return current time."""
    return time.time()


def run_fsm(rockets_list: list):
    """Launch rockets in parallel using heap."""
    start = now()
    work = [(start, i, Launch(d, c))
            for i, (d, c) in enumerate(rockets_list)]
    while work:
        (step_at, rocket_id, launch) = heapq.heappop(work)

        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)

        op, arg = launch.step()
        if op is Op.WAIT:
            step_at = now() + arg
            heapq.heappush(work, (step_at, rocket_id, launch))
        else:
            assert op is Op.STOP


if __name__ == '__main__':
    if sys.argv[1] == "threads":
        run_threads(rockets())
    else:
        assert sys.argv[1] == "fsm"
        run_fsm(rockets())
