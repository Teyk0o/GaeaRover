@echo off

REM Arrêter et supprimer l'ancien conteneur s'il existe
docker stop rover_container 2>nul
docker rm rover_container 2>nul

REM Construire l'image
docker build -t rover_sim .

REM Lancer le nouveau conteneur
docker run -it --name rover_container -v %cd%/src/rover_sim:/catkin_ws/src/rover_sim rover_sim