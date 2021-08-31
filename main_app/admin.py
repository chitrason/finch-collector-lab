from django.contrib import admin
#import models
from .models import Finch, Feeding, Toy

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Toy)

