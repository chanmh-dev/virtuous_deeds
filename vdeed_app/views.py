from django.shortcuts import render
from django.http import HttpResponseRedirect
from vdeed_app.models import deeds1, deeds2, deeds3
from vdeed_app.forms import deeds1Form, deeds2Form, deeds3Form, DateForm, Date2Form, Date3Form
from django.utils import timezone
from datetime import datetime, time
from . import config
import re

def mobile(request):

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False

def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current time
    check_time = check_time or datetime.now().time()
    print('current time', check_time)
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# Create your views here.
def index(request):
    message1 = ''
    message2 = ''
    message3 = ''

    txt1 = ""
    txt2 = ""
    txt3 = ""

    print('config', config.post_success)

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
                config.post_success = 1     
                # assert False
                return HttpResponseRedirect('/index?submitted=True')
        elif 'btnform2' in request.POST:
            print('---btnform2---')
            form2 = deeds2Form(request.POST)
            if form2.is_valid():
                print('---form2 valid---')
                cd2 = form2.cleaned_data
                form2.save()
                config.post_success = 1 
                # assert False
                return HttpResponseRedirect('/index?submitted=True')
        elif 'btnform3' in request.POST:
            print('---btnform3---')
            form3 = deeds3Form(request.POST)
            if form3.is_valid():
                print('---form3 valid---')
                cd3 = form3.cleaned_data
                form3.save()
                config.post_success = 1                
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
        date_time1 = deeds1.objects.values_list('date_time', flat=True).distinct()
        #print(date_time)
        all_messages = deeds1.objects.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message1 = message1 + message
            txt = cleanhtml(message) + "\r\r"
            txt1 = txt1 + txt
        #print('message1', message1)

    #form1 = deeds1Form(hide_condition=True)

    all_deeds2 = deeds2.objects.all().order_by('-date_time')
    #print(all_deeds1)
    if (all_deeds2):
        date_time2 = deeds2.objects.values_list('date_time', flat=True).distinct()
        #print(date_time)
        all_messages = deeds2.objects.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message2 = message2 + message
            txt = cleanhtml(message) + "\r\r"
            txt2 = txt2 + txt
        #print('message2', message2)

    #form2 = deeds2Form(hide_condition=True)

    all_deeds3 = deeds3.objects.all().order_by('-date_time')
    #print(all_deeds1)
    if (all_deeds3):
        date_time3 = deeds3.objects.values_list('date_time', flat=True).distinct()
        #print(date_time)
        all_messages = deeds3.objects.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message3 = message3 + message
            txt = cleanhtml(message) + "\r\r"
            txt3 = txt3 + txt
        #print('message1', message1)

    #form3 = deeds3Form(hide_condition=True)

    context = {}

    context['text1'] = '<textarea readonly rows="10" class="v-border" id="txt1area" style="width:100%">' + txt1 + '</textarea>'
    context['text2'] = '<textarea readonly rows="10" class="v-border" id="txt2area" style="width:100%">' + txt2 + '</textarea>'
    context['text3'] = '<textarea readonly rows="10" class="v-border" id="txt3area" style="width:100%">' + txt3 + '</textarea>'

    context['deed1'] = '<div class="mqcontainer">' + '<div class="marquee">' + message1 + '</div>' + '</div>'
    context['deed2'] = '<div class="mqcontainer">' + '<div class="marquee">' + message2 + '</div>' + '</div>'
    context['deed3'] = '<div class="mqcontainer">' + '<div class="marquee">' + message3 + '</div>' + '</div>'

    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3

    now = timezone.now().strftime('%H:%M:%S')
    now1 = datetime.now().time().strftime('%H:%M:%S')
    show = is_time_between(time(22,00), time(22,45))
    print('show', show)
    print('time now ', now)
    context['now'] = now
    if show:
        context['hide'] = False
    else:
        context['hide'] = False

    context['now1'] = now1

    if mobile(request):
        context['mobile'] = True
    else:
        context['mobile'] = False

    if config.post_success == 1:
        print('post success')
        context['post_success'] = True
        config.post_success = 0
    else:
        print('post failed')
        context['post_success'] = False        

    return render(request, 'index.html', context)


def view_offerings(request):
    message1 = ""
    message2 = ""
    message3 = ""

    txt1 = ""
    txt2 = ""
    txt3 = ""

    submitted = False

    total_deeds1_count = 0
    total_deeds2_count = 0
    total_deeds3_count = 0

    filtered_from_date1 = ""
    filtered_to_date1 = ""
    filtered_from_date2 = ""
    filtered_to_date2 =  ""
    filtered_from_date3 = ""
    filtered_to_date3 = ""

    all_deeds1 = deeds1.objects.all().order_by('-date_time')
    all_deeds2 = deeds1.objects.all().order_by('-date_time')
    all_deeds3 = deeds1.objects.all().order_by('-date_time')

    if request.method == 'POST':
        if 'btnform' in request.POST:
            print('---date form---')
            form = DateForm(request.POST)
            if form.is_valid():
                print('---date form valid---')
                filtered_from_date1 = form.cleaned_data.get('date1_from')
                filtered_to_date1 = form.cleaned_data.get('date1_to')
                # assert False
                #return HttpResponseRedirect('/past_offerings?submitted=True')

        if 'btnform2' in request.POST:
            form2 = Date2Form(request.POST)
            if form2.is_valid():
                print('---date2 form valid---')
                filtered_from_date2 = form2.cleaned_data.get('date2_from')
                filtered_to_date2 = form2.cleaned_data.get('date2_to')

        if 'btnform3' in request.POST:
            form3 = Date3Form(request.POST)
            if form3.is_valid():
                print('---date3 form valid---')
                filtered_from_date3 = form3.cleaned_data.get('date3_from')
                filtered_to_date3 = form3.cleaned_data.get('date3_to')
    else:
        print('---GET---')
        form = DateForm()
        form2 = Date2Form()
        form3 = Date3Form()
        if 'submitted' in request.GET:
            submitted = True

    if filtered_from_date1 != "":
        print('filtered_from_date not None')
        print("from date ", filtered_from_date1)
        print("to date ", filtered_to_date1)
        all_deeds1 = deeds1.objects.all().filter(date_time__range=[filtered_from_date1, filtered_to_date1]).order_by('-date_time')
    else:
        print('filtered_from_date None')
        all_deeds1 = deeds1.objects.all().order_by('-date_time')

    #print(all_deeds1)
    if (all_deeds1):
        #date_time1 = all_deeds1.values_list('date_time', flat=True).distinct()
        deed1_first_obj_date = deeds1.objects.first().date_time.strftime ("%d/%m/%Y")
        deed1_last_obj_date = deeds1.objects.last().date_time.strftime ("%d/%m/%Y")
        print('deed1_first_obj_date', deed1_first_obj_date)
        print('deed1_last_obj_date', deed1_last_obj_date)

        total_deeds1_count = all_deeds1.count()
        messages = all_deeds1.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message1 = message1 + message
            txt = cleanhtml(message) + "\r\r"
            txt1 = txt1 + txt

        #print('message1', message1)

    #form1 = deeds1Form(hide_condition=True)

    if filtered_from_date2 != "":
        print('filtered_from_date2 not None')
        print("from date ", filtered_from_date2)
        print("to date ", filtered_to_date2)
        all_deeds2 = deeds2.objects.all().filter(date_time__range=[filtered_from_date2, filtered_to_date2]).order_by('-date_time')
    else:
        print('filtered_from_date2 None')
        all_deeds2 = deeds2.objects.all().order_by('-date_time')

    #print(all_deeds1)
    if (all_deeds2):
        #date_time2 = all_deeds2.values_list('date_time', flat=True).distinct()
        #print(date_time)
        deed2_first_obj_date = deeds2.objects.first().date_time.strftime ("%d/%m/%Y")
        deed2_last_obj_date = deeds2.objects.last().date_time.strftime ("%d/%m/%Y")
        print('deed2_first_obj_date', deed2_first_obj_date)
        print('deed2_last_obj_date', deed2_last_obj_date)

        total_deeds2_count = all_deeds2.count()
        messages = all_deeds2.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message2 = message2 + message
            txt = cleanhtml(message) + "\r\r"
            txt2 = txt2 + txt

        #print('message2', message2)

    #form2 = deeds2Form(hide_condition=True)

    if filtered_from_date3 != "":
        print('filtered_from_date3 not None')
        print("from date ", filtered_from_date2)
        print("to date ", filtered_to_date2)
        all_deeds3 = deeds3.objects.all().filter(date_time__range=[filtered_from_date3, filtered_to_date3]).order_by('-date_time')
    else:
        print('filtered_from_date3 None')
        all_deeds3 = deeds3.objects.all().order_by('-date_time')

    #print(all_deeds1)
    if (all_deeds3):
        #date_time3 = all_deeds3.values_list('date_time', flat=True).distinct()
        #print(date_time)
        deed3_first_obj_date = deeds3.objects.first().date_time.strftime ("%d/%m/%Y")
        deed3_last_obj_date = deeds3.objects.last().date_time.strftime ("%d/%m/%Y")
        print('deed3_first_obj_date', deed3_first_obj_date)
        print('deed3_last_obj_date', deed3_last_obj_date)

        total_deeds3_count = all_deeds3.count()
        messages = all_deeds3.values_list('deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message3 = message3 + message
            txt = cleanhtml(message) + "\r\r"
            txt3 = txt3 + txt

        #print('message1', message1)

    #form3 = deeds3Form(hide_condition=True)

    context = {}

    form = DateForm
    form2 = Date2Form
    form3 = Date3Form


    if filtered_from_date1 != "":
        context['filtered_from_date1'] = filtered_from_date1
        context['filtered_to_date1'] = filtered_to_date1
    else:
        context['filtered_from_date1'] = deed1_first_obj_date
        context['filtered_to_date1'] = deed1_last_obj_date

    if filtered_from_date2 != "":
        context['filtered_from_date2'] = filtered_from_date2
        context['filtered_to_date2'] = filtered_to_date2
    else:
        context['filtered_from_date2'] = deed2_first_obj_date
        context['filtered_to_date2'] = deed2_last_obj_date

    if filtered_from_date3 != "":
        context['filtered_from_date3'] = filtered_from_date3
        context['filtered_to_date3'] = filtered_to_date3
    else:
        context['filtered_from_date3'] = deed3_first_obj_date
        context['filtered_to_date3'] = deed3_last_obj_date

    context['total_deeds1_count'] = total_deeds1_count

    context['total_deeds2_count'] = total_deeds2_count

    context['total_deeds3_count'] = total_deeds3_count

    print('context_filtered_from_date1', context['filtered_from_date1'])

    context['form'] = form
    context['form2'] = form2
    context['form3'] = form3

    context['text1'] = '<textarea readonly rows="10" class="v-border" id="txt1area" style="width:100%">' + txt1 + '</textarea>'
    context['text2'] = '<textarea readonly rows="10" class="v-border" id="txt2area" style="width:100%">' + txt2 + '</textarea>'
    context['text3'] = '<textarea readonly rows="10" class="v-border" id="txt3area" style="width:100%">' + txt3 + '</textarea>'


    return render(request, 'view_offerings.html', context)
