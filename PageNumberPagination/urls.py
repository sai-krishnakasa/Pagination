from django.urls import path
from . import views
urlpatterns=[
    path('1',views.PageView.as_view()),
    path('2',views.LimitOffsetView.as_view()),
    path('3/',views.CurserView.as_view()),
]