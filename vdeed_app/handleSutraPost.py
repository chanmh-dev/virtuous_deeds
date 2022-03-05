from django.http import HttpResponseRedirect
from vdeed_app.models import sutra_recitation
from vdeed_app.forms import sutraRecitationForm


def handle_mahaprajnaparamita_sutra(request, user_id):
    print('---Mahaprajnaparamita Sutra---')
    form_sutra = sutraRecitationForm(request.POST)
    if form_sutra.is_valid():
        print('---form_sutra valid---')
        print(form_sutra.cleaned_data)
        all_sutra_recitation = sutra_recitation.objects.all()
        print('all_sutra_recitation', all_sutra_recitation)
        if (all_sutra_recitation):
            if all_sutra_recitation.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_sutra_recitation.filter(
                    user=user_id).count())
                obj = all_sutra_recitation.filter(user=user_id).first()
                current_mahaprajnaparamita_sutra_counter = obj.mahaprajnaparamita_sutra_counter
                print('current_mahaprajnaparamita_sutra_counter',
                      current_mahaprajnaparamita_sutra_counter)

                new_mahaprajnaparamita_sutra_counter = current_mahaprajnaparamita_sutra_counter + \
                    form_sutra.cleaned_data['mahaprajnaparamita_sutra_counter']
                print('new mahaprajnaparamita_sutra_counter',
                      new_mahaprajnaparamita_sutra_counter)

                print('update mahaprajnaparamita sutra record')
                all_sutra_recitation.filter(user=user_id).update(
                    mahaprajnaparamita_sutra_counter=new_mahaprajnaparamita_sutra_counter)
            else:
                print('create mahaprajnaparamita sutra record')
                instance = form_sutra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first mahaprajnaparamita sutra record')
            instance = form_sutra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_sutra is not valid')
        print(form_sutra.errors)


def handle_heart_sutra(request, user_id):
    print('---Heart Sutra---')
    form_sutra = sutraRecitationForm(request.POST)
    if form_sutra.is_valid():
        print('---form_sutra valid---')
        print(form_sutra.cleaned_data)
        all_sutra_recitation = sutra_recitation.objects.all()
        print('all_sutra_recitation', all_sutra_recitation)
        if (all_sutra_recitation):
            if all_sutra_recitation.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_sutra_recitation.filter(
                    user=user_id).count())
                obj = all_sutra_recitation.filter(user=user_id).first()
                current_heart_sutra_counter = obj.heart_sutra_counter
                print('current_heart_sutra_counter',
                      current_heart_sutra_counter)

                new_heart_sutra_counter = current_heart_sutra_counter + \
                    form_sutra.cleaned_data['heart_sutra_counter']
                print('new heart_sutra_counter',
                      new_heart_sutra_counter)

                print('update heart sutra record')
                all_sutra_recitation.filter(user=user_id).update(
                    heart_sutra_counter=new_heart_sutra_counter)
            else:
                print('create heart sutra record')
                instance = form_sutra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first heart sutra record')
            instance = form_sutra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_sutra is not valid')
        print(form_sutra.errors)


def handle_medicine_buddha_sutra(request, user_id):
    print('---Medicine Buddha Sutra---')
    form_sutra = sutraRecitationForm(request.POST)
    if form_sutra.is_valid():
        print('---form sutra valid---')
        print(form_sutra.cleaned_data)
        all_sutra_recitation = sutra_recitation.objects.all()
        print('all_sutra_recitation', all_sutra_recitation)
        if (all_sutra_recitation):
            if all_sutra_recitation.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_sutra_recitation.filter(
                    user=user_id).count())
                obj = all_sutra_recitation.filter(user=user_id).first()
                current_medicine_buddha_sutra_counter = obj.medicine_buddha_sutra_counter
                print('current_medicine_buddha_sutra_counter',
                      current_medicine_buddha_sutra_counter)

                new_medicine_buddha_sutra_counter = current_medicine_buddha_sutra_counter + \
                    form_sutra.cleaned_data['medicine_buddha_sutra_counter']
                print('new medicine_buddha_sutra_counter',
                      new_medicine_buddha_sutra_counter)

                print('update medicine buddha sutra record')
                all_sutra_recitation.filter(user=user_id).update(
                    medicine_buddha_sutra_counter=new_medicine_buddha_sutra_counter)
            else:
                print('create medicine buddha sutra record')
                instance = form_sutra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first medicine buddha sutra record')
            instance = form_sutra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_sutra is not valid')
        print(form_sutra.errors)


def handle_golden_light_sutra(request, user_id):
    print('---Golden Light Sutra---')
    form_sutra = sutraRecitationForm(request.POST)
    if form_sutra.is_valid():
        print('---form_sutra valid---')
        print(form_sutra.cleaned_data)
        all_sutra_recitation = sutra_recitation.objects.all()
        print('all_sutra_recitation', all_sutra_recitation)
        if (all_sutra_recitation):
            if all_sutra_recitation.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_sutra_recitation.filter(
                    user=user_id).count())
                obj = all_sutra_recitation.filter(user=user_id).first()
                current_golden_light_sutra_counter = obj.golden_light_sutra_counter
                print('current_golden_light_sutra_counter',
                      current_golden_light_sutra_counter)

                new_golden_light_sutra_counter = current_golden_light_sutra_counter + \
                    form_sutra.cleaned_data['golden_light_sutra_counter']
                print('new current_golden_light_sutra_counter',
                      new_golden_light_sutra_counter)

                print('update recitation record')
                all_sutra_recitation.filter(user=user_id).update(
                    golden_light_sutra_counter=new_golden_light_sutra_counter)
            else:
                print('create golden light sutra record')
                instance = form_sutra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first golden light sutra record')
            instance = form_sutra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_sutra is not valid')
        print(form_sutra.errors)
