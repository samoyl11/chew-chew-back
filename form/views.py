from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FormSerializer
from .models import Form

class FormView(viewsets.ModelViewSet):
    serializer_class = FormSerializer
    queryset = Form.objects.all()
