from django.shortcuts import render
from django.http import JsonResponse

def alunos(request):

    if request.method == 'GET':
        alunos = {
            'id' : 1, 
            'nome':'Nicolas Vilela'
        }
        return JsonResponse(alunos)