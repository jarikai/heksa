# This folder includes files to configure Rasberry Pi system to run Heksa robot.
File [cooler.service](cooler.service) is used to configure background service created with Python.

File [cooler.py](bin/cooler.py) is the script used to run the system cooler.

I made this cooling system because i had some old unused 5V fan and one extra L298N — H Bridge Motor Driver.

I installation of cooling system:
1. copy cooler.py to /usr/local/bin/cooler.py
2. copy cooler.service to /etc/systemd/system/
3. run command `sudo systemctl enable cooler.service`
4. run command `sudo systemctl daemon-reload`
5. run command `sudo systemctl start cooler.service`
6. run command `sudo systemctl status cooler.service` to get status of service

Other scripts running as service will come later. Some in ideas:
- AI powered voice commands
- human detection with nightvision camera
