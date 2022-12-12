from ipware import get_client_ip
from django.http import HttpResponse

BLACK_LIST = ['127.0.0.4'
]

def ip_is_valid(get_response):

    def middleware(request):

        ip, is_routable = get_client_ip(request)

        if ip in BLACK_LIST:
            return HttpResponse('Bad request', status=404)
        else:
            return get_response(request)

    return middleware