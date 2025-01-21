from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Micronutrient, NutrientFeedback
from .serializers import MicronutrientSerializer, MicronutrientDetailSerializer, NutrientFeedbackSerializer 

# Create your views here.
class MicronutrientList(APIView):
    def get(self, request):
        micronutrients = Micronutrient.objects.all()
        serializer = MicronutrientSerializer(micronutrients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MicronutrientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class MicronutrientDetail(APIView):
    def get_object(self,slug):
        try:
            return Micronutrient.objects.get(slug=slug)
        except Micronutrient.DoesNotExist:
            raise Http404
    
    def get(self, request, slug):
        micronutrient = self.get_object(slug)
        serializer = MicronutrientDetailSerializer(micronutrient)
        return Response(serializer.data)


class NutrientFeedbackList(APIView):
    def get(self, request):
        nutrient_feedback = NutrientFeedback.objects.all()
        serializer = NutrientFeedbackSerializer(nutrient_feedback, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NutrientFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class NutrientFeedbackDetail(APIView):
    def get_object(self,pk):
        try:
            return NutrientFeedback.objects.get(pk=pk)
        except NutrientFeedback.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        nutrient_feedback = self.get_object(pk)
        serializer = NutrientFeedbackSerializer(nutrient_feedback)
        return Response(serializer.data)