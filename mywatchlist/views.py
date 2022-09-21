from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_watchhlist = MyWatchlistItem.objects.all()
    context = {
        'list_film': data_watchhlist,
        'nama': 'Zanetta Aisha Dharmawan',
        'npm': '2106751846'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = MyWatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = MyWatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
