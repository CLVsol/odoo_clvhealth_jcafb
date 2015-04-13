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

import base
import admin_groups_id
import data_admin_groups_id

import xmlrpclib
import erppeek

def install_update_module(module, update, config_admin=False):

    modules_to_update = base.modules_to_update

    print '%s%s' % ('--> ', module)
    if module in modules_to_update:
        new_module = base.install_update_module(module, True)
    else:
        new_module = base.install_update_module(module, update)

    if new_module and config_admin:
        method = '%s%s' % ('Administrator_groups_id_', module)
        print '%s%s' % ('--> ', method)
        methodToCall = getattr(admin_groups_id, method)
        result = methodToCall()

        method = '%s%s' % ('Data_Administrator_groups_id_', module)
        print '%s%s' % ('--> ', method)
        methodToCall = getattr(data_admin_groups_id, method)
        result = methodToCall()

    return new_module

def clvhealth_jcafb_install():

    update = base.update

    print '--> create_database()'
    newDB = base.create_database()
    if newDB:
        print '--> YourCompany()'
        base.YourCompany()
        print '--> Administrator()'
        base.Administrator()
        print '--> Administrator_groups_id_updt()'
        base.Administrator_groups_id_updt()
        print '--> Demo_User()'
        base.Demo_User()
        print '--> Data_Administrator_User()'
        base.Data_Administrator_User()
    else:
        client = erppeek.Client(base.server, db=base.dbname, user=base.admin_user, 
                                password=base.admin_user_pw, verbose=False)
        proxy = client.model('ir.module.module')
        proxy.update_list()

    new_module = install_update_module('l10n_br_base', update)

    new_module = install_update_module('l10n_br_zip', update)

    new_module = install_update_module('l10n_br_data_zip', update)

    new_module = install_update_module('clv_base', update, True)

    new_module = install_update_module('clv_base_cst', update)

    new_module = install_update_module('clv_tag', update, True)

    new_module = install_update_module('clv_tag_cst', update)

    new_module = install_update_module('clv_annotation', update, True)

    new_module = install_update_module('clv_annotation_cst', update)

    new_module = install_update_module('clv_address', update, True)

    new_module = install_update_module('l10n_br_clv_address', update)

    new_module = install_update_module('clv_address_cst', update)

    # new_module = install_update_module('clv_place', update, True)

    # new_module = install_update_module('clv_place_cst', update)

    # new_module = install_update_module('clv_frame', update, True)

    # new_module = install_update_module('clv_frame_cst', update)

    # new_module = install_update_module('clv_tray', update, True)

    # new_module = install_update_module('clv_tray_cst', update)

    # new_module = install_update_module('clv_batch', update, True)

    # new_module = install_update_module('clv_batch_cst', update)

    # new_module = install_update_module('clv_insurance', update, True)

    # new_module = install_update_module('clv_insurance_cst', update)

    # new_module = install_update_module('clv_insurance_client', update, True)

    # new_module = install_update_module('clv_insurance_client_cst', update)

    # new_module = install_update_module('clv_insured', update, True)

    # new_module = install_update_module('l10n_br_clv_insured', update)

    # new_module = install_update_module('clv_insured_cst', update)

    # new_module = install_update_module('clv_insured_card', update, True)

    # new_module = install_update_module('clv_insured_card_cst', update)

    # new_module = install_update_module('clv_insured_mng', update, True)

    # new_module = install_update_module('l10n_br_clv_insured_mng', update)

    # new_module = install_update_module('clv_medicament', update, True)

    # new_module = install_update_module('clv_medicament_cst', update)

    # new_module = install_update_module('clv_medicament_mng', update, True)

    # new_module = install_update_module('l10n_br_clv_abcfarma', update)

    # new_module = install_update_module('clv_medicament_catalog', update, True)

    # new_module = install_update_module('clv_medicament_catalog_member', update)

    # new_module = install_update_module('clv_medicament_group', update, True)

    # new_module = install_update_module('clv_medicament_group_cst', update)

    # new_module = install_update_module('clv_medicament_group_member', update)

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],[(t*1000,),1000,60,60])

if __name__ == '__main__':

    from time import time

    start = time()

    base.get_arguments()

    print '--> Executing clvhealth_jcafb_install.py...'

    print '--> Executing clvhealth_jcafb_install()...'
    clvhealth_jcafb_install()

    print '--> clvhealth_jcafb_install.py'
    print '--> Execution time:', secondsToStr(time() - start)
