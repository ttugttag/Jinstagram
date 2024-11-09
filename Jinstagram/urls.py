"""Jinstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Sub
from content.views import Main
from user.views import Join
from django.conf import settings
from django.conf.urls.static import static
from chart.dash_apps.finished_apps import simpleexample
from chart.dash_apps.finished_apps import radio_usage
from chart.dash_apps.finished_apps import callback_usage
# from chart.dash_apps.finished_apps import Minimal_Dash_App
from chart.dash_apps.finished_apps import Connecting_to_Data
from chart.dash_apps.finished_apps import Update_Graphs_on_Hover
from chart.dash_apps.finished_apps import Generic_Crossfilter_Recipe
from chart.dash_apps.finished_apps import Plotly_Basic, Plotly_Advance

app_name = 'Jinstagram'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', Sub.as_view()),
    path('', Join.as_view(), name='Join'),
    path('main/', Main.as_view(), name='Main'),
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),
    path('chart/', include('chart.urls')),
    # path('chart/', Chart.as_view(), name='Chart'),

    # plottlyDash
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
