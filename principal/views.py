from django.shortcuts import render

# Create your views here.
from principal.models import Estado

def estadoData(request):
    estados = Estado.objects.all()
    data = {'estados':estados}
    return render(request,'estadoData.html',data)