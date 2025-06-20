# middleware.py
from fnmatch import fnmatch
from django.http import HttpResponseForbidden     
from accounts.models import userurlpermisson

class URLPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/logout/':
            return self.get_response(request)
        
        if request.user.is_authenticated and not request.user.is_superuser:
            path = request.path
            perms = userurlpermisson.objects.filter(user=request.user, permission=True)
            allowed = any(fnmatch(path, perm.url_pattern) for perm in perms)
            if not allowed:
                return HttpResponseForbidden("You do not have permission to access this URL.")
        return self.get_response(request)
