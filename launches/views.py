from django.shortcuts import render

def historico(request):
    return render(request, 'launches/historico.html')
