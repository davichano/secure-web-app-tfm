from django.core.cache import cache
from datetime import timedelta

from django.http import HttpResponse


def BlockIpMiddleware(get_response):
    def middleware(request):
        ip = get_client_ip(request)
        failed_attempts = cache.get(ip, 0)
        if failed_attempts > 5:
            return HttpResponse("IP bloqueada temporalmente", status=403)
        return get_response(request)

    return middleware


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')
