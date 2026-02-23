from django.contrib import admin
from .models import Contact
from .serializers import ContactSerializer


# Register your models here.
admin.site.register(Contact)