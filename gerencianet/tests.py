#!/usr/bin/python
# -*- encoding: utf-8 -*-
from django.test import TestCase

from gerencianet.entities import GatewayPlan
from gerencianet.gateway import get_payment_link, get_notification_info


class GatewayTest(TestCase):

    def test_get_payment_link(self):

        code = 1
        email = 'teste@mail.com'
        plan = GatewayPlan(code, 1990, u'Plano Básico', 1, False, 100)
        gateway_payment = get_payment_link(email, plan)

        self.assertIsNotNone(gateway_payment)
        self.assertIsNotNone(gateway_payment.transaction)
        self.assertIsNotNone(gateway_payment.link)

    def test_get_notification_info(self):
        notification = 'notificacao_teste'
        info = get_notification_info(notification)

        self.assertIsNotNone(info)
        self.assertIsNotNone(info.history)
