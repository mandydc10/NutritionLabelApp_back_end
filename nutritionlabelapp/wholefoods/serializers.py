from rest_framework import serializers
from django.apps import apps

class WholefoodFeedbackSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = apps.get_model('wholefoods.WholefoodFeedback')
        fields = '__all__'

class WholefoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('wholefoods.Wholefood')
        fields = '__all__'