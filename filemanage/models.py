from django.db import models
import uuid
import os


class Folder(models.Model):
    """
    Model to represent a folder for file management.
    """
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'folder'

    def __str__(self):
        return str(self.uid)


def get_upload_path(instance, filename):
    """
    Generate the upload path dynamically based on the folder's UID.
    """
    return os.path.join(str(instance.folder.uid), filename)


class Files(models.Model):
    """
    Model to represent files within a folder.
    """
    name = models.CharField(max_length=255)
    # URL is optional, can be empty
    url = models.URLField(blank=True, null=True)
    folder = models.ForeignKey(
        Folder, on_delete=models.CASCADE, related_name="files")
    # Dynamically generate upload path
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'files'

    def __str__(self):
        return self.name  # Return the name of the file instead of the path
