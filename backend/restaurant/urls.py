from django.urls import path, include
from .views import *

app_name = 'restaurant'

urlpatterns = [
    path('orderitem/create', OrderItemCreateView.as_view()),
    path('orderitem/list', OrderItemListView.as_view()),
    path('orderitem/delete', OrderItemDestroyView.as_view()),
    path('orderitem/update', OrderItemUpdateView.as_view()),
    path('menu/create/', MenuCreateView.as_view()),
    path('menu/update/<int:pk>/', MenuUpdateView.as_view()),
    path('menu/list/', MenuListView.as_view()),
    path('menu/delete/<int:pk>', MenuDeleteView.as_view()),
    path('order/list/', OrderListView.as_view()),
    path('order/listactive/', OrderListActiveView.as_view()),
    path('order/listnotactive/', OrderListNotActiveView.as_view()),
    path('order/create/', OrderCreateView.as_view()),
    path('order/delete/<str:number>/', OrderDestroyView.as_view()),
    path('order/update/<str:number>/', OrderView.as_view()),
    path('table/create/', TableCreateView.as_view()),
    path('table/list/', TableListView.as_view()),
    path('table/update/<str:name>/', TableView.as_view()),
    path('table/delete/<str:name>/', TableDestroyView.as_view()),
    path('report/fullcost/', FullCostOrdersListView),
    path('report/cost/table/<int:pk>/', CostTablesListView),
    path('report/cost/year/<int:year>/', CostYearListView),
    path('report/cost/month/<int:month>/', CostMonthListView),
    path('report/cost/day/<int:day>/', CostDayListView),

]
