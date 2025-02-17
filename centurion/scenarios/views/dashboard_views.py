from django.shortcuts import render
from ..models import Scenario, Order, Pickup

def scenario_dashboard(request, pk):
    scenario = Scenario.objects.get(pk=pk)
    context = {'scenario': scenario}
    return render(request, 'scenarios/dashboards/scenario_dashboard.html', context)

def order_dashboard(request, pk):
    order = Order.objects.get(pk=pk)
    context = {'order': order}
    return render(request, 'scenarios/dashboards/order_dashboard.html', context)

def order_dashboard_delivery_partial(request, pk):
    pickup = Pickup.objects.get(pk=pk)
    context = {'pickup': pickup}
    return render(request, 'scenarios/dashboards/partial/order_dashboard_deliveries.html', context)