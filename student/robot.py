print("STARTING ROBOT.PY")

from PiBot import PiBot
print("IMPORTED PIBOT")
import rospy
print("IMPORTED ROSPY")

# Create a robot instance

robot = PiBot()


left_enc_0 = 0
right_enc_0 = 0


def correction_start():
    left_enc_0 = robot.get_right_wheel_encoder()
    right_enc_0 = robot.get_left_wheel_encoder()


def correction():
    left_enc = robot.get_right_wheel_encoder() - left_enc_0
    right_enc = robot.get_left_wheel_encoder() - right_enc_0
    return (left_enc - right_enc) / 2  # / 10


# Get distance from object using the front middle IR sensor
mid_dist = robot.get_front_middle_laser()

goal = 0.18
base = 20


correction_start()
# Drive towards object
while mid_dist > 0.18:
    left_dist = robot.get_front_left_laser()
    right_dist = robot.get_front_right_laser()
    mid_dist = robot.get_front_middle_laser()

    s1 = 15
    s2 = 30
    d1 = 0.18
    d2 = 0.82
    cur_speed = ((s1 - s2) / (d1 - d2)) * mid_dist + ((s1 * d2 - s2 * d1) / (d2 - d1))

    diff = (left_dist - right_dist) * 50
    left_speed = int(max(min(base, cur_speed + diff), 0))
    right_speed = int(max(min(base, cur_speed - diff), 0))

    print("mid", mid_dist)
    print("diff", diff)
    print(left_speed, right_speed)

    robot.set_left_wheel_speed(left_speed)
    robot.set_right_wheel_speed(right_speed)

    rospy.sleep(0.001)

# Stop the robot when done
robot.set_wheels_speed(0)
print("Final distance", robot.get_front_middle_laser())
print("left:", robot.get_front_left_laser())
print("right:", robot.get_front_right_laser())

while mid_dist < 0.2546:
    mid_dist = robot.get_front_middle_laser()
    robot.set_left_wheel_speed(-20)
    robot.set_right_wheel_speed(20)

right_dist = robot.get_front_right_laser()
while right_dist < 0.2546:
    right_dist = robot.get_front_right_laser()
    robot.set_left_wheel_speed(-20)
    robot.set_right_wheel_speed(20)

robot.set_wheels_speed(0)
