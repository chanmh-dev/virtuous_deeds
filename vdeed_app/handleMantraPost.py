from django.http import HttpResponseRedirect
from vdeed_app.models import mantra_recitation
from vdeed_app.forms import mantraRecitationForm


def handle_om_mani_padme_hum(request, user_id):
    print('---Om Mani Padme Hum---')
    form_mantra = mantraRecitationForm(request.POST)
    if form_mantra.is_valid():
        print('---form_mantra valid---')
        print(form_mantra.cleaned_data)
        all_mantra_recitation = mantra_recitation.objects.all()
        print('all_mantra_recitation', all_mantra_recitation)
        if (all_mantra_recitation):
            if all_mantra_recitation.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_mantra_recitation.filter(
                    user=user_id).count())
                obj = all_mantra_recitation.filter(user=user_id).first()
                current_om_mani_padme_hum_counter = obj.om_mani_padme_hum_counter
                print('current_om_mani_padme_hum_counter',
                      current_om_mani_padme_hum_counter)

                new_om_mani_padme_hum_counter = current_om_mani_padme_hum_counter + \
                    form_mantra.cleaned_data['om_mani_padme_hum_counter']
                print('new om_mani_padme_hum_counter',
                      new_om_mani_padme_hum_counter)

                print('update om mani padme hum sutra record')
                all_mantra_recitation.filter(user=user_id).update(
                    om_mani_padme_hum_counter=new_om_mani_padme_hum_counter)
            else:
                print('create om mani padme hum record')
                instance = form_mantra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first om mani padme hum record')
            instance = form_mantra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_mantra is not valid')
        print(form_mantra.errors)


def handle_manjushri_mantra(request, user_id):
    print('---Manjushri Mantra---')
    form_mantra = mantraRecitationForm(request.POST)
    if form_mantra.is_valid():
        print('---form_mantra valid---')
        print(form_mantra.cleaned_data)
        all_mantra_recitation = mantra_recitation.objects.all()
        print('all_mantra_recitation', all_mantra_recitation)
        if (all_mantra_recitation):
            if all_mantra_recitation.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_mantra_recitation.filter(
                    user=user_id).count())
                obj = all_mantra_recitation.filter(user=user_id).first()
                current_manjushri_mantra_counter = obj.manjushri_mantra_counter
                print('current_manjushri_mantra_counter',
                      current_manjushri_mantra_counter)

                new_manjushri_mantra_counter = current_manjushri_mantra_counter + \
                    form_mantra.cleaned_data['manjushri_mantra_counter']
                print('new manjushri_mantra_counter',
                      new_manjushri_mantra_counter)

                print('update manjushri mantra record')
                all_mantra_recitation.filter(user=user_id).update(
                    manjushri_mantra_counter=new_manjushri_mantra_counter)
            else:
                print('create manjushri mantra record')
                instance = form_mantra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first manjushri mantra record')
            instance = form_mantra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_mantra is not valid')
        print(form_mantra.errors)


def handle_green_tara_mantra(request, user_id):
    print('---Green Tara Sutra---')
    form_mantra = mantraRecitationForm(request.POST)
    if form_mantra.is_valid():
        print('---form mantra valid---')
        print(form_mantra.cleaned_data)
        all_mantra_recitation = mantra_recitation.objects.all()
        print('all_mantra_recitation', all_mantra_recitation)
        if (all_mantra_recitation):
            if all_mantra_recitation.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_mantra_recitation.filter(
                    user=user_id).count())
                obj = all_mantra_recitation.filter(user=user_id).first()
                current_green_tara_mantra_counter = obj.green_tara_mantra_counter
                print('current_green_tara_mantra_counter',
                      current_green_tara_mantra_counter)

                new_green_tara_mantra_counter = current_green_tara_mantra_counter + \
                    form_mantra.cleaned_data['green_tara_mantra_counter']
                print('new green_tara_mantra_counter',
                      new_green_tara_mantra_counter)

                print('update green tara mantra record')
                all_mantra_recitation.filter(user=user_id).update(
                    green_tara_mantra_counter=new_green_tara_mantra_counter)
            else:
                print('create green tara mantra  record')
                instance = form_mantra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first green tara mantra  record')
            instance = form_mantra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_mantra is not valid')
        print(form_mantra.errors)


def handle_migtsema(request, user_id):
    print('---Migtsema Sutra---')
    form_mantra = mantraRecitationForm(request.POST)
    if form_mantra.is_valid():
        print('---form_mantra valid---')
        print(form_mantra.cleaned_data)
        all_mantra_recitation = mantra_recitation.objects.all()
        print('all_mantra_recitation', all_mantra_recitation)
        if (all_mantra_recitation):
            if all_mantra_recitation.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_mantra_recitation.filter(
                    user=user_id).count())
                obj = all_mantra_recitation.filter(user=user_id).first()
                current_migtsema_counter = obj.migtsema_counter
                print('current_migtsema_counter',
                      current_migtsema_counter)

                new_migtsema_counter = current_migtsema_counter + \
                    form_mantra.cleaned_data['migtsema_counter']
                print('new current_migtsema_counter',
                      new_migtsema_counter)

                print('update migtsema record')
                all_mantra_recitation.filter(user=user_id).update(
                    migtsema_counter=new_migtsema_counter)
            else:
                print('create migtsema record')
                instance = form_mantra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first migtsema record')
            instance = form_mantra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_mantra is not valid')
        print(form_mantra.errors)
