import heapq
import random
import time
from enum import Enum, auto


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


def sleep(delay):
    """Yield waiting state and its duration."""
    yield Op.WAIT, delay


def launch_rocket(delay: float, countdown: int):
    """Rocket launch state machine."""
    yield from sleep(delay)  # STATE WAITING
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        yield from sleep(1)  # STATE COUNTING
    print("Rocket launched!")  # STATE LAUNCHING


class Op(Enum):
    """Operation constants."""
    WAIT = auto()
    STOP = auto()


def now():
    """Return current time."""
    return time.time()


def run_fsm(rockets_list: list):
    """Launch rockets in parallel using heap."""
    start = now()
    work = [(start, i, launch_rocket(d, c))
            for i, (d, c) in enumerate(rockets_list)]
    while work:
        (step_at, rocket_id, launch) = heapq.heappop(work)

        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)

        try:
            op, arg = launch.send(None)
        except StopIteration:
            continue

        if op is Op.WAIT:
            step_at = now() + arg
            heapq.heappush(work, (step_at, rocket_id, launch))
        else:
            assert False, op


if __name__ == '__main__':
    run_fsm(rockets())
