from django.shortcuts import render, redirect, HttpResponse
from .serializers import BookSerializer
from .models import BookList
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User1
from .serializers import UserSerializer
from .serializers import BookSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        print(request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
@api_view(['GET'])
def getData(request):
    app = BookList.objects.all()
    serializer = BookSerializer(app, many=True)
    print(serializer.data)
    return Response(serializer.data)
    # return Response()
def index(request):
    books = BookList.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)
@api_view(['POST'])
def create(request):
   if request.method == 'POST':
        print(request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # title = request.GET['title']
    # price = request.GET['price']
    # author = request.GET['author']
    # book_details = BookList(title=title, price=price, author=author)
    # book_details.save()
    # return redirect('/')


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        # email=rt@gmail.com
        print(request.data)
                # Find user by email
        # user = User1.objects.filter(email=email).first()
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            # Check if the password matches
            if user.check_password(password):
                # Password verified, generate JWT token
                token = generate_jwt_token(user)
                print(token)
                return Response({'token': token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

def generate_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
        
        
          # Print request data for debugging
        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # # Return detailed error response if validation fails
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         # Retrieve user object based on the provided email
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({'error': 'User does not exist'}, status=400)

#         # Authenticate user with the provided password
#         authenticated_user = authenticate(username=email, password=password)

#         if authenticated_user:
#             # If authentication is successful, generate JWT token
#             refresh = RefreshToken.for_user(authenticated_user)
#             return Response({'jwt_token': str(refresh.access_token)}, status=200)
#         else:
#             # If authentication fails, return error response
#             return Response({'error': 'Invalid credentials'}, status=400)
























def add_book(request):
    return render(request, 'add_book.html')



def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')

def edit(request, id):
    books = BookList.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'edit.html', context)


def update(request, id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')