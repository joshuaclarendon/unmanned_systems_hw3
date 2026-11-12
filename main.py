"""Provided driver for Problem 1(c)-(d). Implement MountedSensor in models.py."""
from pathlib import Path
import numpy as np
from numpy.typing import NDArray
from models import Robot2D, MountedSensor

EXPECTED = np.array([2.0, 2.932050808])

def calculate_world_point() -> NDArray[np.float64]:
    robot = Robot2D(3.0, 1.0, np.deg2rad(90))
    sensor = MountedSensor(robot, [0.2, 0.0], np.deg2rad(30))
    return sensor.to_world(np.array([2.0, 0.0]))

def main() -> None:
    world_point = calculate_world_point()
    matches = bool(np.allclose(world_point, EXPECTED, atol=1e-6, rtol=0))
    report = (
        "Problem 1(c)-(d): sensor point in world coordinates\n"
        f"Python result (m): {np.array2string(world_point, precision=9)}\n"
        f"Expected (m): {np.array2string(EXPECTED, precision=9)}\n"
        "Comparison: atol=1e-6 m, rtol=0\n"
        f"Matches expected: {matches}\n"
    )
    print(report, end="")
    output = Path("outputs")
    output.mkdir(exist_ok=True)
    (output / "comparison.txt").write_text(report)
    if not matches:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
