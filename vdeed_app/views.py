from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from vdeed_app.models import deeds
from vdeed_app.forms import deedsForm
from django.utils import timezone
from datetime import datetime, time

def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    print('current time', check_time)
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

# Create your views here.
def index(request):
    message1 = ''    

    submitted = False
    if request.method == 'POST':
        if 'btnform1' in request.POST:
            print('---btnform1---')
            form1 = deedsForm(request.POST)
            if form1.is_valid():
                print('---form1 valid---')
                #print('final deed', form1.cleaned_data['deed'])
                cd1 = form1.cleaned_data
                form1.save()
                # assert False
                return HttpResponseRedirect('/index?submitted=True')  
 
        print('empty post') 
        form1 = deedsForm()                      
    else:
        print('---GET---')
        form1 = deedsForm()
        if 'submitted' in request.GET:
            submitted = True

    all_deeds1 = deeds.objects.all().order_by('-date_time')
    #print(all_deeds1)
    if (all_deeds1):
        datetime = deeds.objects.values_list('date_time', flat=True).distinct()
        #print(datetime)
        messages = deeds.objects.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message1 = message1 + message

        #print('message1', message1)

    #form1 = deedsForm(hide_condition=True)          

    context = {}
 
    context['deed1'] = '<div class="mqcontainer">' + '<div class="marquee">' + message1 + '</div>' + '</div>'
    context['form1'] = form1

    now = timezone.now().strftime('%H:%M:%S') 
    show = is_time_between(time(14,00), time(14,30))
    print('show', show)
    print('time now ', now)
    if(show):
        context['hide'] = False
    else:
        context['hide'] = False
    
 
    return render(request, 'index.html', context)
 
