from django.conf.urls import include, url
import sys
sys.path.append('..')

urlpatterns =[
    url(r'^api/', include('lmedxanalytics.urls'))
]