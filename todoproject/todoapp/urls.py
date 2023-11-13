
from django.urls import path

from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    #path('detail',views.detail,name='detail')
    # path('add/',views.add,name='add')
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete'),
]