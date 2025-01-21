# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Wholefood, WholefoodFeedback
from .serializers import WholefoodSerializer, WholefoodFeedbackSerializer

# Create your views here.
class WholefoodList(APIView):
    def get(self, request):
        wholefoods = Wholefood.objects.all()
        serializer = WholefoodSerializer(wholefoods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WholefoodSerializer(data=request.data)
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

class WholefoodDetail(APIView):
    def get_object(self, request):
        try:
            return Wholefood.objects.get(pk=pk)
        except Wholefood.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        wholefood = self.get_object(pk)
        serializer = WholefoodSerializer(wholefood)
        return Response(serializer.data)

class WholefoodFeedbackList(APIView):
    def get(self, request):
        wf_feedback = WholefoodFeedback.objects.all()
        serializer = WholefoodFeedbackSerializer(wf_feedback, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WholefoodFeedbackSerializer(data=request.data)
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

class WholefoodFeedbackDetail(APIView):
    def get_object(self, request):
        try:
            return WholefoodFeedback.objects.get(pk=pk)
        except WholefoodFeedback.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        wf_feedback_item = self.get_object(pk)
        serializer = WholefoodFeedbackSerializer(wf_feedback_item)
        return Response(serializer.data)
