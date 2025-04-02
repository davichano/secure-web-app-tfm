from django.utils.deprecation import MiddlewareMixin
import re


class SQLInjectionDetectionMiddleware(MiddlewareMixin):
    DANGEROUS_PATTERNS = [
        r"(?:'|\").*(?:--)|(;)|(--)",  # Comentarios y terminadores
        r"(?i)(union select|drop table|or 1=1|exec\(|select.*from|insert into|delete from|update.*set)",
        # Comandos SQL comunes
        r"(?i)\b(and|or)\b\s+\d+=\d+",  # Condiciones booleanas simples como 'AND 1=1'
    ]

    def process_request(self, request):
        try:
            params = request.GET.dict()
            params.update(request.POST.dict())
            for key, value in params.items():
                if self.is_dangerous(value):
                    return self.block_request(key, value)
        except Exception as e:
            # Loguea cualquier excepción inesperada
            print(f"Error en el middleware SQLInjectionDetectionMiddleware: {e}")
            return None

    def is_dangerous(self, value):
        """
        Verifica si un valor contiene patrones peligrosos.
        """
        for pattern in self.DANGEROUS_PATTERNS:
            if re.search(pattern, value):
                return True
        return False

    def block_request(self, key, value):
        """
        Devuelve una respuesta de error si se detecta una solicitud peligrosa.
        """
        from django.http import JsonResponse
        return JsonResponse({
            "error": f"Solicitud bloqueada: parámetro peligroso detectado en '{key}'"
        }, status=400)
