from rest_framework import serializers
from django.apps import apps


class NutrientFeedbackSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = apps.get_model('micronutrients.NutrientFeedback')
        fields = '__all__'

class MicronutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('micronutrients.Micronutrient')
        fields = '__all__'

class MicronutrientDetailSerializer(MicronutrientSerializer):
    nutrient_feedback = NutrientFeedbackSerializer(many=True, read_only=True)
