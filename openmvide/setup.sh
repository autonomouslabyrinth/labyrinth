#! /bin/sh

sudo apt-get install -y libxcb* libGLES* libts* libsqlite* libodbc* libsybdb* libusb-1.0 python-pip
sudo pip install pyusb

sudo cp $( dirname "$0" )/share/qtcreator/pydfu/50-openmv.rules /etc/udev/rules.d/50-openmv.rules
sudo udevadm control --reload-rules

if [ -z "${QT_QPA_PLATFORM}" ]; then
    echo >> ~/.bashrc
    echo "# Force Qt Apps to use xcb" >> ~/.bashrc
    echo "export QT_QPA_PLATFORM=xcb" >> ~/.bashrc
    echo
    echo Please type "source ~/.bashrc".
fi

