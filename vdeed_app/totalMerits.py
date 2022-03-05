from vdeed_app.forms import repentanceForm, sutraRecitationForm, mantraRecitationForm
from vdeed_app.models import repentance, sutra_recitation, mantra_recitation
from django.db.models import Sum


def total_repentance(context):
    new_full_prostration_counter = 0
    new_half_prostration_counter = 0
    new_recitation_counter = 0
    new_bow_counter = 0
    form_repentance = repentanceForm()
    all_repentance = repentance.objects.all()
    #print('all_repentance', all_repentance)
    if (all_repentance):
        new_full_prostration_counter = repentance.objects.aggregate(
            Sum('full_prostration_counter'))['full_prostration_counter__sum']
        new_half_prostration_counter = repentance.objects.aggregate(
            Sum('half_prostration_counter'))['half_prostration_counter__sum']
        new_bow_counter = repentance.objects.aggregate(Sum('bow_counter'))[
            'bow_counter__sum']
        new_recitation_counter = repentance.objects.aggregate(
            Sum('recitation_counter'))['recitation_counter__sum']

    context['form_repentance'] = form_repentance
    print('full_prostration_counter', new_full_prostration_counter)
    context['full_prostration_counter'] = new_full_prostration_counter
    context['half_prostration_counter'] = new_half_prostration_counter
    context['bow_counter'] = new_bow_counter
    context['recitation_counter'] = new_recitation_counter


def total_sutra(context):
    new_mahaprajnaparamita_sutra_counter = 0
    new_heart_sutra_counter = 0
    new_medicine_buddha_sutra_counter = 0
    new_golden_light_sutra_counter = 0
    form_sutra_recitation = sutraRecitationForm()
    all_sutra_recitation = sutra_recitation.objects.all()
    #print('all_sutra_recitation', all_sutra_recitation)
    if (all_sutra_recitation):
        new_mahaprajnaparamita_sutra_counter = sutra_recitation.objects.aggregate(
            Sum('mahaprajnaparamita_sutra_counter'))['mahaprajnaparamita_sutra_counter__sum']
        new_heart_sutra_counter = sutra_recitation.objects.aggregate(
            Sum('heart_sutra_counter'))['heart_sutra_counter__sum']
        new_medicine_buddha_sutra_counter = sutra_recitation.objects.aggregate(Sum('medicine_buddha_sutra_counter'))[
            'medicine_buddha_sutra_counter__sum']
        new_golden_light_sutra_counter = sutra_recitation.objects.aggregate(
            Sum('golden_light_sutra_counter'))['golden_light_sutra_counter__sum']

    context['form_sutra_recitation'] = form_sutra_recitation
    context['mahaprajnaparamita_sutra_counter'] = new_mahaprajnaparamita_sutra_counter
    context['heart_sutra_counter'] = new_heart_sutra_counter
    context['medicine_buddha_sutra_counter'] = new_medicine_buddha_sutra_counter
    context['golden_light_sutra_counter'] = new_golden_light_sutra_counter


def total_mantra(context):
    new_om_mani_padme_hum_counter = 0
    new_manjushri_mantra_counter = 0
    new_green_tara_mantra_counter = 0
    new_migtsema_counter = 0
    form_mantra_recitation = mantraRecitationForm()
    all_mantra_recitation = mantra_recitation.objects.all()
    #print('all_mantra_recitation', all_mantra_recitation)
    if (all_mantra_recitation):
        new_om_mani_padme_hum_counter = mantra_recitation.objects.aggregate(
            Sum('om_mani_padme_hum_counter'))['om_mani_padme_hum_counter__sum']
        new_manjushri_mantra_counter = mantra_recitation.objects.aggregate(
            Sum('manjushri_mantra_counter'))['manjushri_mantra_counter__sum']
        new_green_tara_mantra_counter = mantra_recitation.objects.aggregate(Sum('green_tara_mantra_counter'))[
            'green_tara_mantra_counter__sum']
        new_migtsema_counter = mantra_recitation.objects.aggregate(
            Sum('migtsema_counter'))['migtsema_counter__sum']

    context['form_mantra_recitation'] = form_mantra_recitation
    context['om_mani_padme_hum_counter'] = new_om_mani_padme_hum_counter
    context['manjushri_mantra_counter'] = new_manjushri_mantra_counter
    context['green_tara_mantra_counter'] = new_green_tara_mantra_counter
    context['migtsema_counter'] = new_migtsema_counter
