# Jungle Protein Lounge — menú web editable (Django)

## Qué incluye
- Menú público adaptable a celulares.
- Categorías, productos, descripciones, precios e imágenes administrables desde Django Admin.
- Datos iniciales de los productos y precios confirmados en la conversación.
- Preparado para añadir imágenes desde el panel de administración.
- El QR definitivo se genera cuando el sitio tenga una URL pública estable.

## Requisitos
- Python 3.10+
- Django 5.2
- Pillow (para subir imágenes)

## Ejecutar localmente
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_menu
python manage.py runserver
```
Abre:
- Menú: http://127.0.0.1:8000/
- Administración: http://127.0.0.1:8000/admin/

Desde Administración podrás crear/editar categorías, productos, precios, descripciones y fotos.

## Importante
Los precios marcados como confirmados en el proceso se incluyen abajo. Los sabores, salsas, toppings y algunos productos adicionales se cargan como elementos de menú sin precio individual o como notas, cuando el precio no quedó confirmado. Revísalos antes de publicar.
Para producción, configura `DEBUG=False`, `ALLOWED_HOSTS`, una clave secreta segura, almacenamiento de medios y una base de datos persistente. No subas contraseñas ni secretos a GitHub.
