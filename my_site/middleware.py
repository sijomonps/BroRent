"""
Custom middleware for serving media files in production
"""
from django.conf import settings
from django.http import FileResponse, Http404
import os


class ServeMediaMiddleware:
    """
    Middleware to serve media files in production when Cloudinary is not configured
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only serve media files if not in DEBUG mode and path starts with MEDIA_URL
        if not settings.DEBUG and request.path.startswith(settings.MEDIA_URL):
            # Get the file path
            media_path = request.path[len(settings.MEDIA_URL):]
            file_path = os.path.join(settings.MEDIA_ROOT, media_path)
            
            # Check if file exists
            if os.path.exists(file_path) and os.path.isfile(file_path):
                return FileResponse(open(file_path, 'rb'))
            else:
                raise Http404("Media file not found")
        
        response = self.get_response(request)
        return response
