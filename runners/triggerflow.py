#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Parasite        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Parasite
# https://github.com/0xInfection/Parasite

from core.colors import G
import logging, sys
from core.requester import sendQuery

baseurl = 'https://api.github.com/repos/{}/actions/workflows/{}/dispatches'

def triggerWorkflow(slug: str, template: bool):
    '''
    Creates a repository for the authenticated user
    '''
    global baseurl
    log = logging.getLogger('triggerFlow')

    if not template or not slug:
        log.error('One or more required parameters got passed invalid params.')
        return None

    template = '{}.yml'.format(template)
    baseurl = baseurl.format(slug, template)

    payload = {
        "ref" : "main"
    }
    log.debug('Sending payload: %s' % payload)

    req = sendQuery("POST", baseurl, json=payload)
    if req is not None:
        print(G, 'Successfully triggered a workflow for: %s' % template)
        return True
    else:
        log.fatal('Could not trigger a workflow. Something went wrong!')
        sys.exit(1)