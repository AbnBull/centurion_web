from django.urls import path
from .views import ScenarioListView, ScenarioDetailView, ScenarioCreateView, ScenarioUpdateView, ScenarioDeleteView
from .views import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView


# Scenarios
urlpatterns = [
    path('scenario/', ScenarioListView.as_view(), name='scenario_list'),
    path('scenario/<int:pk>/', ScenarioDetailView.as_view(), name='scenario_detail'),
    path('scenario/add/', ScenarioCreateView.as_view(), name='scenario_create'),
    path('scenario/<int:pk>/edit/', ScenarioUpdateView.as_view(), name='scenario_update'),
    path('scenario/<int:pk>/delete/', ScenarioDeleteView.as_view(), name='scenario_delete'),
]


# Orders
urlpatterns += [
    path('order/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/add/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]