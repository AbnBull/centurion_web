from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from ..models import Order, Scenario


class OrderListView(ListView):
    model = Order
    template_name = 'scenarios/order/order_list.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'scenarios/order/order_detail.html'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'scenarios/order/order_form.html'
    fields = ['name', 'scenario', 'offset']
    success_url = reverse_lazy('order_list')

    def get_initial(self):
        initial = super().get_initial()
        scenario_id = self.kwargs.get('scenario_id')
        if scenario_id:
            initial['scenario'] = get_object_or_404(Scenario, pk=scenario_id)
        return initial


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'scenarios/order/order_form.html'
    fields = ['name', 'scenario', 'offset']


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'scenarios/order/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')