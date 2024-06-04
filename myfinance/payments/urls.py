from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.index, name='index'),
    path('payments/<int:payment_id>/', views.payment_detail, name='payment_detail'),
    # path('create/', views.post_create, name='payment_create'),
    # path('payments/<int:payment_id>/edit/', views.post_edit, name='payment_edit'),
]
