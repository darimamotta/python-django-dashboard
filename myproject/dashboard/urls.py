from django.urls import path
from . import views
#from django.views.decorators.cache import cache_page

urlpatterns = [
    #path('', cache_page(60)(views.index), name='dashboard-index'),
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('order/', views.order, name='dashboard-order'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('profile/', views.profile, name='dashboard-profile'),
    path('add', views.add, name='dashboard-add'),
    #path('result_add', views.result_add, name='dashboard-add'),
    path('result/add/<int:pk>/', views.result_add, name='dashboard-result'),
    #path('add', views.result_add, name='dashboard-result'),
    path('add', views.add1, name='dashboard-result'),
    #path('resultlist', views.resultlist, name='dashboard-resultlist'),
    path('<str:id>/', views.resultlist, name='dashboard-resultlist'),
    path('resultlist.html', views.result_list, name='tableres'),
    path('add', views.TaskSetter.as_view()),
    #path('settask', views.TaskSetter.as_view()),
   # path('gettask', views.TaskGetter.as_view()),

]