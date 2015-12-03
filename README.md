# rpi_bt_connector
Connect a bluetooth device to RaspberryPi

### Motivation
Attaching a bluetooth device is not easy at this point with the
Raspberry Pi running RetroPie.  Currently, there seems to be a large
number of steps that make it difficult for novice users.  I wanted to
gift someone a raspberry pi, and while I have the experience and
know-how to get around an embedded system, I didn't want them to need
that knowledge.

I wanted something I could run on a RetroPie without needing
to plug in a keyboard and mouse.  This script allows me to auto-pair
a device if its searching, even if the device has been paired
previously.

In the example of an [NES30](http://www.nes30.com), I can forget my
previous pairing, and  this script will take care of repairing without
needing a keyboard.

Note this has only been tested on a
[RetroPi](http://blog.petrockblock.com/retropie/) build running under
berryboot on a [raspberry pi 2](http://www.amazon.com/Raspberry-Pi-Model-Project-Board/dp/B00T2U7R7I/ref=lp_5811495011_1_1?srs=5811495011&ie=UTF8&qid=1449181391&sr=8-1) using an
[insignia bluetooth device](http://www.insigniaproducts.com/products/computer-speakers-accessories/NS-PCY5BMA.html).
I ended up realizing that my [canakit](http://www.canakit.com/raspberry-pi-starter-kit.html) did not include a bluetooth adaptor
and I ran down to the local Best Buy to pick up their cheapest bluetooth
usb stick.  Fortunately, it was $10.

Most of my instructions for setup came from here:
[8bitdo's forums](http://forum.8bitdo.com/thread-328-1-1.html)

### Dependencies
The following list of [Raspbian](http://raspbian.org) packages are
required.

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
