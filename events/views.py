from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Event
from accounts.models import Account
from django.contrib.auth.decorators import login_required
from . import forms
import datetime
from events.models import Update
from .forms import UpdateBlogPostForm
from events.forms import CreateUpdateForm
from django.conf import settings
User = settings.AUTH_USER_MODEL
# pagination display
# displays the likes
# displays all events that have been created so far


def events_list(request):
    events = Event.objects.all().order_by('-date')
    events = events.filter(is_approved=True)
    event_today = events.filter(date=datetime.date.today())
    eventold = events.filter(date__lt=datetime.date.today())
    eventnew = events.filter(date__gt=datetime.date.today())
    page = request.GET.get('page', 1)
    eventscount = eventold.count()
    print(eventscount)
    paginator = Paginator(eventold, 3)
    try:
        eventold = paginator.page(1)
    except:
        pass
    content = {
        'events': events,
        'event_today': event_today,
        'eventold': eventold,
        'eventnew': eventnew,
        'eventscount': eventscount,
        'three': 3,
    }
    return render(request, 'events/events_list.html', content)


def old_events_view(request):
    events = Event.objects.all().order_by('-date')
    eventold = events.filter(date__lt=datetime.date.today())
    context = {
        'eventold': eventold,
    }
    return render(request, 'events/events_old.html', context)

# displays indivisual views


def event_detail(request, slug):
    today = datetime.date.today()
    event = Event.objects.get(slug=slug)
    content = {
        'event': event,
        "today": today,
    }
    return render(request, 'events/events_detail.html', content)

# displays the view for adding an announcement for the website


@login_required(login_url="/accounts/login/")
def create_update(request):
    if request.user.is_sig_head:
        if request.user.is_sig_head:
            if request.method == 'POST':
                form = CreateUpdateForm(request.POST, request.FILES)
                if form.is_valid():
                    # save article to db
                    instance = form.save(commit=False)
                    instance.author = request.user
                    instance.save()
                    # change this to the dashboard later
                    return redirect('home_page')
            else:
                form = forms.CreateUpdateForm()
            return render(request, 'events/create_update.html', {'form': form})
        else:
            return redirect('home_page')


# displays the login credentials of the logged in student
@login_required(login_url="/accounts/login/")
def student_view(request):
    return render(request, 'events/dashboard_student.html')

# displays the event credentials of a logged in SIG head


@login_required(login_url="/accounts/login/")
def sig_view(request):
    user = request.user
    events = Event.objects.filter(author=user)
    approval = Event.objects.filter(is_approved=False).exclude(author=user)
    context = {
        'events': events,
    }
    if request.user.is_superuser or request.user == 'WEB DEV SIG IEEE' or request.user.username == 'Approval Team':
        context['approval'] = approval
    else:
        context['approval'] = None
    if request.user.is_sig_head:
        return render(request, 'events/events_dashboard.html', context)
    return redirect('articles:s_dashboard')

# displays the view to edit events


@login_required(login_url="/accounts/login/")
def edit_view(request, slug):
    context = {}
    if request.user.is_sig_head:
        event = get_object_or_404(Event, slug=slug)
        if request.POST:
            form = UpdateBlogPostForm(
                request.POST or None, request.FILES or None, instance=event)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                context['success_message'] = 'Updated '
                event = obj
                return redirect('articles:dashboard')
        else:
            form = UpdateBlogPostForm(
                initial={
                    "event_name": event.event_name,
                    'date': event.date,
                    'reg': event.reg,
                    'time': event.time,
                    'location': event.location,
                    'orgzer': event.orgzer,
                    'winners': event.winners,
                    'description': event.description,
                    'slug': event.slug,
                }
            )
        return render(request, 'events/edit.html', {'form': form})
    else:
        return redirect('articles:s_dashboard')

# displays the view to delete an event


@login_required(login_url="/accounts/login/")
def delete_view(request, slug):
    item = Event.objects.get(slug=slug)
    if request.POST:
        item.delete()
        return redirect('articles:dashboard')
    context = {
        'item': item,
    }
    return render(request, 'events/delete.html', context)

# displays the view to create an event


@login_required(login_url="/accounts/login/")
def event_create(request):
    # superusers = User.objects.filter(is_superuser=True)
    if request.user.is_sig_head:
        if request.method == 'POST':
            form = forms.CreateEvent(request.POST, request.FILES)
            if form.is_valid():
                # save article to db
                instance = form.save(commit=False)
                instance.author = request.user
                if request.user.is_superuser:
                    instance.is_approved = True
                    instance.approved_by = request.user
                instance.save()
                # change this to the dashboard later
                return redirect('articles:dashboard')
        else:
            form = forms.CreateEvent()
        return render(request, 'events/event_create.html', {'form': form})
    else:
        return redirect('home_page')

# approve view that approves the event


def approve_view(request, slug):
    item = Event.objects.get(slug=slug)
    if request.POST:
        item.is_approved = True
        item.approved_by = request.user.username
        item.save()
        return redirect('articles:dashboard')
    else:
        return redirect('articles:list')
