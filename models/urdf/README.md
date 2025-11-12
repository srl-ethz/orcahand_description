# ORCA Hand URDF files
1. convert from MJCF to URDF with [mjcf_urdf_simple_converter](https://pypi.org/project/mjcf-urdf-simple-converter/)
2. add links for the fingertip positions
3. move base of hand URDF to origin
4. modify by hand (and GPT-5) to a single XACRO file for the right and left hand

You can also compile the XACRO into URDF yoursel (could be helpful for debugging) with:
```bash
cd /path/to/orcahand_description/models/urdf/
ros2 run xacro xacro orcahand.urdf.xacro chirality:=left prefix:=myprefix_ extension:=False > orcahand.urdf
```