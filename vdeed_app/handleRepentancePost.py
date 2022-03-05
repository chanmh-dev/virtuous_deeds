from django.http import HttpResponseRedirect
from vdeed_app.models import repentance
from vdeed_app.forms import repentanceForm


def handle_full_prostration(request, user_id):
    print('---Full Prostration---')
    form_repentance = repentanceForm(request.POST)
    if form_repentance.is_valid():
        print('---repentance valid---')
        print(form_repentance.cleaned_data)
        all_repentance = repentance.objects.all()
        print('all_repentance', all_repentance)
        if (all_repentance):
            if all_repentance.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_repentance.filter(
                    user=user_id).count())
                obj = all_repentance.filter(user=user_id).first()
                current_full_prostration_counter = obj.full_prostration_counter
                print('current_full_prostration_counter',
                      current_full_prostration_counter)

                new_full_prostration_counter = current_full_prostration_counter + \
                    form_repentance.cleaned_data['full_prostration_counter']
                print('new full_prostration_counter',
                      new_full_prostration_counter)

                print('update full prostration record')
                all_repentance.filter(user=user_id).update(
                    full_prostration_counter=new_full_prostration_counter)
            else:
                print('create full prostration record')
                instance = form_repentance.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first full prostration record')
            instance = form_repentance.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_repentance is not valid')
        print(form_repentance.errors)


def handle_half_prostration(request, user_id):
    print('---Half Prostration---')
    form_repentance = repentanceForm(request.POST)
    if form_repentance.is_valid():
        print('---repentance valid---')
        print(form_repentance.cleaned_data)
        all_repentance = repentance.objects.all()
        print('all_repentance', all_repentance)
        if (all_repentance):
            if all_repentance.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_repentance.filter(
                    user=user_id).count())
                obj = all_repentance.filter(user=user_id).first()
                current_half_prostration_counter = obj.half_prostration_counter
                print('current_half_prostration_counter',
                      current_half_prostration_counter)

                new_half_prostration_counter = current_half_prostration_counter + \
                    form_repentance.cleaned_data['half_prostration_counter']
                print('new half_prostration_counter',
                      new_half_prostration_counter)

                print('update half prostration record')
                all_repentance.filter(user=user_id).update(
                    half_prostration_counter=new_half_prostration_counter)
            else:
                print('create half prostration record')
                instance = form_repentance.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first half prostration record')
            instance = form_repentance.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_repentance is not valid')
        print(form_repentance.errors)


def handle_bow(request, user_id):
    print('---Bow---')
    form_repentance = repentanceForm(request.POST)
    if form_repentance.is_valid():
        print('---repentance valid---')
        print(form_repentance.cleaned_data)
        all_repentance = repentance.objects.all()
        print('all_repentance', all_repentance)
        if (all_repentance):
            if all_repentance.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_repentance.filter(
                    user=user_id).count())
                obj = all_repentance.filter(user=user_id).first()
                current_bow_counter = obj.bow_counter
                print('current_bow_counter',
                      current_bow_counter)

                new_bow_counter = current_bow_counter + \
                    form_repentance.cleaned_data['bow_counter']
                print('new bow_counter',
                      new_bow_counter)

                print('update bow record')
                all_repentance.filter(user=user_id).update(
                    bow_counter=new_bow_counter)
            else:
                print('create bow prostration record')
                instance = form_repentance.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first bow record')
            instance = form_repentance.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_repentance is not valid')
        print(form_repentance.errors)


def handle_recitation(request, user_id):
    print('---Recitation---')
    form_repentance = repentanceForm(request.POST)
    if form_repentance.is_valid():
        print('---repentance valid---')
        print(form_repentance.cleaned_data)
        all_repentance = repentance.objects.all()
        print('all_repentance', all_repentance)
        if (all_repentance):
            if all_repentance.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_repentance.filter(
                    user=user_id).count())
                obj = all_repentance.filter(user=user_id).first()
                current_recitation_counter = obj.recitation_counter
                print('current_recitation_counter',
                      current_recitation_counter)

                new_recitation_counter = current_recitation_counter + \
                    form_repentance.cleaned_data['recitation_counter']
                print('new recitation_counter',
                      new_recitation_counter)

                print('update recitation record')
                all_repentance.filter(user=user_id).update(
                    recitation_counter=new_recitation_counter)
            else:
                print('create recitation prostration record')
                instance = form_repentance.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first recitation record')
            instance = form_repentance.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_repentance is not valid')
        print(form_repentance.errors)
