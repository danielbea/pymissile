#!/usr/bin/env python
#
# A simple network client to move missiles via UDP
# I use a 320x240 grid (no coincidence :)) to determine
# which way to move and for how long
#
# I drive this from motion (http://motion.sourgeforge.net/) as the
# script called via:
#
#  on_motion_detected movetointercept.py %K %L
#
# now point webcam at target area, viola!
#
# there is no auto fire, I leave that as an exercise to the reader :)
#
# - License --------------------------------------------------------------
#
# Copyright (c) 2006, Scott Weston
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * The name of the contributors may not be used to endorse or promote
#   products derived from this software without specific prior written
#   permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import getopt
import os
from time import sleep
from socket import *

def main(argv):
  host = "localhost"
  port = 20000
  buf  = 1024
  addr = (host,port)

  x = int(argv[0])
  y = int(argv[1])
  data = None

  UDPSock = socket(AF_INET,SOCK_DGRAM)

  sleeptimex = float(abs(float(x)-160)/55) + 0.3
  sleeptimey = float(abs(float(y)-120)/55) + 0.3
  sleeptime = max(sleeptimex, sleeptimey)

  print "Moving to (%d, %d) sleep time is (%2.2f)" % (x, y, sleeptime)

  mm = [['q', 'a', 'z'], ['w', 'S', 'x'], ['e', 'd', 'c']]

  if x in range(0, 126):
    mx=0
  elif x in range(127, 192):
    mx=1
  else:
    mx=2

  if y in range(0, 100):
    my=0
  elif y in range(101, 140):
    my=1
  else:
    my=2

  pid = os.getpid()
  data = "%s:%s" % (mm[mx][my], pid)

  print "Decided best course of action: %s" % data

  UDPSock.sendto(data,addr)
  sleep(sleeptime)
  UDPSock.sendto("%s:%s" % ("s", pid),addr)
  UDPSock.close()

if __name__=="__main__":
  main(sys.argv[1:])
