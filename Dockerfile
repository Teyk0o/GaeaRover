FROM osrf/ros:noetic-desktop-full

RUN apt-get update && apt-get install -y \
    gazebo11 \
    ros-noetic-gazebo-ros-pkgs \
    ros-noetic-gazebo-ros-control \
    python3-pip \
    git

WORKDIR /catkin_ws/src

# Copier le contenu du projet
COPY ./src/rover_sim ./rover_sim

WORKDIR /catkin_ws

RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; catkin_make'

RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc

ENV DISPLAY=host.docker.internal:0.0

CMD ["/bin/bash"]