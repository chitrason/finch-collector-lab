from django.contrib import admin
#import models
from .models import Finch, Feeding

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)

