# Create your views here.
from django.http import HttpResponse
from artifacts.models import Artifact
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello, world. You're at artifacts."  )

def detail(request,artifact_id):

    try:
        a = Artifact.objects.get(id=artifact_id)
    except Artifact.DoesNotExist:
        raise Http404 

    next = a.id + 1
    previous = a.id - 1

    ##check if we're the last object
    try:
        Artifact.objects.get(id=str(a.id+1))
    except Artifact.DoesNotExist:
        next = 0

    ##render it
    return render_to_response("detail.html", {"artifact": a, "next" : next, "previous" : previous})
