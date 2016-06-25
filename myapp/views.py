from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from myapp.models import urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import hashlib

ARR = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_base(num, array=ARR):
    if(num==0):
        return array[0]
    retarr=[]
    base = len(array)
    while num:
        num, res = divmod(num,base)
        retarr.append(array[res])
    retarr.reverse()
    return ''.join(retarr)[:6]

def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)
 
def redirect_original(request, short_id):
    url = get_object_or_404(urls, pk=short_id) # get object, if not found return 404 error
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)
 
def shorten_url(request):
    url = request.POST.get("url", '')
    validate = URLValidator()
    url = url.lower()
    if not (url == ''):
        if url.startswith('https://'):
            url = "http://" + url[8:]
        if not (url.startswith('http://')):
            url = "http://" + url
        short_id = (hashlib.md5(url.encode())).hexdigest()
        short_id = int(short_id,16)
        short_id = encode_base(short_id)
        try :
            validate(url)
        except ValidationError, e:
            return HttpResponse(json.dumps({"inval":"Invalid URL"}),  content_type="application/json")
        b = urls(httpurl=url, short_id=short_id)
        b.save()
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")
