from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Supervisor)
admin.site.register(Intern)
admin.site.register(Assign_task)
admin.site.register(Task_for_intern)
admin.site.register(Attendence)
