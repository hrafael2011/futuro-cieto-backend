
from rest_framework import viewsets
from .models import navigation, news, educations, logo, missionValues, whoWeAre, banner, event, causes, collaborator, video, reflectionByJose, contact, currency, accountBank
from .serializer import (navSerializer, 
                         newsSerializer, 
                         educationSerializer, 
                         logoSerializer, 
                         missionValuesSerializer, 
                         whoWeAreSerializer, 
                         bannerSerializer, eventSerializer, 
                         causeSerializer,
                           collaboratorSerializer,
                           videoSerializer,
                           reflectionSerializer,
                           contactSerializer, 
                           accountBankSerializer)



# Create your views here.
class navView(viewsets.ModelViewSet):
    queryset  = navigation.objects.filter(is_active=True)
    serializer_class = navSerializer

class newsView(viewsets.ModelViewSet):
    queryset = news.objects.filter(is_active=True)
    serializer_class = newsSerializer

class educationView(viewsets.ModelViewSet):
    queryset = educations.objects.filter(is_active=True)
    serializer_class = educationSerializer

class logoView(viewsets.ModelViewSet):
    queryset = logo.objects.filter(is_active=True)
    serializer_class = logoSerializer

class missionValueView(viewsets.ModelViewSet):
    queryset = missionValues.objects.filter(is_active=True)
    serializer_class = missionValuesSerializer

class whoWeAreView(viewsets.ModelViewSet):
    queryset = whoWeAre.objects.filter(is_active=True)
    serializer_class = whoWeAreSerializer

class bannerView(viewsets.ModelViewSet):
    queryset = banner.objects.filter(is_active=True).select_related('Url')
    serializer_class = bannerSerializer

class eventView(viewsets.ModelViewSet):
    queryset = event.objects.filter(is_active=True)
    serializer_class = eventSerializer

class causeView(viewsets.ModelViewSet):
    queryset = causes.objects.filter(is_active=True)
    serializer_class = causeSerializer


class collaboratorView(viewsets.ModelViewSet):
    queryset = collaborator.objects.filter(is_active=True)
    serializer_class = collaboratorSerializer



class videoView(viewsets.ModelViewSet):
    queryset = video.objects.filter(is_active=True)
    serializer_class = videoSerializer

class reflectionView(viewsets.ModelViewSet):
    queryset = reflectionByJose.objects.filter(is_active=True)
    serializer_class = reflectionSerializer

class contactView(viewsets.ModelViewSet):
    queryset = contact.objects.filter(is_active=True)
    serializer_class = contactSerializer

class accountBankView(viewsets.ModelViewSet):
    queryset = accountBank.objects.filter(is_active=True).select_related('Currency')
    serializer_class = accountBankSerializer

class currencyView(viewsets.ModelViewSet):
    queryset = currency.objects.filter(is_active=True)
    