from django.http import JsonResponse
from django.shortcuts import render
from dash.models import Order
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard.html', {})

def pivot_data(request):
        dataset = Order.objects.all()
        data = serializers.serialize('json', dataset)
        return JsonResponse(data, safe=False)
    
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username and password match the default values
        if username == 'admin' and password == 'password':
            # Redirect to dashboard upon successful login
            return redirect('dashboard')
        else:
            # Invalid username or password, display error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')