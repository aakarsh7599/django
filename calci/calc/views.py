from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'calc/home.html')

def calc(request):
    field1=int(request.GET['text1'])
    field2=int(request.GET['text2'])
    operation=request.GET['optradio']
    result=0
    if operation == '+':
        result = field1 + field2
    if operation == '-':
        result = field1 - field2
    if operation == 'X':
        result = field1 * field2
    if operation == '/':
        result = field1 / field2
    return render(request, 'calc/calc.html',{'result':result,'field1':field1,'field2':field2,'operation':operation})
