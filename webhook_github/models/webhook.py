# -*- encoding: utf-8 -*-
##############################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: moylop260@vauxoo.com
#    planned by: nhomar@vauxoo.com
#                moylop260@vauxoo.com
############################################################################

from pprint import pprint

from openerp import api, models


class Webhook(models.Model):
    _inherit = 'webhook'

    @api.one
    def set_driver_remote_address(self):
        super(Webhook, self).set_driver_remote_address()
        self.env.webhook_driver_address.update({
            'github': ['192.30.252.0/22']
        })

    @api.one
    def set_event(self):
        super(Webhook, self).set_event()
        if not self.env.webhook_event and self.env.webhook_driver_name == 'github':
            self.env.webhook_event = self.env.request.httprequest.headers.get('X-Github-Event') 

    @api.one
    def run_webhook_github_status(self):
        print "I'm here: run_webhook_github_status"
        # pprint(self.env.request.jsonrequest)
        return True

    @api.one
    def run_webhook_github_pull_request(self):
        print "I'm here: run_webhook_github_pull_request"
        # pprint(self.env.request.jsonrequest)
        print "PR change in: %s/%s/pull/%s" % (
            self.env.request.jsonrequest['repository']['owner']['login'],
            self.env.request.jsonrequest['repository']['name'],
            self.env.request.jsonrequest['pull_request']['number']
        )
        return True

    @api.one
    def run_webhook_github_push(self):
        print "I'm here: run_webhook_github_push"
        pprint(self.env.request.jsonrequest)
        print "Push change in: %s/%s" % (
            self.env.request.jsonrequest['repository']['owner']['name'],
            self.env.request.jsonrequest['repository']['name']
        )
        print "self.env.request.jsonrequest['ref']", self.env.request.jsonrequest['ref']
        print "self.env.request.jsonrequest['base_ref']", self.env.request.jsonrequest['base_ref']
        return True
