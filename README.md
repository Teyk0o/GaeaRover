# 🤖 GaeaRover Simulation Project

## 📝 Description
The GaeaRover Simulation Project is a ROS/Gazebo simulation of an autonomous rover equipped with a rotating LiDAR. This project aims to develop and test autonomous exploration algorithms in a simulated environment.

## 🐳 Docker Setup and Usage

### Prerequisites
- Docker installed on your system
- X11 server (for GUI applications on Windows or macOS)

### 🚀 Installation and Setup

1. Clone this repository:
```BASH
cd ~/catkin_ws/src
git clone https://github.com/Teyk0o/GaeaRover.git
```

2. Build the Docker image:
```BASH
docker build -t gaea_rover .
```

### 🎮 Usage

1. Start the Docker container:
- On Windows :
```BASH
./run.bat
```

- Other :
```BASH
./run.sh
```

2. Inside the container, build the project:
```BASH
cd /catkin_ws
catkin_make
source devel/setup.bash
```

3. Launch the simulation:
```BASH
roslaunch rover_sim rover_sim.launch
```

4. To stop the simulation, press ``Crtl+C`` in the terminal.

5. To exit the Docker container, type ``exit`` in the terminal.

### 💡 Tips

- If you modify the source code, you need to rebuild the project inside the Docker container using catkin_make.
- Changes made to files in the src directory will persist on your host machine.

### 📁 Project Structure

- ``rover_sim/``: Main rover package
  - ``launch/``: Launch files
  - ``models/``: URDF models of the rover
  - ``src/``: Python source code
  - ``config/``: Configuration files
  
### ✨ Features

- Four-wheeled rover simulation
- Rotating LiDAR for mapping

### 🤝 Contributing

Contributions to this project are welcome. Please follow these steps to contribute:

1. Fork the project
2. Create your feature branch (``git checkout -b feature/AmazingFeature``)
3. Commit your changes (``git commit -m 'feat: Add some AmazingFeature'``)
4. Push to the branch (``git push origin feature/AmazingFeature``)
5. Open a Pull Request

### 📄 License

Distributed under the CC BY-NC-ND 4.0. See ``LICENSE`` for more information.

### 🙏 Acknowledgments

- ROS community
- Gazebo simulator
- All contributors to this project