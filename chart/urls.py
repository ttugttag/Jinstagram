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
from . views import Index, Static, Light, MultiChart, Tables, Setting
from . views import AddData, ChangeChart
from . views import Plotly_Sample, Plotly_Basic, Plotly_Advance
from . views import Matplotlib_Sample, Matplotlib_Basic, Matplotlib_Advance

app_name = 'chart'

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('adddata/', AddData.as_view(), name='AddData'),
    path('changechart/', ChangeChart.as_view(), name='ChangeChart'),
    path('static/', Static.as_view(), name='Static'),
    path('light/', Light.as_view(), name='Light'),
    path('multichart/', MultiChart.as_view(), name='MultiChart'),
    path('tables/', Tables.as_view(), name='Tables'),
    path('setting/', Setting.as_view(), name='Setting'),

    path('plotly_sample/', Plotly_Sample.as_view(), name='Plotly_Sample'),
    path('plotly_basic/', Plotly_Basic.as_view(), name='Plotly_Basic'),
    path('plotly_advance/', Plotly_Advance.as_view(), name='Plotly_Advance'),

    path('matplotlid_sample/', Matplotlib_Sample.as_view(), name='Matplotlib_Sample'),
    path('matplotlid_basic/', Matplotlib_Basic.as_view(), name='Matplotlib_Basic'),
    path('matplotlid_advance/', Matplotlib_Advance.as_view(), name='Matplotlib_Advance'),
]
