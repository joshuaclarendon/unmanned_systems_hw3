"""Robot2D is supplied from the completed lesson. Implement MountedSensor."""
import numpy as np
from numpy.typing import ArrayLike, NDArray
from rotations import rotation_matrix

class Robot2D:
    def __init__(self, x: float = 0.0, y: float = 0.0, yaw: float = 0.0) -> None:
        self.x, self.y, self.yaw = float(x), float(y), float(yaw)
    def robot_world_pos(self) -> ArrayLike:
        return np.cos


    def move(self, forward_speed: float, yaw_rate: float, dt: float) -> None:
        if not np.isfinite(dt) or dt <= 0:
            raise ValueError("dt must be finite and positive")
        velocity = rotation_matrix(self.yaw) @ np.array([forward_speed, 0.0])
        self.x += velocity[0] * dt
        self.y += velocity[1] * dt
        self.yaw += yaw_rate * dt

class MountedSensor:
    def __init__(self, robot: Robot2D, offset_body: ArrayLike, yaw_body: float) -> None:
        # Defines sensors position in the robot's reference frame.
        x_offset = offset_body[0]
        y_offset = offset_body[1]
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.yaw_offset = yaw_body
        # Stores robot class in MountedSensor class
        self.robot_mount = robot


    def to_world(self, point_sensor: ArrayLike) -> NDArray[np.float64]:
        """Return a shape-(2,) NumPy world point without changing the input."""
        # Extract robot object and position.
        robot = self.robot_mount
        robot_world_x = robot.x
        robot_world_y = robot.y
        robot_world_yaw = robot.yaw
        
        # Calculate the SE3 matrix for the robot reference frame in terms of the 
        # world reference frame.
        R_world_robot = rotation_matrix(robot_world_yaw,robot_world_x,robot_world_y)
        
        # Calculate the SE3 matrix for the sensor reference frame in terms of the 
        # robot reference frame.
        R_robot_sensor = rotation_matrix(self.yaw_offset, self.x_offset, self.y_offset)
        
        # Calculate the SE3 matrix for the sensor reference frame in terms of the 
        # world reference frame by multiplying the world->robot SE3 matrix with the
        # robot -> sensor SE3 matrix.
        R_world_sensor = R_world_robot @ R_robot_sensor
        
        # Use the resulting world->sensor SE3 matrix to find the position of the
        # sensed point in terms of the world reference frame.
        point_world = R_world_sensor @ np.append(point_sensor,1)
        return point_world[0:2]
        
        
