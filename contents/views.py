from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import ContentSerializer
from .models import Content

# Create your views here.
@csrf_exempt
def index(request):
  if request.method == 'GET':
    contents = Content.objects.all()
    serializer = ContentSerializer(contents, many=True)
    return JsonResponse(serializer.data, safe=False)