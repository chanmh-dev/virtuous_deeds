from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Sum
from vdeed_app.models import deeds1, deeds2, deeds3, globalLamrim2, repentance, sutra_recitation, mantra_recitation, counter_target
from vdeed_app.forms import deeds1Form, deeds2Form, deeds3Form, globalLamrim2Form, DateForm, Date2Form, Date3Form, Date4Form
from vdeed_app.forms import repentanceForm, sutraRecitationForm, mantraRecitationForm
from django.utils import timezone
from datetime import datetime, time
from . import config
from .handleRepentancePost import handle_full_prostration, handle_half_prostration, handle_bow, handle_recitation
from .handleSutraPost import handle_mahaprajnaparamita_sutra, handle_heart_sutra, handle_medicine_buddha_sutra, handle_golden_light_sutra
from .handleMantraPost import handle_om_mani_padme_hum, handle_manjushri_mantra, handle_green_tara_mantra, handle_migtsema

from .totalMerits import total_repentance, total_sutra, total_mantra
import re


def mobile(request):

    MOBILE_AGENT_RE = re.compile(
        r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

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
    else:  # crosses midnight
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
                # print('final deed', form1.cleaned_data['deed'])
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
    # print(all_deeds1)
    if (all_deeds1):
        date_time1 = deeds1.objects.values_list(
            'date_time', flat=True).distinct()
        # print(date_time)
        all_messages = deeds1.objects.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message1 = message1 + message
            txt = cleanhtml(message) + "\r\r"
            txt1 = txt1 + txt
        # print('message1', message1)

    # form1 = deeds1Form(hide_condition=True)

    all_deeds2 = deeds2.objects.all().order_by('-date_time')
    # print(all_deeds2)
    if (all_deeds2):
        date_time2 = deeds2.objects.values_list(
            'date_time', flat=True).distinct()
        # print(date_time)
        all_messages = deeds2.objects.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message2 = message2 + message
            txt = cleanhtml(message) + "\r\r"
            txt2 = txt2 + txt
        # print('message2', message2)

    # form2 = deeds2Form(hide_condition=True)

    all_deeds3 = deeds3.objects.all().order_by('-date_time')
    # print(all_deeds3)
    if (all_deeds3):
        date_time3 = deeds3.objects.values_list(
            'date_time', flat=True).distinct()
        # print(date_time)
        all_messages = deeds3.objects.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message3 = message3 + message
            txt = cleanhtml(message) + "\r\r"
            txt3 = txt3 + txt
        # print('message1', message1)

    # form3 = deeds3Form(hide_condition=True)

    context = {}

    context['text1'] = '<textarea readonly rows="10" class="v-border" id="txt1area" style="width:100%">' + txt1 + '</textarea>'
    context['text2'] = '<textarea readonly rows="10" class="v-border" id="txt2area" style="width:100%">' + txt2 + '</textarea>'
    context['text3'] = '<textarea readonly rows="10" class="v-border" id="txt3area" style="width:100%">' + txt3 + '</textarea>'

    context['deed1'] = '<div class="mqcontainer">' + \
        '<div class="marquee">' + message1 + '</div>' + '</div>'
    context['deed2'] = '<div class="mqcontainer">' + \
        '<div class="marquee">' + message2 + '</div>' + '</div>'
    context['deed3'] = '<div class="mqcontainer">' + \
        '<div class="marquee">' + message3 + '</div>' + '</div>'

    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3

    now = timezone.now().strftime('%H:%M:%S')
    now1 = datetime.now().time().strftime('%H:%M:%S')
    day = datetime.today().weekday() + 1
    print('day', day)
    show = is_time_between(time(22, 00), time(22, 45))
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
    filtered_to_date2 = ""
    filtered_from_date3 = ""
    filtered_to_date3 = ""

    all_deeds1 = deeds1.objects.all().order_by('-date_time')
    all_deeds2 = deeds1.objects.all().order_by('-date_time')
    all_deeds3 = deeds1.objects.all().order_by('-date_time')

    nameCount = deeds1.objects.order_by('name').values(
        'name').annotate(count=Count('id'))
    sortedName = sorted(nameCount, key=lambda k: k['count'], reverse=True)
    deeds1_top_five = list(sortedName)[:5]
    print(deeds1_top_five)

    nameCount = deeds2.objects.order_by('name').values(
        'name').annotate(count=Count('id'))
    sortedName = sorted(nameCount, key=lambda k: k['count'], reverse=True)
    deeds2_top_five = list(sortedName)[:5]
    print(deeds2_top_five)

    nameCount = deeds3.objects.order_by('name').values(
        'name').annotate(count=Count('id'))
    sortedName = sorted(nameCount, key=lambda k: k['count'], reverse=True)
    deeds3_top_five = list(sortedName)[:5]
    print(deeds3_top_five)

    if request.method == 'POST':
        if 'btnform' in request.POST:
            print('---date form---')
            form = DateForm(request.POST)
            if form.is_valid():
                print('---date form valid---')
                filtered_from_date1 = form.cleaned_data.get('date1_from')
                filtered_to_date1 = form.cleaned_data.get('date1_to')
                # assert False
                # return HttpResponseRedirect('/past_offerings?submitted=True')

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
        all_deeds1 = deeds1.objects.all().filter(
            date_time__range=[filtered_from_date1, filtered_to_date1]).order_by('-date_time')
    else:
        print('filtered_from_date None')
        all_deeds1 = deeds1.objects.all().order_by('-date_time')

    # print(all_deeds1)
    if (all_deeds1):
        # date_time1 = all_deeds1.values_list('date_time', flat=True).distinct()
        deed1_first_obj_date = deeds1.objects.first().date_time.strftime("%d/%m/%Y")
        deed1_last_obj_date = deeds1.objects.last().date_time.strftime("%d/%m/%Y")
        print('deed1_first_obj_date', deed1_first_obj_date)
        print('deed1_last_obj_date', deed1_last_obj_date)

        total_deeds1_count = all_deeds1.count()
        messages = all_deeds1.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message1 = message1 + message
            txt = cleanhtml(message) + "\r\r"
            txt1 = txt1 + txt

        # print('message1', message1)

    # form1 = deeds1Form(hide_condition=True)

    if filtered_from_date2 != "":
        print('filtered_from_date2 not None')
        print("from date ", filtered_from_date2)
        print("to date ", filtered_to_date2)
        all_deeds2 = deeds2.objects.all().filter(
            date_time__range=[filtered_from_date2, filtered_to_date2]).order_by('-date_time')
    else:
        print('filtered_from_date2 None')
        all_deeds2 = deeds2.objects.all().order_by('-date_time')

    # print(all_deeds1)
    if (all_deeds2):
        # date_time2 = all_deeds2.values_list('date_time', flat=True).distinct()
        # print(date_time)
        deed2_first_obj_date = deeds2.objects.first().date_time.strftime("%d/%m/%Y")
        deed2_last_obj_date = deeds2.objects.last().date_time.strftime("%d/%m/%Y")
        print('deed2_first_obj_date', deed2_first_obj_date)
        print('deed2_last_obj_date', deed2_last_obj_date)

        total_deeds2_count = all_deeds2.count()
        messages = all_deeds2.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message2 = message2 + message
            txt = cleanhtml(message) + "\r\r"
            txt2 = txt2 + txt

        # print('message2', message2)

    # form2 = deeds2Form(hide_condition=True)

    if filtered_from_date3 != "":
        print('filtered_from_date3 not None')
        print("from date ", filtered_from_date2)
        print("to date ", filtered_to_date2)
        all_deeds3 = deeds3.objects.all().filter(
            date_time__range=[filtered_from_date3, filtered_to_date3]).order_by('-date_time')
    else:
        print('filtered_from_date3 None')
        all_deeds3 = deeds3.objects.all().order_by('-date_time')

    # print(all_deeds1)
    if (all_deeds3):
        # date_time3 = all_deeds3.values_list('date_time', flat=True).distinct()
        # print(date_time)
        deed3_first_obj_date = deeds3.objects.first().date_time.strftime("%d/%m/%Y")
        deed3_last_obj_date = deeds3.objects.last().date_time.strftime("%d/%m/%Y")
        print('deed3_first_obj_date', deed3_first_obj_date)
        print('deed3_last_obj_date', deed3_last_obj_date)

        total_deeds3_count = all_deeds3.count()
        messages = all_deeds3.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message3 = message3 + message
            txt = cleanhtml(message) + "\r\r"
            txt3 = txt3 + txt

        # print('message1', message1)

    # form3 = deeds3Form(hide_condition=True)

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

    context['deeds1_top_five'] = deeds1_top_five
    context['deeds2_top_five'] = deeds2_top_five
    context['deeds3_top_five'] = deeds3_top_five

    return render(request, 'view_offerings.html', context)


def view_merits(request):
    full_prostration_target = 0
    half_prostration_target = 0
    bow_target = 0
    recitation_target = 0

    mahaprajnaparamita_sutra_target = 0
    heart_sutra_target = 0
    medicine_buddha_sutra_target = 0
    golden_light_sutra_target = 0

    om_mani_padme_hum_target = 0
    manjushri_mantra_target = 0
    green_tara_mantra_target = 0
    migtsema_target = 0

    context = {}
    first_counter_target_record = counter_target.objects.first()
    if(first_counter_target_record):
        full_prostration_target = first_counter_target_record.full_prostration_target
        half_prostration_target = first_counter_target_record.half_prostration_target
        bow_target = first_counter_target_record.bow_target
        recitation_target = first_counter_target_record.recitation_target

        mahaprajnaparamita_sutra_target = first_counter_target_record.mahaprajnaparamita_sutra_target
        heart_sutra_target = first_counter_target_record.heart_sutra_target
        medicine_buddha_sutra_target = first_counter_target_record.medicine_buddha_sutra_target
        golden_light_sutra_target = first_counter_target_record.golden_light_sutra_target

        om_mani_padme_hum_target = first_counter_target_record.om_mani_padme_hum_target
        manjushri_mantra_target = first_counter_target_record.manjushri_mantra_target
        green_tara_mantra_target = first_counter_target_record.green_tara_mantra_target
        migtsema_target = first_counter_target_record.migtsema_target

    total_repentance(context)
    total_sutra(context)
    total_mantra(context)

    context['full_prostration_target'] = full_prostration_target
    context['half_prostration_target'] = half_prostration_target
    context['bow_target'] = bow_target
    context['recitation_target'] = recitation_target

    context['mahaprajnaparamita_sutra_target'] = mahaprajnaparamita_sutra_target
    context['heart_sutra_target'] = heart_sutra_target
    context['medicine_buddha_sutra_target'] = medicine_buddha_sutra_target
    context['golden_light_sutra_target'] = golden_light_sutra_target

    context['om_mani_padme_hum_target'] = om_mani_padme_hum_target
    context['manjushri_mantra_target'] = manjushri_mantra_target
    context['green_tara_mantra_target'] = green_tara_mantra_target
    context['migtsema_target'] = migtsema_target

    print('view_merits')

    return render(request, 'view_merits.html', context)


@ login_required(login_url="/accounts/login")
def view_merits_detail(request, id=None):
    user_id = request.user.id
    print(request.user)
    print('page id =', id)
    print('user id =', user_id)

    if request.method == 'POST':
        print('request.POST', request.POST)
        print('---anchor tag---', request.POST.get('anchor-tag'))

        redirect_path = '/view_merits_detail/view_merits_detail/' + \
            str(user_id) + request.POST.get('anchor-tag')
        print(redirect_path)

        if 'btnFullProstration' in request.POST:
            handle_full_prostration(request, user_id)
        elif 'btnHalfProstration' in request.POST:
            handle_half_prostration(request, user_id)
        elif 'btnBow' in request.POST:
            handle_bow(request, user_id)
        elif 'btnRecitation' in request.POST:
            handle_recitation(request, user_id)
        elif 'btnMahaprajnaparamita' in request.POST:
            handle_mahaprajnaparamita_sutra(request, user_id)
        elif 'btnHeartSutra' in request.POST:
            handle_heart_sutra(request, user_id)
        elif 'btnMedicineBuddhaSutra' in request.POST:
            handle_medicine_buddha_sutra(request, user_id)
        elif 'btnGoldenLightSutra' in request.POST:
            handle_golden_light_sutra(request, user_id)
        elif 'btnOmManiPadmeHum' in request.POST:
            handle_om_mani_padme_hum(request, user_id)
        elif 'btnManjushriMantra' in request.POST:
            handle_manjushri_mantra(request, user_id)
        elif 'btnGreenTaraMantra' in request.POST:
            handle_green_tara_mantra(request, user_id)
        elif 'btnMigtsema' in request.POST:
            handle_migtsema(request, user_id)
        else:
            print('empty post')

        return HttpResponseRedirect(redirect_path)
    else:
        print('---GET---')
        if 'submitted' in request.GET:
            submitted = True

    context = {}

    new_full_prostration_counter = 0
    new_half_prostration_counter = 0
    new_bow_counter = 0
    new_recitation_counter = 0
    form_repentance = repentanceForm()
    all_repentance = repentance.objects.all()
    if (all_repentance):
        if all_repentance.filter(user=user_id).exists():
            obj = all_repentance.filter(user=user_id).first()
            new_full_prostration_counter = obj.full_prostration_counter
            new_half_prostration_counter = obj.half_prostration_counter
            new_bow_counter = obj.bow_counter
            new_recitation_counter = obj.recitation_counter

    print('full_prostration_counter', new_full_prostration_counter)
    context['full_prostration_counter'] = new_full_prostration_counter
    context['half_prostration_counter'] = new_half_prostration_counter
    context['bow_counter'] = new_bow_counter
    context['recitation_counter'] = new_recitation_counter

    context['form_repentance'] = form_repentance

    new_mahaprajnaparamita_sutra_counter = 0
    new_heart_sutra_counter = 0
    new_medicine_buddha_sutra_counter = 0
    new_golden_light_sutra_counter = 0
    form_sutra_recitation = sutraRecitationForm()
    all_sutra_recitation = sutra_recitation.objects.all()
    if (all_sutra_recitation):
        if all_sutra_recitation.filter(user=user_id).exists():
            obj = all_sutra_recitation.filter(user=user_id).first()
            new_mahaprajnaparamita_sutra_counter = obj.mahaprajnaparamita_sutra_counter
            new_heart_sutra_counter = obj.heart_sutra_counter
            new_medicine_buddha_sutra_counter = obj.medicine_buddha_sutra_counter
            new_golden_light_sutra_counter = obj.golden_light_sutra_counter

    print('mahaprajnaparamita_sutra_counter',
          new_mahaprajnaparamita_sutra_counter)
    context['mahaprajnaparamita_sutra_counter'] = new_mahaprajnaparamita_sutra_counter
    context['heart_sutra_counter'] = new_heart_sutra_counter
    context['medicine_buddha_sutra_counter'] = new_medicine_buddha_sutra_counter
    context['golden_light_sutra_counter'] = new_golden_light_sutra_counter

    context['form_sutra_recitation'] = form_sutra_recitation

    new_om_mani_padme_hum_counter = 0
    new_manjushri_mantra_counter = 0
    new_green_tara_mantra_counter = 0
    new_migtsema_counter = 0
    form_mantra_recitation = mantraRecitationForm()
    all_mantra_recitation = mantra_recitation.objects.all()
    #print('all_mantra_recitation', all_mantra_recitation)
    if (all_mantra_recitation):
        if all_mantra_recitation.filter(user=user_id).exists():
            obj = all_mantra_recitation.filter(user=user_id).first()
            new_om_mani_padme_hum_counter = obj.om_mani_padme_hum_counter
            new_manjushri_mantra_counter = obj.manjushri_mantra_counter
            new_green_tara_mantra_counter = obj.green_tara_mantra_counter
            new_migtsema_counter = obj.migtsema_counter

    print('om_mani_padme_hum_counter',
          new_om_mani_padme_hum_counter)
    context['om_mani_padme_hum_counter'] = new_om_mani_padme_hum_counter
    context['manjushri_mantra_counter'] = new_manjushri_mantra_counter
    context['green_tara_mantra_counter'] = new_green_tara_mantra_counter
    context['migtsema_counter'] = new_migtsema_counter

    context['form_mantra_recitation'] = form_mantra_recitation

    if user_id is not None:
        print('view_merits_detail')
        return render(request, 'view_merits_detail.html', context)
    else:
        print('view_merits')
        return render(request, 'view_merits.html', context)


@ login_required(login_url="/accounts/login")
def view_add_counter(request, id=None):
    user_id = request.user.id
    print(request.user)
    print('page id =', id)
    print('user id =', user_id)

    if request.method == 'POST':
        print('request.POST', request.POST)
        print('---anchor tag---', request.POST.get('anchor-tag'))

        redirect_path = '/view_add_counter/view_add_counter/' + \
            str(user_id) + request.POST.get('anchor-tag')
        print(redirect_path)

        if 'btnMigtsema' in request.POST:
            handle_migtsema(request, user_id)
        else:
            print('empty post')

        return HttpResponseRedirect(redirect_path)
    else:
        print('---GET---')
        if 'submitted' in request.GET:
            submitted = True

    context = {}

    new_om_mani_padme_hum_counter = 0
    new_manjushri_mantra_counter = 0
    new_green_tara_mantra_counter = 0
    new_migtsema_counter = 0
    form_mantra_recitation = mantraRecitationForm()
    all_mantra_recitation = mantra_recitation.objects.all()
    #print('all_mantra_recitation', all_mantra_recitation)
    if (all_mantra_recitation):
        if all_mantra_recitation.filter(user=user_id).exists():
            obj = all_mantra_recitation.filter(user=user_id).first()
            new_om_mani_padme_hum_counter = obj.om_mani_padme_hum_counter
            new_manjushri_mantra_counter = obj.manjushri_mantra_counter
            new_green_tara_mantra_counter = obj.green_tara_mantra_counter
            new_migtsema_counter = obj.migtsema_counter

    print('om_mani_padme_hum_counter',
          new_om_mani_padme_hum_counter)
    context['om_mani_padme_hum_counter'] = new_om_mani_padme_hum_counter
    context['manjushri_mantra_counter'] = new_manjushri_mantra_counter
    context['green_tara_mantra_counter'] = new_green_tara_mantra_counter
    context['migtsema_counter'] = new_migtsema_counter

    context['form_mantra_recitation'] = form_mantra_recitation

#############
    total_migtsema_counter = 0

    all_mantra_recitation = mantra_recitation.objects.all()
    if (all_mantra_recitation):
        total_migtsema_counter = mantra_recitation.objects.aggregate(
            Sum('migtsema_counter'))['migtsema_counter__sum']

    context['total_migtsema_counter'] = total_migtsema_counter

#############

    if user_id is not None:
        print('view_add_counter')
        return render(request, 'view_add_counter.html', context)
    else:
        print('view_merits')
        return render(request, 'view_merits.html', context)


def view_home(request):
    migtsema_target = 0
    context = {}

    first_counter_target_record = counter_target.objects.first()
    if(first_counter_target_record):
        migtsema_target = first_counter_target_record.migtsema_target

    total_migtsema_counter = 0

    all_mantra_recitation = mantra_recitation.objects.all()
    if (all_mantra_recitation):
        total_migtsema_counter = mantra_recitation.objects.aggregate(
            Sum('migtsema_counter'))['migtsema_counter__sum']

    context['total_migtsema_counter'] = total_migtsema_counter
    context['migtsema_target'] = migtsema_target

    print('total_migtsema_target', context['migtsema_target'])

    print('view_home')

    return render(request, 'view_home.html', context)
