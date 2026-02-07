from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializers

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
