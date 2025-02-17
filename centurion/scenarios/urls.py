from django.urls import path
from .views import ScenarioListView, ScenarioDetailView, ScenarioCreateView, ScenarioUpdateView, ScenarioDeleteView
from .views import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView
from .views import PickupCreateView, PickupDeleteView, PickupDetailView, PickupListView, PickupUpdateView
from .views import DeliveryCreateView, DeliveryDeleteView, DeliveryDetailView, DeliveryListView, DeliveryUpdateView
from .views import navbar_scenario_list, scenario_dashboard, order_dashboard, order_dashboard_delivery_partial

# Dashboards
urlpatterns = [
    path('dashboard/scenario/<int:pk>/', scenario_dashboard, name='scenario_dashboard'),
    path('dashboard/order/<int:pk>/', order_dashboard, name='order_dashboard'),
    path('dashboard/partial/order-dashboard-deliveries/pickup/<int:pk>/', order_dashboard_delivery_partial, name='order_dashboard_delivery_partial'),
]

# Scenarios
urlpatterns += [
    path('scenario/', ScenarioListView.as_view(), name='scenario_list'),
    path('scenario/<int:pk>/', ScenarioDetailView.as_view(), name='scenario_detail'),
    path('scenario/add/', ScenarioCreateView.as_view(), name='scenario_create'),
    path('scenario/<int:pk>/edit/', ScenarioUpdateView.as_view(), name='scenario_update'),
    path('scenario/<int:pk>/delete/', ScenarioDeleteView.as_view(), name='scenario_delete'),
    path('scenario/partial/navbar-scenario-list/', navbar_scenario_list, name='navbar_scenario_list'),
]


# Orders
urlpatterns += [
    path('order/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/add/', OrderCreateView.as_view(), name='order_create'),
    path('order/add/pickup/<int:scenario_id>/', OrderCreateView.as_view(), name='order_create_with_scenario_id'),
    path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]

# Pickups
urlpatterns += [
    path('pickup/', PickupListView.as_view(), name='pickup_list'),
    path('pickup/<int:pk>/', PickupDetailView.as_view(), name='pickup_detail'),
    path('pickup/add/', PickupCreateView.as_view(), name='pickup_create'),
    path('pickup/add/order/<int:order_id>/', PickupCreateView.as_view(), name='pickup_create_with_order_id'),
    path('pickup/<int:pk>/edit/', PickupUpdateView.as_view(), name='pickup_update'),
    path('pickup/<int:pk>/delete/', PickupDeleteView.as_view(), name='pickup_delete'),
]

# Deliveries
urlpatterns += [
    path('delivery/', DeliveryListView.as_view(), name='delivery_list'),
    path('delivery/<int:pk>/', DeliveryDetailView.as_view(), name='delivery_detail'),
    path('delivery/add/', DeliveryCreateView.as_view(), name='delivery_create'),
    path('delivery/add/pickup/<int:pickup_id>/', DeliveryCreateView.as_view(), name='delivery_create_with_pickup_id'),
    path('delivery/<int:pk>/edit/', DeliveryUpdateView.as_view(), name='delivery_update'),
    path('delivery/<int:pk>/delete/', DeliveryDeleteView.as_view(), name='delivery_delete'),
]