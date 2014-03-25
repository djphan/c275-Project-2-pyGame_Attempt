c275_project
============

------------------------------------------------------------------------------------
# Important
------------------------------------------------------------------------------------
The following project is written in Python 2.7. Please load the main files
in Python 2.7 otherwise the project will not open properly. All instructions 
are tailored for Ubuntu. Documentation contains information for Windows
installation, and Macs are unsupported.

------------------------------------------------------------------------------------
# Installation
------------------------------------------------------------------------------------
The following project requires these modules:
------------------------------------------------------------------------------------
1. pygame
You can follow the instructions found in  http://www.pygame.org/wiki/CompileUbuntu
------------------------------------------------------------------------------------

Install Dependencies

sudo apt-get install mercurial python-dev python-numpy ffmpeg \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
 
Grab Source
hg clone https://bitbucket.org/pygame/pygame
 
Finally Build and Install
cd pygame
python setup.py build
sudo python setup.py install

------------------------------------------------------------------------------------
2. OceanGUI
Files found: http://www.pygame.org/project-OcempGUI-125-.html
and complete documentation: http://ocemp.sourceforge.net/gui.html
------------------------------------------------------------------------------------

Download tar and install
sudo python setup.py install
