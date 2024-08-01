#!/bin/bash
xhost +local:docker
docker run -it --rm \
  --env="DISPLAY=$DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --volume="$PWD:/catkin_ws/src/rover_project" \
  --name gaea_rover_container \
  gaea_rover \
  bash
xhost -local:docker