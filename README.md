# rpi_bt_connector
Connect a bluetooth device to RaspberryPi

### Motivation
Attaching a bluetooth device is not easy at this point with the
Raspberry Pi running RetroPie.  Currently, there seems to be a large
number of steps that make it difficult to

I wanted something I could run on a RetroPie without needing
to plug in a keyboard and mouse.  This script allows me to auto-pair
a device if its searching, even if the device has been paired
previously.

In the example of an NES30, I can forget my previous pairing, and this
script will take care of repairing without needing a keyboard.

Note this has only been
tested on a RetroPi build running under berryboot on a raspberry pi 2
using an insignia bluetooth device.  I ended up realizing that my
canakit did not include a bluetooth adaptor and I ran down to the local
Best Buy to pick up their cheapest bluetooth usb stick.  Fortunately,
it was $10.

Most of my instructions for setup came from here:  [8bitdo's forums](http://forum.8bitdo.com/thread-328-1-1.html)

### Dependencies
The following list of Ubuntu packages are required.

    bluetooth
    bluez-utils
    blueman
    bluez
    python-gobject

For retropie, I simply use ssh.  You'll need the ip address for your
raspberry pi.  I denote the ip below as 'rpi.ip'.

    > ssh-copy-id pi@rpi.ip # default password for pi is 'raspberry'
    > ssh pi@rpi.ip  # no need to remember password now.

    > sudo apt-get install -y bluetooth bluez-utils blueman bluez python-gobject

In addition, I use [docopt](http://docopt.org) to handle arguments within the
python script, so we'll need those dependencies as well:

    > sudo chown -R `whoami` /usr/local  # sets up permissions properly
    > pip install docopt  # installs docopt


Once these are installed, the python file should run without an issue.
