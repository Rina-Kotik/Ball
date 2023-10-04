from ball import degree
import pytest

test_ball = (
    (10.0, 9.8, 2.0, 0.0, 62.97),
    (14.0, 9.8, 3.5, 5.0, 79.76), 
    (8.0, 9.8, 5.5, 2.0, 87.12),
)
@pytest.mark.parametrize('radius, acceleration, time, velocity, expected', test_ball)
def test_ball(radius: float, acceleration: float, time: float, velocity: float, expected: int) -> None:
    """Test a degree function using assertion.

    Args: 
        radius: the radius of the ball, 
        acceleration: acceleration of free fall, is a constant == 9.8, 
        time: the time of the ball movement , 
        velocity: the velocity of the ball.
        expected: expected result of a degree function.
    """
    assert degree(radius, acceleration, time, velocity) == expected
