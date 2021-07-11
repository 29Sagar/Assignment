from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Client, Project
from datetime import datetime 
import datetime
from django.contrib.auth.models import User
from itertools import chain




# Create your views here.

# @login_required
@csrf_exempt
def index(request):
    try:
        current_user = request.user
        # print(current_user.username)
    except:
        return HttpResponse("The request is invalid: 404 Not Found",status=404)
    return HttpResponse("server is running...!!!",status=200)


# @login_required
@csrf_exempt
def clients(request):
    if request.method == "GET":
        try:
            current_user = request.user
            data = Client.objects.all()
        except:
            return HttpResponse("The request is invalid: 400 bad request",status=400)
        qs_json = serializers.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json',status=200)

    if request.method == "POST":
        try:
            data = request.POST
            user = User.objects.get(id=request.user.id)
            newClient = Client(client_name=data['client_name'], created_by=user)
            newClient.save()
                
        except:
            return HttpResponse("The request is invalid: 400 bad request",status=400)
        return HttpResponse("Client Created Successfully...!!!",status=200)



# @login_required
@csrf_exempt
def get_clients_id(request, id):
    if request.method == "GET":
        try:
            current_user = request.user
            data = Client.objects.filter(id=int(id))
            for d in data:
                data1 = Project.objects.filter(created_by=d.created_by)
        except:
            return HttpResponse("The request is invalid: 400 bad request",status=400)
        combined = list(chain(data, data1))

        json = serializers.serialize('json', combined)
        return HttpResponse(json, content_type='application/json',status=200)
        return HttpResponse("Data Created Successfully...!!!",status=200)
    

    if request.method == "PUT":
        try:
            data = request.body.decode('utf-8').split("=", 1)
            
            user = User.objects.get(id=request.user.id)
            updatedClient = Client.objects.filter(id=int(id)).update(client_name=data[1], created_by=user)
            
        except:
            return HttpResponse("The request is invalid: 400 bad request",status=400)
        return HttpResponse("Client Data Updated Successfully...!!!",status=200)

    if request.method == "DELETE":
        try:
            client_data = Client.objects.filter(id=int(id))
            client_data.delete()
        except:
            return HttpResponse("The request is invalid: 400 bad request",status=400)
        return HttpResponse("Client Data Deleted Successfully...!!!",status=204)



# @login_required
@csrf_exempt
def create_project(request, id):
    if request.method == "POST":
        try:
            data = request.POST
            Client_data = Client.objects.filter(id = int(id)).first()
            print("ClientDAta========",Client_data.created_by)
            user = User.objects.get(id=request.user.id)
            newProject = Project(project_name=data['project_name'], created_by=user)
            newProject.save()

        except:
            return HttpResponse("The request is invalid: 400 bad request",status=400)
        return HttpResponse("Project Created Successfully...!!!",status=200)



# @login_required
@csrf_exempt
def projects(request):
    if request.method == "GET":
        try:
            current_user = request.user
            # print("-----",current_user.id)
            data = Project.objects.filter(created_by = current_user.id)
        except:
            return HttpResponse("The request is invalid: 400 bad request",status=400)
        qs_json = serializers.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json',status=200)

