from django.shortcuts import render
from django.views.generic import ListView

from .mixins import TitleMixin, UserIsAdminCheckMixin

from .models import VipNetInfo
# Create your views here.


class VipNetInfoListView(TitleMixin, ListView):
    title = 'Список всех пользователей'
    model = VipNetInfo
    template_name = 'pc_list.html'
    ordering = ('-address')
