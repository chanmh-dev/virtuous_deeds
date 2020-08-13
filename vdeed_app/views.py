from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from vdeed_app.models import deeds1, deeds2, deeds3
from vdeed_app.forms import deeds1Form, deeds2Form, deeds3Form
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
    message2 = ''
    message3 = ''    

    submitted = False
    if request.method == 'POST':
        if 'btnform1' in request.POST:
            print('---btnform1---')
            form1 = deeds1Form(request.POST)
            if form1.is_valid():
                print('---form1 valid---')
                #print('final deed', form1.cleaned_data['deed'])
                cd1 = form1.cleaned_data
                form1.save()
                # assert False
                return HttpResponseRedirect('/index?submitted=True')
        elif 'btnform2' in request.POST:  
            print('---btnform2---')   
            form2 = deeds2Form(request.POST)
            if form2.is_valid():
                print('---form2 valid---')
                cd2 = form2.cleaned_data
                form2.save()
                # assert False
                return HttpResponseRedirect('/index?submitted=True')      
        elif 'btnform3' in request.POST:   
            print('---btnform3---')  
            form3 = deeds3Form(request.POST)
            if form3.is_valid():
                print('---form3 valid---')
                cd2 = form3.cleaned_data
                form3.save()
                # assert False
                return HttpResponseRedirect('/index?submitted=True')  
 
        print('empty post') 
        form1 = deeds1Form()
        form2 = deeds2Form() 
        form3 = deeds3Form()                       
    else:
        print('---GET---')
        form1 = deeds1Form()
        form2 = deeds2Form()
        form3 = deeds3Form()
        if 'submitted' in request.GET:
            submitted = True

    all_deeds1 = deeds1.objects.all().order_by('-date_time')
    #print(all_deeds1)
    if (all_deeds1):
        datetime = deeds1.objects.values_list('date_time', flat=True).distinct()
        #print(datetime)
        messages = deeds1.objects.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message1 = message1 + message

        #print('message1', message1)

    #form1 = deeds1Form(hide_condition=True)

    all_deeds2 = deeds2.objects.all().order_by('-date_time')
    #print(all_deeds1)
    if (all_deeds2):
        datetime = deeds2.objects.values_list('date_time', flat=True).distinct()
        #print(datetime)
        messages = deeds2.objects.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message2 = message2 + message

        #print('message2', message2)

    #form2 = deeds2Form(hide_condition=True) 

    all_deeds3 = deeds3.objects.all().order_by('-date_time')
    #print(all_deeds1)
    if (all_deeds3):
        datetime = deeds3.objects.values_list('date_time', flat=True).distinct()
        #print(datetime)
        messages = deeds3.objects.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message3 = message3 + message

        #print('message1', message1)

    #form3 = deeds3Form(hide_condition=True)                     

    context = {}
 
    context['deed1'] = '<div class="mqcontainer">' + '<div class="marquee">' + message1 + '</div>' + '</div>'
    context['deed2'] = '<div class="mqcontainer">' + '<div class="marquee">' + message2 + '</div>' + '</div>'
    context['deed3'] = '<div class="mqcontainer">' + '<div class="marquee">' + message3 + '</div>' + '</div>'
    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3

    now = timezone.now().strftime('%H:%M:%S') 
    show = is_time_between(time(14,00), time(14,30))
    print('show', show)
    print('time now ', now)
    if(show):
        context['hide'] = False
    else:
        context['hide'] = False
    
 
    return render(request, 'index.html', context)
 
