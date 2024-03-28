from django.urls import path

from src.web.service_provider.views import DashboardView, ProfileView, ReviewsView, WishlistView, SettingView, \
    OrdersView, TravellersView, TravelAgentsView, InvoicesView, PaymentsView, CurrencyView, SubscriberView, \
    LocationView, EditProfileView

app_name = "service_provider"

urlpatterns = [
    path('service_provider/dashboard/', DashboardView.as_view(), name="dashboard"),
    path('service_provider/orders/', OrdersView.as_view(), name="orders"),

    path('service_provider/travellers/', TravellersView.as_view(), name="travellers"),

    path('service_provider/profile/', ProfileView.as_view(), name="profile"),
    path('service_provider/edit/profile/', EditProfileView.as_view(), name="edit_profile"),
    path('service_provider/reviews/', ReviewsView.as_view(), name="reviews"),
    path('service_provider/wishlist/', WishlistView.as_view(), name="wishlist"),

    path('service_provider/travel-agents/', TravelAgentsView.as_view(), name="travel-agents"),

    path('service_provider/invoices/', InvoicesView.as_view(), name="invoices"),
    path('service_provider/payments/', PaymentsView.as_view(), name="payments"),
    path('service_provider/currency/', CurrencyView.as_view(), name="currency"),
    path('service_provider/subscriber/', SubscriberView.as_view(), name="subscriber"),

    path('service_provider/location/', LocationView.as_view(), name="location"),

    path('service_provider/setting/', SettingView.as_view(), name="setting"),
]
