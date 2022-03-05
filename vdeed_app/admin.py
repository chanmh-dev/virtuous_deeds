from django.contrib import admin
from .models import deeds1, deeds2, deeds3, globalLamrim2, repentance, sutra_recitation, mantra_recitation, counter_target
from django.http import HttpResponse
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# admin.site.register(deeds1)
# admin.site.register(deeds2)
# admin.site.register(deeds3)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                  for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class deeds1Resource(resources.ModelResource):
    class Meta:
        model = deeds1


class deeds1Admin(ImportExportModelAdmin, ExportCsvMixin):
    resource_class = deeds1Resource
    list_display = ("id", "name",  "date_time")
    list_filter = ("name", "date_time")
    #actions = ["export_as_csv"]


admin.site.register(deeds1, deeds1Admin)


class deeds2Resource(resources.ModelResource):
    class Meta:
        model = deeds2


class deeds2Admin(ImportExportModelAdmin, ExportCsvMixin):
    resource_class = deeds2Resource
    list_display = ("id", "name",  "date_time")
    list_filter = ("name", "date_time")
    #actions = ["export_as_csv"]


admin.site.register(deeds2, deeds2Admin)


@admin.register(deeds3)
class deeds3Admin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "name",  "date_time")
    list_filter = ("name", "date_time")
    #actions = ["export_as_csv"]


@admin.register(globalLamrim2)
class globalLamrim2Admin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "name",  "date_time")
    list_filter = ("name", "date_time")
    #actions = ["export_as_csv"]


@admin.register(repentance)
class repentanceAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "user",  "date_time", "full_prostration_counter",
                    "half_prostration_counter", "bow_counter", "recitation_counter")
    list_filter = ("user", "date_time", "full_prostration_counter",
                   "half_prostration_counter", "bow_counter", "recitation_counter")
    #actions = ["export_as_csv"]


@admin.register(sutra_recitation)
class sutraRecitationAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "user",  "date_time", "mahaprajnaparamita_sutra_counter",
                    "heart_sutra_counter", "medicine_buddha_sutra_counter", "golden_light_sutra_counter")
    list_filter = ("user", "date_time", "mahaprajnaparamita_sutra_counter",
                   "heart_sutra_counter", "medicine_buddha_sutra_counter", "golden_light_sutra_counter")
    #actions = ["export_as_csv"]


@admin.register(mantra_recitation)
class mantraRecitationAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "user",  "date_time", "om_mani_padme_hum_counter",
                    "manjushri_mantra_counter", "green_tara_mantra_counter", "migtsema_counter")
    list_filter = ("user", "date_time", "om_mani_padme_hum_counter",
                   "manjushri_mantra_counter", "green_tara_mantra_counter", "migtsema_counter")
    #actions = ["export_as_csv"]


@admin.register(counter_target)
class counterTargetAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "om_mani_padme_hum_target", "manjushri_mantra_target", "green_tara_mantra_target", "migtsema_target",
                    "mahaprajnaparamita_sutra_target", "heart_sutra_target", "medicine_buddha_sutra_target", "golden_light_sutra_target",
                    "full_prostration_target", "half_prostration_target", "bow_target", "recitation_target")

    list_filter = ("om_mani_padme_hum_target", "manjushri_mantra_target", "green_tara_mantra_target", "migtsema_target",
                   "mahaprajnaparamita_sutra_target", "heart_sutra_target", "medicine_buddha_sutra_target", "golden_light_sutra_target",
                   "full_prostration_target", "half_prostration_target", "bow_target", "recitation_target")
