from django.contrib import admin
from .models import AboutMe, Services, Contact

# Register your models here.
admin.site.register(Services)
admin.site.register(AboutMe)
admin.site.register(Contact)