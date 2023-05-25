"""
URLs for lmedxanalytics.
"""
from django.urls import re_path,path # pylint: disable=unused-import
# from django.conf.urls import url,path
from django.views.generic import TemplateView  # pylint: disable=unused-import
from . import views

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="lmedxanalytics/base.html")),
    path('', views.hello_world, name='hello_world'),\
    path('test', views.hello_world2, name='hello_world2')
]
