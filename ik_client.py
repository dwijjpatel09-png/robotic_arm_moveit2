import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from moveit_commander import MoveGroupCommander

class IKClient(Node):

    def __init__(self):
        super().__init__('ik_client')

        self.arm = MoveGroupCommander("arm")

        self.target_pose = Pose()
        self.target_pose.position.x = 0.4
        self.target_pose.position.y = 0.2
        self.target_pose.position.z = 0.3

        self.move_to_target()

    def move_to_target(self):

        self.arm.set_pose_target(self.target_pose)

        plan = self.arm.go(wait=True)

        self.arm.stop()
        self.arm.clear_pose_targets()

        self.get_logger().info("Reached Target Successfully")

def main():
    rclpy.init()
    node = IKClient()
    rclpy.spin(node)

if __name__ == "__main__":
    main()
