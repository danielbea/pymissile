Control your Marks and Spencer USB Missile Launcher on Linux (and maybe other platforms that support python and libusb).


## Tested on ##

  * Ubuntu-5.04
    * (please report other success stories)

## Requirements ##

  1. python (>=2.3)
  1. libusb (>=0.1.8)
  1. pyusb (==0.3.1) python module with patch included below
  1. urwid python module

## Install ##

  1. ensure python is installed and right version
  1. install libusb-0.1.18 or better (available [here](http://libusb.sourceforge.net/)) or use package appropriate for your distro, e.g. on ubuntu:
```
$ sudo apt-get install libusb-dev
```
  1. install pyusb-0.3.1 (available [here](http://sourceforge.net/projects/pyusb/) or [archived here](http://pymissile.googlecode.com/svn/trunk/pyusb-0.3.1.tar.gz)) but patched (see below):
```
$ wget http://pymissile.googlecode.com/svn/trunk/pyusb-0.3.1.tar.gz
$ tar zxvf pyusb-0.3.1.tar.gz
$ cd pyusb-0.3.1
$ wget http://pymissile.googlecode.com/svn/trunk/pyusb-0.3.1-kernel-detach.patch
$ patch -p1 < pyusb-0.3.1-kernel-detach.patch
$ sudo python setup.py install
```
  1. install urwid-0.8.10 (available [here](http://excess.org/urwid/))
  1. plug in Missile Launcher
  1. run missile.py **as root** (maybe non-root will work if you mess with libusb, let me know the details if that's the case)
```
$ wget http://pymissile.googlecode.com/svn/trunk/missile.py 
$ chmod +x ./missile.py
$ sudo ./missile.py
```

## Screenshot and Videos ##

| ![http://pymissile.googlecode.com/svn/trunk/missile.png](http://pymissile.googlecode.com/svn/trunk/missile.png) |
|:----------------------------------------------------------------------------------------------------------------|
| [video 1](http://video.google.com/videoplay?docid=-5930393724587911462) | [video 2](http://video.google.com/videoplay?docid=8706152362255714044) |

## Usage ##

  1. Install
  1. Aim
  1. ...
  1. Profit$

## Todo ##

  * commandline interface
  * use webcam and [motion](http://motion.sourceforge.net/) to have automated sentry (aim and fire)
    * _DONE but not documented yet_
  * daemon and xmlrpc interface for remote aim and shooting of coworkers
    * _SORT OF DONE: manual control is available via the above TODO, needs documentation_