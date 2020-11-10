from django.http import HttpResponse
from django.shortcuts import render
import datetime
from events.models import Update


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
