1) The Raspberry Pi will be utilizing the vehicles power supply; therefore, we will perform commands so that the exteral SSD automatically mounts to the Pi after reboot. 

Perform the simple commands outlined in this straightforward video tutorial created by SpaceRex, so that the external SSD mounts onto Raspberry Pi on reboot:
https://www.youtube.com/watch?v=eQZdPlMH-X8

2) So the recorder.py script will run on startup we will create a service. 

Create: 
sudo nano /etc/systemd/system/camera-capture.service

Paste:
[Unit]
Description=Long-duration camera capture
After=multi-user.target

[Service]
Type=simple
User=pi
Group=pi
ExecStart=/usr/bin/python3 /home/pi/capture.py
WorkingDirectory=/home/juan
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target


sudo systemctl daemon-reload
sudo systemctl enable camera-capture.service
sudo systemctl start camera-capture.service


Video of Dash Cam in action:
https://www.youtube.com/watch?v=T6Gz-dZnkSY

