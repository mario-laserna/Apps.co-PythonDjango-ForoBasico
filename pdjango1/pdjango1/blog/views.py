# Create your views here.

from django.http import HttpResponse
from blog.models import Entrada

def index(request):
    #return HttpResponse("Bienvenido al blog")
    verentradas = Entrada.objects.all().order_by('-fecha')[:5]
    output = ', '.join([p.titulo for p in verentradas])
    return HttpResponse(output) 
    
