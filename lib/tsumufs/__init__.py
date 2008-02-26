#!/usr/bin/python2.4
#
# Copyright (C) 2007  Google, Inc. All Rights Reserved.
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

from dataregion import *
from inode import *
from nfsmount import *
from synclog import *
from triumvirate import *
from mountthread import *
from syncthread import *
from fusethread import *

debugMode = True

progName = None

mountSource  = False
mountPoint   = False
mountOptions = {}

nfsBaseDir    = "/var/lib/tsumufs/nfs"
nfsMountPoint = None

cacheBaseDir  = "/var/cache/tsumufs"
cacheSpecDir  = "/var/lib/tsumufs/cachespec"
cachePoint    = None

mountedEvent         = Event()
nfsConnectedEvent    = Event()

nfsMount = None
