from moveit_commander import MoveGroupCommander

class TrajectoryPlanner:

    def __init__(self):
        self.arm = MoveGroupCommander("arm")

    def go_to_point(self, x, y, z):

        pose = self.arm.get_current_pose().pose
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z

        self.arm.set_pose_target(pose)

        plan = self.arm.plan()
        self.arm.execute(plan[1], wait=True)

        self.arm.stop()
        self.arm.clear_pose_targets()
