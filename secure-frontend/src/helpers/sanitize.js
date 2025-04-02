import DOMPurify from 'dompurify';

/**
 * Sanitiza contenido HTML para evitar vulnerabilidades XSS.
 * @param {string} content - El contenido HTML que se desea sanitizar.
 * @returns {string} - Contenido sanitizado.
 */
export function sanitize(content) {
    return DOMPurify.sanitize(content);
}
