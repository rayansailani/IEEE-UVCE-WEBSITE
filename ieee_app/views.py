from django.http import HttpResponse
from django.shortcuts import render
import datetime
from events.models import Update
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
import tweepy as tw

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
def covid_page(request):
    return render(request, 'covid.html')

@cache_control(no_cache=True)
def membershipBenefits(request):
    return render(request, 'membershipBenefits.html')

@cache_control(no_cache=True)
def rewards_1_view(request):
    return render(request, 'reward_1.html')

@cache_control(no_cache=True)
def ieeextreme(request):
    return render(request, 'ieeextreme.html')


def global_events_view(request):
    consumer_key= 'cA5ClFLWtmGRTIlwTuSCKPebZ'
    consumer_secret= 'OMp8YAq9JSWFnRfNep4bUb3Iejv4qDvUQlSFw9MfhD2ncIgsFa'
    access_token= '807235964766744576-Zzy6hNyOJBfVU0fUao7PPgEReVf7ZIy'
    access_token_secret= 'lhSZdeH6zNTCVdq6ybwt4ezEEfp4gtY6Q63KhiAkUoJAt'
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    tweet_information = [{
        'name':'IEEE Bangalore Section',
        'handle':'ieee_section',
        'tweets': api.user_timeline(screen_name = "ieee_section", count=10,include_rts = True, tweet_mode = 'extended'),
        'more':'https://twitter.com/ieee_section'
    },
    {
        'name':'IEEE Computer Society',
        'handle':'ComputerSociety',
        'tweets': api.user_timeline(screen_name = "ComputerSociety", count=10,include_rts = True, tweet_mode = 'extended'),
        'more':'https://twitter.com/ComputerSociety'
    },
    {
        'name':'IEEE PES',
        'handle':'ieee_pes',
        'tweets': api.user_timeline(screen_name = "ieee_pes", count=10,include_rts = True, tweet_mode = 'extended'),
        'more':'https://twitter.com/ieee_pes'
    },
    {
        'name':'IEEE PELS',
        'handle':'IEEEPELS',
        'tweets': api.user_timeline(screen_name = "IEEEPELS", count=10,include_rts = True, tweet_mode = 'extended'),
        'more':'https://twitter.com/IEEEPELS'
    },
    ]
    context = {"tweet_info":tweet_information }
    return render(request, "tweets.html", context)



