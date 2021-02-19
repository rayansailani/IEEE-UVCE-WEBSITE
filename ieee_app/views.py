from django.http import HttpResponse
from django.shortcuts import render
import datetime
from events.models import Update
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control


def home(request):
    updates = Update.objects.all().order_by('created')
    updates = updates.filter(till_when__gte=datetime.date.today())
    today = datetime.date.today()
    context = {
        'updates': updates,
        "today": today,
    }
    return render(request, 'homepage.html', context)


def teams(request):
    return render(request, 'team.html')


def reg_form(request):
    return render(request, 'reg.html')


@cache_control(no_cache=True)
def rewards_1_view(request):
    return render(request, 'reward_1.html')
