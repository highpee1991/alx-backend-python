from datetime import datetime, time
from django.http import HttpResponseForbidden
from collections import defaultdict

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
    


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Structure: { ip: [timestamp1, timestamp2, ...] }
        self.ip_request_log = defaultdict(list)
        self.limit = 5  # Max messages
        self.time_window = 60  # seconds

    def __call__(self, request):
        # Only enforce on POST requests (like sending a chat message)
        if request.method == 'POST':
            ip = self.get_client_ip(request)
            now = time.time()

            # Clean up timestamps older than 1 minute
            self.ip_request_log[ip] = [
                ts for ts in self.ip_request_log[ip] if now - ts < self.time_window
            ]

            # Check limit
            if len(self.ip_request_log[ip]) >= self.limit:
                return HttpResponse("Rate limit exceeded. Try again later.", status=429)

            # Log this request
            self.ip_request_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        # This will use the correct IP behind a proxy if available
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip