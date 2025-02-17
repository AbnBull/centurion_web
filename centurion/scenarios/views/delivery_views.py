from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from ..models import Delivery, Pickup


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'scenarios/delivery/delivery_list.html'


class DeliveryDetailView(DetailView):
    model = Delivery
    template_name = 'scenarios/delivery/delivery_detail.html'


class DeliveryCreateView(CreateView):
    model = Delivery
    template_name = 'scenarios/delivery/delivery_form.html'
    fields = ['weight', 'pickup', 'offset', 'location', 'altitude_ft']


    def get_initial(self):
        initial = super().get_initial()
        pickup_id = self.kwargs.get('pickup_id')
        if pickup_id:
            initial['pickup'] = get_object_or_404(Pickup, pk=pickup_id)
        return initial
    
    def get_success_url(self):
        return reverse('delivery_detail', kwargs={'pk': self.object.pk})

class DeliveryUpdateView(UpdateView):
    model = Delivery
    template_name = 'scenarios/delivery/delivery_form.html'
    fields = ['weight', 'pickup', 'offset', 'location', 'altitude_ft']

    def get_success_url(self):
        return reverse('delivery_detail', kwargs={'pk': self.object.pk})


class DeliveryDeleteView(DeleteView):
    model = Delivery
    template_name = 'scenarios/delivery/delivery_confirm_delete.html'
    success_url = reverse_lazy('delivery_list')