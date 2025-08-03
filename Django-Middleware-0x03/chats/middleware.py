from datetime import datetime, time
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}\n"
        
        with open("chats/requests.log", "a") as log_file:
            log_file.write(log_message)
        
        response = self.get_response(request)
        return response




class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now().time()
        allowed_start = time(18, 0) #6pm
        allowed_end = time(21, 0) #9pm

        if not (allowed_start <= now <= allowed_end):
            # Only restrict paths starting with /chat or similar, to avoid blocking admin etc.
            if request.path.startswith('/chat'):
                return HttpResponseForbidden("Access to the chat is only allowed between 6PM to 9PM.")
            
        return self.get_response(request)