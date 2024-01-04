from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView

from .forms import CustomUserCreationForm, BookForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = request.POST
        form = CustomUserCreationForm(data)
        print(form.data)
        if form.is_valid():

            try:
                user = form.save()
                print("saved2")
            except IntegrityError as e:
                print(f"Integrity Error: {e}")

        else:
            err = form.errors
            print(err)
            form = CustomUserCreationForm()

    return JsonResponse("saved", safe=False)


class BookCreateView(APIView):
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
