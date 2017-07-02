from django.shortcuts import render
from rest_framework import response,status
from rest_framework.decorators import api_view
import os
# Create your views here.
import json

def home(request):
	return render(request, 'home.html')

@api_view(['GET'])
def test(request):
	print('this is current path:',os.getcwd())
	jsondata = open('data.json')

	data = json.load(jsondata)
	jsondata.close()

	return response.Response(data,status = status.HTTP_200_OK)

def testhtml(request):
	return render(request,'testhtml.html')

def add_message(request):
	pass