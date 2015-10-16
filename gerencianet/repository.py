#!/usr/bin/python
# -*- encoding: utf-8 -*-
from gerencianet.constants import GatewayStatusResponse
from gerencianet.models import PaymentLog

import simplejson


def insert_success_log(notification, email=None, response=None):
    if response is not None:
        response = simplejson.dumps(response)
    PaymentLog.objects.create(data=notification, email=email, response=response, status=GatewayStatusResponse.success)


def insert_error_log(notification, email=None, response=None):
    if response is not None:
        response = simplejson.dumps(response)
    PaymentLog.objects.create(data=notification, email=email, response=response, status=GatewayStatusResponse.error)
