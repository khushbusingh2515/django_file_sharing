from django.apps import AppConfig
import os
from django.conf import settings


class FilemanageConfig(AppConfig):
    name = 'filemanage'

    def ready(self):
        # Ensure the 'public/static' directory exists
        base_path = os.path.join(settings.BASE_DIR, 'public', 'static')
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        # Ensure the 'public/static/zip' directory exists
        zip_path = os.path.join(settings.BASE_DIR, 'public', 'static', 'zip')
        if not os.path.exists(zip_path):
            os.makedirs(zip_path)
