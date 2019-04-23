from django.urls import path, re_path
# from django.conf.urls import include, url
from . import views

# 缺少则'Specifying a namespace in include() without providing an app_name '
app_name = '[learning5_logs]'

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name = 'topic'),
    path('new_topic/', views.new_topic, name = 'new_topic'),
    re_path('edit_topic/(?P<topic_id>\d+)/', views.edit_topic, name = 'edit_topic'),
    re_path('del_topic/(?P<topic_id>\d+)/', views.del_topic, name = 'del_topic'),
    re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name = 'new_entry'),
    re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name = 'edit_entry'),
    re_path('del_entry/(?P<entry_id>\d+)/', views.del_entry, name = 'del_entry'),
]
