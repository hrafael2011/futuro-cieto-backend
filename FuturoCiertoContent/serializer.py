from rest_framework import serializers
from django.utils.html import linebreaks
from .models import (navigation, 
                    news, 
                    educations, 
                    logo, 
                    missionValues, 
                    whoWeAre,
                    banner, 
                    event,
                    causes,
                    collaborator,
                    video,
                    reflectionByJose,
                    contact,
                    currency, 
                    accountBank)


class navSerializer(serializers.ModelSerializer):
    class Meta:
        model = navigation
        fields = ("NavId", "PageName","Url", "is_hidden")

class newsSerializer(serializers.ModelSerializer):
    formatted_text = serializers.SerializerMethodField()

    class Meta:
        model = news
        fields = ("NewID","formatted_text","Title","Content","Image", "TextAlt","CreateAt")

    def get_formatted_text(self, obj):
        # Usa `linebreaks` para que Django convierta los saltos de línea en HTML
        return linebreaks(obj.Content)

class educationSerializer(serializers.ModelSerializer):
    formatted_text = serializers.SerializerMethodField()


    class Meta:
        model = educations
        fields = ("EducationID","formatted_text","Title","Content","Image","TextAlt","CreateAt")
    def get_formatted_text(self, obj):
        # Usa `linebreaks` para que Django convierta los saltos de línea en HTML
        return linebreaks(obj.Content)


class logoSerializer(serializers.ModelSerializer):
    class Meta:
        model = logo
        fields = ("LogoID","Image","TextAlt")

class missionValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = missionValues
        fields = ("missionValuesID","Title_mission","Content_mission","Content_objetive","Title_objetive", "Content_mission", "Title_motivation","Content_motivation")

class whoWeAreSerializer(serializers.ModelSerializer):
    class Meta:
        model = whoWeAre
        fields = ("whoWeAreID","Title","Content")

class bannerSerializer(serializers.ModelSerializer):
 
    url_name = serializers.CharField(source='Url.Url', read_only=True)
    url_id = serializers.IntegerField(source='Url.NavId', read_only=True)  # Campo adicional para el ID

    class Meta:
        model = banner
        fields = ('BannerID','Image', 'url_name','url_id', 'TextAlt')

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ('EventID', 'Event','Address', 'EventDate', 'Image', 'TextAlt')

class causeSerializer(serializers.ModelSerializer):
    class Meta:
        model = causes
        fields = ('CauseID','Cause', 'Image','Title','Description','TextAlt')

class collaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = collaborator
        fields = ('CollaboratorID','Name', 'Image','Description','TextAlt')


class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ('VideoID','Title', 'VideoFile')

class reflectionSerializer(serializers.ModelSerializer):

    formatted_comment1 = serializers.SerializerMethodField()
    formatted_comment2 = serializers.SerializerMethodField()
    formatted_comment3 = serializers.SerializerMethodField()

    class Meta:
        model = reflectionByJose
        fields = ('ReflectionID','Comment1','Comment2','Comment3', 'Image', 'TextAlt', 'formatted_comment1', 'formatted_comment2', 'formatted_comment3')
    def get_formatted_comment1(self, obj):
        # Usa `linebreaks` para que Django convierta los saltos de línea en HTML
        return linebreaks(obj.Comment1)
    def get_formatted_comment2(self, obj):
        
        return linebreaks(obj.Comment2)
    def get_formatted_comment3(self, obj):
     
        return linebreaks(obj.Comment3)
    
class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ('ContactID','Phone', 'Email','LinkFacebook','LinkInstagram','LinkTweeter')


class accountBankSerializer(serializers.ModelSerializer):

    currency_name = serializers.CharField(source='Currency.Currency', read_only=True)
    currency_ID = serializers.IntegerField(source='Currency.CurrencyID', read_only=True)  # Campo adicional para el ID
    class Meta:
        model = accountBank
        fields = ('AccountID','Bank', 'Account','Currency','currency_name','currency_ID')

  