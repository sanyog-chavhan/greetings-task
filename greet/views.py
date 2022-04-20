from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2

def index(request):
    ip_addr = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_addr:
        ip = ip_addr.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    g = GeoIP2()
    location = g.city(ip)
    location_country = location["country_name"]
    context = {
        "ip": ip,
        "location_country": location_country,
    }
    return render(request, "greeting.html", context)