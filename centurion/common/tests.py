from django.test import TestCase
from scenarios.models import Scenario, Order, Pickup, Delivery
from .utilities.general_utilities import get_all_related_objects

class GetAllRelatedObjectsTestCase(TestCase):
    def setUp(self):
        
        # create scenario
        self.scenario = Scenario.objects.create()
        self.scenario.save()

        # create order
        self.order = Order.objects.create(scenario=self.scenario)
        self.order.save()

        # create pickup
        self.pickup = Pickup.objects.create(order=self.order)
        self.pickup.save()

        # create delivery
        self.delivery = Delivery.objects.create(pickup=self.pickup)
        self.delivery.save()


    def test_get_all_related_objects(self):
        related_objects = get_all_related_objects(self.scenario)
        self.assertIn(self.order, related_objects)
        self.assertIn(self.pickup, related_objects)
        self.assertIn(self.delivery, related_objects)
        self.assertNotIn(self.scenario, related_objects)

