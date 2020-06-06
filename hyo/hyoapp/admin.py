from django.contrib import admin
from hyoapp.models import Family, Member, Image
admin.site.register(Family)
admin.site.register(Member)
# Register your models here.
admin.site.register(Image)