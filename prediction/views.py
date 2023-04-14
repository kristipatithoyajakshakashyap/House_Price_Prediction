from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
import pandas as pd
import csv
from . import ml_predict


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'prediction/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')
    return render(request, 'prediction/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def homePage(request):
    return render(request, 'prediction/home.html')


def housePrice(request):
    with open('F:/kavyamini/mini/prediction/templates/prediction/Bengaluru_House_Data.csv', 'r') as file:
        reader = csv.reader(file)
        data = []
        for i, row in enumerate(reader):
            if i == 0:
                headers = row
            else:
                data.append(row)
            if i == 100:
                break
    return render(request, 'prediction/housePrice.html', {'headers': headers, 'data': data})


def intro(request):
    return render(request, 'prediction/intro.html')


def prediction(request):
    return render(request, 'prediction/prediction.html')


def result(request):
    location = request.GET['loc']
    sqft = request.GET['sqft']
    bath = request.GET['bath']
    bhk = request.GET['bhk']
    prediction = ml_predict.predict_price(location, sqft, bath, bhk)
    context = {'prediction': round(prediction, 2), 'location': location, 'sqft': sqft, 'bath': bath, 'bhk':bhk}
    return render(request, 'prediction/result.html', context)
