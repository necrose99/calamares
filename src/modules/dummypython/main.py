#!/usr/bin/env python3
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2014, Teo Mrnjavac <teo@kde.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import sys
import libcalamares
import os
from time import gmtime, strftime

def calamares_main():
    os.system( "/bin/sh -c \"touch ~/calamares-dummypython\"" )
    accumulator = strftime( "%Y-%m-%d %H:%M:%S", gmtime() ) + "\n"
    accumulator += "Calamares version: " + libcalamares.VERSION_SHORT + "\n"
    accumulator += "This job's name: " + libcalamares.job.prettyName() + "\n"
    accumulator += "This job's path: " + libcalamares.job.workingPath() + "\n"
    return accumulator
