from django.db import models
from django.contrib.auth.models import User


class deeds1(models.Model):
    deed = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class deeds2(models.Model):
    deed = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class deeds3(models.Model):
    deed = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class globalLamrim2(models.Model):
    deed = models.CharField(max_length=600)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class repentance(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    full_prostration_counter = models.PositiveIntegerField(default=0)
    half_prostration_counter = models.PositiveIntegerField(default=0)
    bow_counter = models.PositiveIntegerField(default=0)
    recitation_counter = models.PositiveIntegerField(default=0)

    full_prostration_target = models.PositiveIntegerField(default=0)
    half_prostration_target = models.PositiveIntegerField(default=0)
    bow_target = models.PositiveIntegerField(default=0)
    recitation_target = models.PositiveIntegerField(default=0)

    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class sutra_recitation(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    mahaprajnaparamita_sutra_counter = models.PositiveIntegerField(default=0)
    heart_sutra_counter = models.PositiveIntegerField(default=0)
    medicine_buddha_sutra_counter = models.PositiveIntegerField(default=0)
    golden_light_sutra_counter = models.PositiveIntegerField(default=0)

    mahaprajnaparamita_sutra_target = models.PositiveIntegerField(default=0)
    heart_sutra_target = models.PositiveIntegerField(default=0)
    medicine_buddha_sutra_target = models.PositiveIntegerField(default=0)
    golden_light_sutra_target = models.PositiveIntegerField(default=0)

    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class mantra_recitation(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    om_mani_padme_hum_counter = models.PositiveIntegerField(default=0)
    manjushri_mantra_counter = models.PositiveIntegerField(default=0)
    green_tara_mantra_counter = models.PositiveIntegerField(default=0)
    migtsema_counter = models.PositiveIntegerField(default=0)

    om_mani_padme_hum_target = models.PositiveIntegerField(default=0)
    manjushri_mantra_target = models.PositiveIntegerField(default=0)
    green_tara_mantra_target = models.PositiveIntegerField(default=0)
    migtsema_target = models.PositiveIntegerField(default=0)

    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class counter_target(models.Model):

    full_prostration_target = models.PositiveIntegerField(default=0)
    half_prostration_target = models.PositiveIntegerField(default=0)
    bow_target = models.PositiveIntegerField(default=0)
    recitation_target = models.PositiveIntegerField(default=0)

    mahaprajnaparamita_sutra_target = models.PositiveIntegerField(default=0)
    heart_sutra_target = models.PositiveIntegerField(default=0)
    medicine_buddha_sutra_target = models.PositiveIntegerField(default=0)
    golden_light_sutra_target = models.PositiveIntegerField(default=0)

    om_mani_padme_hum_target = models.PositiveIntegerField(default=0)
    manjushri_mantra_target = models.PositiveIntegerField(default=0)
    green_tara_mantra_target = models.PositiveIntegerField(default=0)
    migtsema_target = models.PositiveIntegerField(default=0)
