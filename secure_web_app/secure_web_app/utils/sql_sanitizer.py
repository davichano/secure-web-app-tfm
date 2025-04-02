import re


class SQLSanitizer:
    """
    Clase para analizar y validar consultas SQL antes de su ejecución.
    """
    DANGEROUS_KEYWORDS = [
        "UNION", "SELECT", "INSERT", "DELETE", "DROP", "ALTER", "EXEC"
    ]

    def sanitize_and_execute(self, raw_sql, params, cursor):
        """
        Inspecciona y ejecuta una consulta SQL si es segura.

        :param raw_sql: Consulta SQL en formato de cadena.
        :param params: Lista o tupla de parámetros para la consulta.
        :param cursor: Cursor de la base de datos.
        :raises ValueError: Si se detecta una consulta peligrosa.
        """
        if self.is_dangerous(raw_sql):
            raise ValueError("Consulta SQL peligrosa detectada y bloqueada.")

        # Ejecutar la consulta segura
        cursor.execute(raw_sql, params)

    def is_dangerous(self, sql):
        """
        Valida si una consulta contiene palabras clave peligrosas.

        :param sql: Consulta SQL en formato de cadena.
        :return: True si se detecta una consulta peligrosa, False en caso contrario.
        """
        sql_upper = sql.upper()
        for keyword in self.DANGEROUS_KEYWORDS:
            if re.search(rf"\b{keyword}\b", sql_upper):
                return True
        return False
