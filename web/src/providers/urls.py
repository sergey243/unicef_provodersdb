from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [
    path('providers/',login_required(views.ProvidersList.as_view()),name='providers-list'),
    path('providers/<int:pk>/',login_required(views.ProviderDetails.as_view()),name='provider-details'),
    path('providers/update/<int:pk>/',login_required(views.ProviderUpdate.as_view()),name='provider-update'),
    path('providers/create/',login_required(views.ProviderCreate.as_view()),name='provider-create'),
    path('providers/delete/<int:pk>/',login_required(views.ProviderDelete.as_view()),name='provider-delete'),
    
    path('services/',login_required(views.ServicesList.as_view()),name='services-list'),
    path('services/<int:pk>/',login_required(views.ServiceDetails.as_view()),name='service-details'),
    path('services/update/<int:pk>/',login_required(views.ServiceUpdate.as_view()),name='service-update'),
    path('services/create/',login_required(views.ServiceCreate.as_view()),name='service-create'),
    path('services/delete/<int:pk>/',login_required(views.ServiceDelete.as_view()),name='service-delete'),

    path('goods/',login_required(views.GoodsList.as_view()),name='goods-list'),
    path('goods/<int:pk>/',login_required(views.GoodDetails.as_view()),name='good-details'),
    path('goods/update/<int:pk>/',login_required(views.GoodUpdate.as_view()),name='good-update'),
    path('goods/create/',login_required(views.GoodCreate.as_view()),name='good-create'),
    path('goods/delete/<int:pk>/',login_required(views.GoodDelete.as_view()),name='good-delete'),

    path('works/',login_required(views.WorksList.as_view()),name='works-list'),
    path('works/<int:pk>/',login_required(views.WorkDetails.as_view()),name='work-details'),
    path('works/update/<int:pk>/',login_required(views.WorkUpdate.as_view()),name='work-update'),
    path('works/create/',login_required(views.WorkCreate.as_view()),name='work-create'),
    path('works/delete/<int:pk>/',login_required(views.WorkDelete.as_view()),name='work-delete'),
]
