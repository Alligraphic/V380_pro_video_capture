## Report
- The camera is a RTSP server running on port 554
- I believe it can be accessed with a static ip as well
- I couldn't figure out a way to rotate the camera or use it's ptz 
- Wireshark shows no packets being sent to the camera when I try to move the camera from the android app
- But the video stream is available in a python code and OBS Studio


## Open Ports
- 554 (RTSP)
- 8800 (probably used for PTZ)
- 8899 (it's open when ONVIF is enabled in the setting but I don't think it's supported in this model of the camera)
- 9800 (?)

## Running the code
- Requirements : run 
```
pip install -r requirements.txt
```
    to install the requirements  

- Option1: you can recieve the footage by editing the file and replacing ``usr``, ``pwd``, and ``ip`` with username, password, and ip   
- Option2: to you can add the URI in a the ``OBS Studio`` app
```
rtsp://{usr}:{pwd}@{ip}/live/ch00_1
```
