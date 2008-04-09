#!/usr/bin/python2.4
#
# Copyright (C) 2008  Google, Inc. All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""TsumuFS, a NFS-based caching filesystem."""

import tsumufs

class Triumvirate:
  """Defines some basic behavior and utility functions that all three
  main threads require for functioning.

  Any shared code between the three should be placed here instead of
  copying."""

  name = None

  def setName(self, name):
    self.name = name

  def getName(self):
    return self.name
  
  def debug(self, args):
    """Quick method to output some debugging information which states the
    thread name a colon, and whatever arguments have been passed to
    it.

    Args:
      args: a list of additional arguments to pass, much like what
        print() takes.
    """
    
    if tsumufs.debugMode:
      print(self.getName() + ": "+ args)
