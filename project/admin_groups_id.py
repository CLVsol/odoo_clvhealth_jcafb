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

import xmlrpclib

def Administrator_groups_id_clv_base():

    '''
    Reference: http://help.openerp.com/question/18704/hide-menu-for-existing-group/

    There are actually0-6 numbers for representing each job for a many2many/ one2many field

        (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
        (1, ID, { values }) -- update the linked record with id = ID (write values on it)
        (2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the 
                   object completely, and the link to it as well)
        (3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two 
                   objects but does not delete the target object itself)
        (4, ID) -- link to existing record with id = ID (adds a relationship)
        (5) -- unlink all (like using (3,ID) for all linked records)
        (6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
    '''

    print 'Executing Administrator_groups_id_clv_base...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_base
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Super User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Register Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Super Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_tag():

    print 'Executing Administrator_groups_id_clv_tag...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_tag
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Tag User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Tag Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_annotation():

    print 'Executing Administrator_groups_id_clv_annotation...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_annotation
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Annotation User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Annotation Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_address():

    print 'Executing Administrator_groups_id_clv_address...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_address
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Address User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Address Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_person():

    print 'Executing Administrator_groups_id_clv_person...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_person
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Person User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Person Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_family():

    print 'Executing Administrator_groups_id_clv_family...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_family
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Family User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Family Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Administrator_groups_id_clv_community():

    print 'Executing Administrator_groups_id_clv_community...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_community
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Community User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Community Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_patient():

    print 'Executing Administrator_groups_id_clv_patient...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_patient
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Patient User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Patient Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_survey():

    print 'Executing Administrator_groups_id_clv_survey...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_survey
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Survey User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Survey Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Administrator_groups_id_clv_lab_test():

    print 'Executing Administrator_groups_id_clv_lab_test...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_lab_test
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Lab Test User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Lab Test Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    # values = {
    #     'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Lab Test Approver')])[0])],
    #     }
    # sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_pointing():

    print 'Executing Administrator_groups_id_clv_pointing...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_pointing
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Pointing User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Pointing Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clv_document():

    print 'Executing Administrator_groups_id_clv_document...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_document
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Document User')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Document Manager')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(base.dbname, uid, base.admin_user_pw, 'res.groups', 'search', [('name', '=', 'Document Approver')])[0])],
        }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_clvhealth_jcafb():

    '''
    Reference: http://help.openerp.com/question/18704/hide-menu-for-existing-group/

    There are actually0-6 numbers for representing each job for a many2many/ one2many field

        (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
        (1, ID, { values }) -- update the linked record with id = ID (write values on it)
        (2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the 
                   object completely, and the link to it as well)
        (3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two 
                   objects but does not delete the target object itself)
        (4, ID) -- link to existing record with id = ID (adds a relationship)
        (5) -- unlink all (like using (3,ID) for all linked records)
        (6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
    '''

    print 'Executing Administrator_groups_id_clvhealth_futuragene...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    print 'Done.'
