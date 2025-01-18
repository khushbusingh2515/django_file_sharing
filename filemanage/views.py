from django.http import FileResponse
import os
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import FileListSerializer


# Define home view


def home(request):
    # Ensure 'home.html' exists in your templates directory
    return render(request, 'home.html')

# Define download view


def download(request, uid):
    return render(request, 'download.html', context={'uid': uid})

# Handle file upload


class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]  # Use MultiPartParser for file uploads

    def post(self, request):
        try:
            # Get the data from the request
            data = request.data

            # Initialize the serializer with the data
            serializer = FileListSerializer(data=data)

            # Validate the data and save it if valid
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Files uploaded successfully',
                    'data': serializer.data
                })

            # If validation fails, return errors
            return Response({
                'status': 400,
                'message': 'Validation failed',
                'data': serializer.errors
            })
        except Exception as e:
            # Log the error (you can use Django's logging framework)
            print(f"Error during file upload: {e}")
            return Response({
                'status': 500,
                'message': f"An error occurred: {str(e)}",
                'data': None
            })


# def download_file(request, file_id):
#     file_path = os.path.join(settings.MEDIA_ROOT, file_id,
#                              'download.svg')  # Adjust the path
#     if os.path.exists(file_path):
#         return FileResponse(open(file_path, 'rb'), content_type='image/svg+xml')
#     else:
#         raise Http404("File not found")
