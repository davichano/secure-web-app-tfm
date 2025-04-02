from django.utils.deprecation import MiddlewareMixin
import re


class XSSEntrySanitizerMiddleware(MiddlewareMixin):
    MALICIOUS_PATTERNS = [
        r"<script.*?>.*?</script>",  # Detectar etiquetas <script>
        r"on\w+\s*=\s*[\"'].*?[\"']",  # Atributos de eventos JavaScript
        r"javascript:",  # Protocolo JavaScript en URLs
    ]

    def process_request(self, request):
        sanitized_params = self.sanitize_data(request.GET.dict())
        sanitized_params.update(self.sanitize_data(request.POST.dict()))
        request.GET = sanitized_params
        request.POST = sanitized_params

    def sanitize_data(self, data):
        sanitized = {}
        for key, value in data.items():
            for pattern in self.MALICIOUS_PATTERNS:
                value = re.sub(pattern, "[REDACTED]", value, flags=re.IGNORECASE)
            sanitized[key] = value
        return sanitized
