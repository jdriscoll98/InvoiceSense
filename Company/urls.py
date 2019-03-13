from django.conf.urls import url, include

from .views import *

# Application Routes (URLs)

app_name = 'Company'

urlpatterns = [
    	# General Page Views
		url(r'^homepage/$', CompanyHomepage.as_view(), name='homepage'),
]
