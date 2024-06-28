#!/usr/bin/env python

import sys
import copy
import rospy
import random
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import os
import csv
import numpy as np
from math import pi
from six.moves import input
from std_msgs.msg import String
from tf.transformations import quaternion_from_euler
from moveit_commander.conversions import pose_to_list

def all_close(goal, actual, tolerance):
  """
  Convenience method for testing if a list of values are within a tolerance of their counterparts in another list
  @param: goal       A list of floats, a Pose or a PoseStamped
  @param: actual     A list of floats, a Pose or a PoseStamped
  @param: tolerance  A float
  @returns: bool
  """
  all_equal = True
  if type(goal) is list:
    for index in range(len(goal)):
      if abs(actual[index] - goal[index]) > tolerance:
        return False

  elif type(goal) is geometry_msgs.msg.PoseStamped:
    return all_close(goal.pose, actual.pose, tolerance)

  elif type(goal) is geometry_msgs.msg.Pose:
    return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

  return True

class DiscoveryDaysRoboticInterface(object):
  """DiscoveryDaysRoboticInterface"""
  def __init__(self):
    super(DiscoveryDaysRoboticInterface, self).__init__()
    ## BEGIN_SUB_INTERFACE setup
    ##
    ## First initialize `moveit_commander`_ and a `rospy`_ node:
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('moveit_python_interface')

    ## Get the name of the robot - this will be used to properly define the end-effector link when adding a box
    self.robot_model = rospy.get_param("~robot_model")
    self.robot_name = rospy.get_namespace().strip("/")
    self.ee_link_offset = rospy.get_param("~ee_link_offset")
    self.joint_goal = rospy.get_param("~joint_goal")
    pose_goal_raw = rospy.get_param("~pose_goal")
    quat = quaternion_from_euler(pose_goal_raw[3], pose_goal_raw[4], pose_goal_raw[5])
    self.pose_goal = geometry_msgs.msg.Pose()
    self.pose_goal.position.x = pose_goal_raw[0]
    self.pose_goal.position.y = pose_goal_raw[1]
    self.pose_goal.position.z = pose_goal_raw[2]
    self.pose_goal.orientation.x = quat[0]
    self.pose_goal.orientation.y = quat[1]
    self.pose_goal.orientation.z = quat[2]
    self.pose_goal.orientation.w = quat[3]

    ## Instantiate a `RobotCommander`_ object. This object is the outer-level interface to
    ## the robot:
    self.robot = moveit_commander.RobotCommander()

    ## Instantiate a `PlanningSceneInterface`_ object.  This object is an interface
    ## to the world surrounding the robot:
    self.scene = moveit_commander.PlanningSceneInterface()

    ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
    ## to one group of joints.  In this case the group is the joints in the Interbotix
    ## arm so we set ``group_name = interbotix_arm``. If you are using a different robot,
    ## you should change this value to the name of your robot arm planning group.
    ## This interface can be used to plan and execute motions on the Interbotix Arm:
    group_name = "interbotix_arm"
    self.group = moveit_commander.MoveGroupCommander(group_name)

    ## We create a `DisplayTrajectory`_ publisher which is used later to publish
    ## trajectories for RViz to visualize:
    self.display_trajectory_publisher = rospy.Publisher("move_group/display_planned_path",
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)
    '''
    ## Getting Basic Information
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^
    # We can get the name of the reference frame for this robot:
    self.planning_frame = self.group.get_planning_frame()
    print("============ Reference frame: %s" % self.planning_frame)

    # We can also print the name of the end-effector link for this group:
    self.eef_link = self.group.get_end_effector_link()
    print("============ End effector: %s" % self.eef_link)

    # We can get a list of all the groups in the robot:
    self.group_names = self.robot.get_group_names()
    print("============ Robot Groups: " + str(self.group_names))
    '''

    # Sometimes for debugging it is useful to print the entire state of the
    # robot:
    print("============ Printing robot state")
    print(self.robot.get_current_state())
    print("")

  def go_to_joint_state(self):
    ## Planning to a Joint Goal
    ## ^^^^^^^^^^^^^^^^^^^^^^^^

    print("============ Printing Joint Goal: " + str(self.joint_goal))

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    self.group.go(self.joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    self.group.stop()

    current_joints = self.group.get_current_joint_values()
    return all_close(self.joint_goal, current_joints, 0.01)

  def go_to_pose_goal(self):
    ## Planning to a Pose Goal
    ## ^^^^^^^^^^^^^^^^^^^^^^^
    ## We can plan a motion for this group to a desired pose for the
    ## end-effector:

    print("============ Printing Pose Goal:\n" + str(self.pose_goal))
    self.group.set_pose_target(self.pose_goal)

    ## Now, we call the planner to compute the plan and execute it.
    plan = self.group.go(wait=True)
    # Calling `stop()` ensures that there is no residual movement
    self.group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    self.group.clear_pose_targets()

    current_pose = self.group.get_current_pose().pose
    return all_close(self.pose_goal, current_pose, 0.01)

  def plan_absolute_path(self, pose_data, raise_from_base = True, mirror_return = True):
    ## You can plan a Cartesian path directly by specifying a list of waypoints
    ## for the end-effector to go through:
    ##
    ## Input: pose_data is an array of size (n,7), first 3 are xyz position, last 4 are wxyz orientation

    # make sure that it is NumPy array
    pose_data = np.array(pose_data)

    # initialize
    waypoints = []
    # Define a "sleep" pose that is the robot on its base
    sleep_pose = self.group.get_current_pose().pose
    # Initialize a running variable to store pose data
    wpose = self.group.get_current_pose().pose

    if raise_from_base == True:
      wpose.position.z += 0.25
      waypoints.append(copy.deepcopy(wpose))
      wpose.position.x += 0.25
      waypoints.append(copy.deepcopy(wpose))

    if mirror_return == True:
      # does a return to base mirroring previous motion
      pose_data = np.vstack((pose_data, np.flipud(pose_data[0:pose_data.shape[0]-1,:])))

    # number of waypoints
    n = pose_data.shape[0]

    # position only
    if pose_data.shape[1] == 3:
      for tstep in range(n):
        wpose.position.x = pose_data[tstep, 0]
        wpose.position.y = pose_data[tstep, 1]
        wpose.position.z = pose_data[tstep, 2]
        waypoints.append(copy.deepcopy(wpose))
    # position and orientation (euler angles converted to quat)
    elif pose_data.shape[1] == 6:
      for tstep in range(n):
        wpose.position.x = pose_data[tstep, 0]
        wpose.position.y = pose_data[tstep, 1]
        wpose.position.z = pose_data[tstep, 2]
        quat = quaternion_from_euler(pose_data[tstep, [3]],
                                     pose_data[tstep, [4]],
                                     pose_data[tstep, [5]])
        wpose.orientation.w = quat[0]
        wpose.orientation.x = quat[1]
        wpose.orientation.y = quat[2]
        wpose.orientation.z = quat[3]
        waypoints.append(copy.deepcopy(wpose))
    # position and orientation (quat)
    elif pose_data.shape[1] == 7:
      for tstep in range(n):
        wpose.position.x = pose_data[tstep, 0]
        wpose.position.y = pose_data[tstep, 1]
        wpose.position.z = pose_data[tstep, 2]
        wpose.orientation.w = pose_data[tstep, 3]
        wpose.orientation.x = pose_data[tstep, 4]
        wpose.orientation.y = pose_data[tstep, 5]
        wpose.orientation.z = pose_data[tstep, 6]
        waypoints.append(copy.deepcopy(wpose))
    else:
      print("Check that pose data matrix is oriented properly.")

    # return to base safely, moving above base and returning
    wpose.position.z = sleep_pose.position.z + 0.2
    wpose.position.x = sleep_pose.position.x + 0.2
    wpose.position.y = sleep_pose.position.y
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += -0.19
    wpose.position.x += -0.2
    waypoints.append(copy.deepcopy(wpose))

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
    (plan, fraction) = self.group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.01,        # eef_step
                                       0.0)         # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:
    return plan, fraction, waypoints

  def plan_difference_path(self, pose_data, raise_from_base = True, mirror_return = True):
    ## You can plan a Cartesian path directly by specifying a list of waypoints
    ## for the end-effector to go through:
    ##
    ## Input: pose_data is an array of size (n,7), first 3 are xyz position, last 4 are wxyz orientation

    # make sure that it is NumPy array
    pose_data = np.array(pose_data)
    # initialize
    waypoints = []
    # Define a "sleep" pose that is the robot on its base
    sleep_pose = self.group.get_current_pose().pose
    # Initialize a running variable to store pose data
    wpose = self.group.get_current_pose().pose

    if raise_from_base == True:
      wpose.position.z += 0.2
      waypoints.append(copy.deepcopy(wpose))

    if mirror_return == True:
      # does a return to base mirroring previous motion
      pose_data = np.vstack((pose_data, np.flipud(-pose_data)))

    # number of waypoints
    n = pose_data.shape[0]

    # position only
    if pose_data.shape[1] == 3:
      for tstep in range(n):
        wpose.position.x += pose_data[tstep, 0]
        wpose.position.y += pose_data[tstep, 1]
        wpose.position.z += pose_data[tstep, 2]
        waypoints.append(copy.deepcopy(wpose))
    # position and orientation (euler angles converted to quat)
    elif pose_data.shape[1] == 6:
      for tstep in range(n):
        wpose.position.x += pose_data[tstep, 0]
        wpose.position.y += pose_data[tstep, 1]
        wpose.position.z += pose_data[tstep, 2]
        quat = quaternion_from_euler(pose_data[tstep, [3]],
                                     pose_data[tstep, [4]],
                                     pose_data[tstep, [5]])
        wpose.orientation.w += quat[0]
        wpose.orientation.x += quat[1]
        wpose.orientation.y += quat[2]
        wpose.orientation.z += quat[3]
        waypoints.append(copy.deepcopy(wpose))
    # position and orientation (quat)
    elif pose_data.shape[1] == 7:
      for tstep in range(n):
        wpose.position.x += pose_data[tstep, 0]
        wpose.position.y += pose_data[tstep, 1]
        wpose.position.z += pose_data[tstep, 2]
        wpose.orientation.w += pose_data[tstep, 3]
        wpose.orientation.x += pose_data[tstep, 4]
        wpose.orientation.y += pose_data[tstep, 5]
        wpose.orientation.z += pose_data[tstep, 6]
        waypoints.append(copy.deepcopy(wpose))
    else:
      print("Check that pose data matrix is oriented properly.")

    if mirror_return == True:
      # does a quick return, moving above base and returning
      wpose.position.z = sleep_pose.position.z + 0.2
      waypoints.append(copy.deepcopy(wpose))
      wpose.position.z = sleep_pose.position.z + 0.005
      waypoints.append(copy.deepcopy(wpose))

    if mirror_return == False:
      wpose.position.z = sleep_pose.position.z + 0.2
      waypoints.append(copy.deepcopy(wpose))
      wpose.position.z = sleep_pose.position.z + 0.005
      waypoints.append(copy.deepcopy(wpose))


    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
    (plan, fraction) = self.group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.02,        # eef_step
                                       0.0)         # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:
    return plan, fraction

  def display_trajectory(self, plan):
    ## Displaying a Trajectory
    ## ^^^^^^^^^^^^^^^^^^^^^^^
    ## You can ask RViz to visualize a plan (aka trajectory) for you. But the
    ## group.plan() method does this automatically so this is not that useful
    ## here (it just displays the same trajectory again):
    ##
    ## A `DisplayTrajectory`_ msg has two primary fields, trajectory_start and trajectory.
    ## We populate the trajectory_start with our current robot state to copy over
    ## any AttachedCollisionObjects and add our plan to the trajectory.
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = self.robot.get_current_state()
    display_trajectory.trajectory.append(plan)
    # Publish
    self.display_trajectory_publisher.publish(display_trajectory);

  def execute_plan(self, plan):
    ## Executing a Plan
    ## ^^^^^^^^^^^^^^^^
    ## Use execute if you would like the robot to follow
    ## the plan that has already been computed:
    self.group.execute(plan, wait=True)

    ## **Note:** The robot's current joint state must be within some tolerance of the
    ## first waypoint in the `RobotTrajectory`_ or ``execute()`` will fail

  def wait_for_state_update(self, box_is_known=False, box_is_attached=False, timeout=4):
    ## Ensuring Collision Updates Are Receieved
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ## If the Python node dies before publishing a collision object update message, the message
    ## could get lost and the box will not appear. To ensure that the updates are
    ## made, we wait until we see the changes reflected in the
    ## ``get_known_object_names()`` and ``get_known_object_names()`` lists.
    ## For the purpose of this interface, we call this function after adding,
    ## removing, attaching or detaching an object in the planning scene. We then wait
    ## until the updates have been made or ``timeout`` seconds have passed
    start = rospy.get_time()
    seconds = rospy.get_time()
    while (seconds - start < timeout) and not rospy.is_shutdown():
      # Test if the box is in attached objects
      attached_objects = self.scene.get_attached_objects([self.box_name])
      is_attached = len(attached_objects.keys()) > 0

      # Test if the box is in the scene.
      # Note that attaching the box will remove it from known_objects
      is_known = self.box_name in self.scene.get_known_object_names()
      # Test if we are in the expected state
      if (box_is_attached == is_attached) and (box_is_known == is_known):
        return True

      # Sleep so that we give other threads time on the processor
      rospy.sleep(0.1)
      seconds = rospy.get_time()

    # If we exited the while loop without returning then we timed out
    return False

  def add_box(self, timeout=4):
    ## Adding Objects to the Planning Scene
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ## First, we will create a box in the planning scene at the location of the left finger:
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = self.eef_link
    box_pose.pose.position.x = self.ee_link_offset[0]
    box_pose.pose.position.y = self.ee_link_offset[1]
    box_pose.pose.position.z = self.ee_link_offset[2]
    box_pose.pose.orientation.w = 1.0
    self.box_name = "box"
    self.scene.add_box(self.box_name, box_pose, size=(0.025, 0.025, 0.05))

    return self.wait_for_state_update(box_is_known=True, timeout=timeout)

  def attach_box(self, timeout=4):
    ## Attaching Objects to the Robot
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ## Next, we will attach the box to the Arm's wrist. Manipulating objects requires the
    ## robot be able to touch them without the planning scene reporting the contact as a
    ## collision. By adding link names to the ``touch_links`` array, we are telling the
    ## planning scene to ignore collisions between those links and the box. For the Interbotix
    ## robot, we set ``grasping_group = 'interbotix_gripper'``. If you are using a different robot,
    ## you should change this value to the name of your end effector group name.
    grasping_group = 'interbotix_gripper'
    touch_links = self.robot.get_link_names(group=grasping_group)
    self.scene.attach_box(self.eef_link, self.box_name, touch_links=touch_links)

    # We wait for the planning scene to update.
    return self.wait_for_state_update(box_is_attached=True, box_is_known=False, timeout=timeout)

  def detach_box(self, timeout=4):
    ## Detaching Objects from the Robot
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ## We can also detach and remove the object from the planning scene:
    self.scene.remove_attached_object(self.eef_link, name=self.box_name)

    # We wait for the planning scene to update.
    return self.wait_for_state_update(box_is_known=True, box_is_attached=False, timeout=timeout)

  def remove_box(self, timeout=4):
    ## Removing Objects from the Planning Scene
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ## We can remove the box from the world.
    self.scene.remove_world_object(self.box_name)

    ## **Note:** The object must be detached before we can remove it from the world

    # We wait for the planning scene to update.
    return self.wait_for_state_update(box_is_attached=False, box_is_known=False, timeout=timeout)

  def load_csv(self, input_file):
      with open(input_file, 'r', encoding='utf-8-sig') as f:  # Notice 'utf-8-sig' to manage BOM
          reader = csv.reader(f)
          data = list(reader)
          try:
              data_array = np.array(data, dtype=float)
          except ValueError as e:
              print(f"Error converting data to float: {e}")
              return None
      return data_array

def main():
    print("============ Press `Enter` to set up the moveit_commander (press ctrl-d to exit) ...")
    input()
    interface = DiscoveryDaysRoboticInterface()

    print("============ Press `Enter` to plan and display a path ...")

    input_file = os.path.join("/home", "jhsiaoc", "Downloads", "Star_robot.csv")
    # pose_data = interface.load_csv(input_file)

    step_number = 50

    theta = np.linspace(-np.pi/2,np.pi/2,step_number)[:, np.newaxis]
    x = np.cos(theta)
    y = np.sin(theta)

    phi = np.linspace(0,2*np.pi,step_number)[:, np.newaxis]
    z = np.sin(phi)

    x_offset = 0.145
    y_offset = 0
    z_offset = 0.09 + 0.2

    x_bar = x * 0.2 + x_offset
    y_bar = y * 0.2 + y_offset
    z_bar = z * 0.15 + z_offset

    pose_data = np.hstack((x_bar, y_bar, z_bar))

    # qx = np.ones_like(x_bar) * 0
    # qy = np.ones_like(x_bar) * 0
    # qz = np.ones_like(x_bar) * 0
    # qw = np.ones_like(x_bar) * 1

    # , qw, qx, qy, qz

    pose_data = np.hstack((x_bar, y_bar, z_bar))

    plan, fraction, waypoints = interface.plan_absolute_path(pose_data, mirror_return = True)

    print("============ Press `Enter` to display a saved trajectory (this will replay the path)  ...")
    input()
    interface.display_trajectory(plan)
    '''
    if fraction < 0.98
      print("Trajectory planning failed!")
      rospy.spin()
    '''
    print(waypoints)

    print("============ Press `Enter` to execute the path ...")
    input()
    interface.execute_plan(plan)
    rospy.spin()

if __name__ == '__main__':
  main()