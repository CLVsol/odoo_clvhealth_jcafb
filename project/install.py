#!/usr/bin/env python
# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

from base import *
from admin_groups_id import *
#from data import *

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],[(t*1000,),1000,60,60])

def clvhealth_jcafb_install():

    update = True
    #update = False

    print '--> create_database()'
    newDB = create_database(dbname, admin_user_pw, lang)
    if newDB:
        print '--> CLVhealth_JCAFB()'
        CLVhealth_JCAFB()
        print '--> Administrator()'
        Administrator()
        print '--> Administrator_groups_id_updt()'
        Administrator_groups_id_updt()

    print '--> clvhealth_jcafb'
    new_clvhealth_jcafb = install_update_module('clvhealth_jcafb', dbname, admin_user_pw, update)
    if new_clvhealth_jcafb:
        print '--> Administrator_groups_id_clvhealth_jcafb()'
        Administrator_groups_id_clvhealth_jcafb()

if __name__ == '__main__':

    from time import time
    start = time()

    print '--> Executing clvhealth_jcafb_install.py ...'
    clvhealth_jcafb_install()

    print '--> clvhealth_jcafb_install.py'
    print '--> Execution time:', secondsToStr(time() - start)
