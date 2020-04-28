from django.contrib import admin
from .models import School,Club,Circle,FormKuModel, FormKgModel, FormDuModel, FormRuModel
# Register your models here.
admin.site.register(School)
admin.site.register(Club)
admin.site.register(Circle)
admin.site.register(FormKuModel)
admin.site.register(FormKgModel)
admin.site.register(FormDuModel)
admin.site.register(FormRuModel)
