# ✅ Django REST API Integration Exercise

## 🎯 Challenge

Your task is to build a simple API that interacts with a database model using Django REST Framework (DRF). The API will allow users to view and add items to the database.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to set up Django and Django REST Framework.
- How to create and configure API views using DRF.
- The process of serializing Django models for API responses.
- How to create API endpoints for viewing and adding items to the database.

## 👤 User Story

As a user of the Django REST API, I want to be able to view all items and add new items to the database through API endpoints so that I can manage my list effectively.

## ✅ Acceptance Criteria

- The API should have the following endpoints:
  - A `GET` endpoint to retrieve all items.
  - A `POST` endpoint to add a new item to the database.
- The API should use serializers to return data in JSON format.
- Responses should include appropriate status codes (e.g., `200 OK` for successful GET requests, `201 Created` for successful POST requests).
- The API should handle validation and errors for POST requests.

## 🛠️ Steps to Complete

1. **📁 Set up a new Django project**:
   - Install Django REST Framework:  
     ```bash
     pip install django djangorestframework
     ```
   
2. **📝 Configure Django REST Framework**:
   - Add `'rest_framework'` to the `INSTALLED_APPS` list in `settings.py`:
     ```python
     INSTALLED_APPS = [
         ...
         'rest_framework',
        ]
     ```

3. **📄 Define the database model**:
   - Create a new folder in root diretory called `api` and also necessary files like models.py, views.py, __init__.py, urls.py, In `api/models.py`, 

   example: create a model called `Item` with fields such as `name` and `created` or USE AN EXISTING MODEL:
     ```python
     from django.db import models

     class Item(models.Model):
         name = models.CharField(max_length=100)
         created = models.DateTimeField(auto_now_add=True)

         def __str__(self):
             return self.name
     ```

4. **🖊️ Create a serializer**:
   - In `api/serializers.py`, create a serializer class for the `Item` model. YOU CAN USE EXISTING MODEL AND JUST MAKE CHANGES ACCORDINGLY WITH THIS BELOW EXAMPLE, in place of Item you can use your modelname and in fields add your fields/attributes of model:
     ```python
     from rest_framework import serializers
     from .models import Item

     class ItemSerializer(serializers.ModelSerializer):
         class Meta:
             model = Item
             fields = ['id', 'name', 'created']
     ```

5. **📝 Implement views**:
   - In `api/views.py`, create views for listing items and adding new items, YOU CAN USE EXISTING MODEL AND JUST MAKE CHANGES ACCORDINGLY WITH THIS BELOW EXAMPLE:
     ```python
     from rest_framework.views import APIView
     from rest_framework.response import Response
     from rest_framework import status
     from .models import Item
     from .serializers import ItemSerializer

     # View for listing all items
     class ItemListView(APIView):
         def get(self, request):
             items = Item.objects.all()
             serializer = ItemSerializer(items, many=True)
             return Response(serializer.data)

     # View for adding a new item
     class AddItemView(APIView):
         def post(self, request):
             serializer = ItemSerializer(data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data, status=status.HTTP_201_CREATED)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     ```

6. **📄 Configure URLs**:
   - In `api/urls.py`, define URL patterns for the item list and add item endpoints, YOU CAN USE EXISTING MODEL AND JUST MAKE CHANGES ACCORDINGLY WITH THIS BELOW EXAMPLE:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('items/', views.ItemListView.as_view(), name='item-list'),
         path('items/add/', views.AddItemView.as_view(), name='add-item'),
     ]
     ```

   - In `myproject/urls.py`, include the `api` app's URLs:
     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('api/', include('api.urls')),
     ]
     ```

7. **🔄 Run migrations if any**: (OPTIONAL)
   - Make and apply migrations for any leftover model fields you added newly:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

8. **🔍 Test the API**:
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```
   - Open a browser or Postman:
     - To **view all items**, make a `GET` request to `http://localhost:8000/api/items/`.
     - To **add a new item**, make a `POST` request to `http://localhost:8000/api/items/add/` with the following JSON body:
       ```json
       {
         "name": "New Item"
       }
       ```

9. **💬 Comment your code**: Ensure each part of your code is clearly commented to explain its purpose.

## Additional Resources

- [Django Documentation: Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django Documentation: Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Documentation: Serializers](https://www.django-rest-framework.org/tutorial/3-class-based-views/#serializers)

## Submission

Once you complete the task, submit your entire Django project folder to your instructor.

Good luck, and happy coding!