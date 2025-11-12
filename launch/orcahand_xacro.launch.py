# ==============================================================================
# Copyright (c) 2025 ORCA
#
# This file is part of ORCA and is licensed under the MIT License.
# You may use, copy, modify, and distribute this file under the terms of the MIT License.
# See the LICENSE file at the root of this repository for full license information.
# ==============================================================================

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import xacro
import os
def generate_launch_description():
    # Example usages:
    # - ros2 launch orcahand_description orcahand.launch.py
    # - ros2 launch orcahand_description orcahand.launch.py urdf_file:=orcahand_left.urdf

    # Launch argument for URDF filename
    urdf_file_arg = DeclareLaunchArgument(
        'urdf_file',
        default_value='orcahand.urdf.xacro',
        description='URDF file to load from the orcahand_description/urdf directory'
    )

    chirality_arg = DeclareLaunchArgument(
        'chirality',
        default_value='right',
        description='right or left'
    )

    # Construct the full path to the URDF/XACRO file using the argument
    orcahand_description_path = PathJoinSubstitution([
        FindPackageShare('orcahand_description'),
        'urdf',
        LaunchConfiguration('urdf_file')
    ])

    # RViz config path (static)
    orcahand_rviz_config_path = PathJoinSubstitution([
        FindPackageShare('orcahand_description'),
        'rviz',
        'config.rviz'
    ])

    robot_description = Command([
        'xacro ', orcahand_description_path, 
        ' chirality:=', LaunchConfiguration('chirality'),
        ' prefix:=', "",
        ' extension:=', "true",
    ])


    return LaunchDescription([
        urdf_file_arg,
        chirality_arg,
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description
            }],
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher',
            output='screen',
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', orcahand_rviz_config_path],
        ),
    ])
