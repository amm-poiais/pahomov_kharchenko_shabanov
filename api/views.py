from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsUser
from .serializers import DictionarySerializer, UserSerializer
from .models import Dictionary
from rest_framework import permissions


class CreateDictionaryView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsUser)

    def perform_create(self, serializer):
        """Save the post data when creating a new dictionary."""
        serializer.save()


class DetailsDictionaryView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsUser)


# class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     """This class handles the http GET, PUT and DELETE requests."""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (
#         permissions.IsAuthenticated,
#         IsUser)
#
#     def post(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def filter_queryset(self, queryset):
#         return self.request.user


class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self):
        try:
            return User.objects.get(pk=self.request.user.id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        user = self.get_object()
        try:
            history_words = request.data["history"].split(';')
            favorite_words = request.data["favorite"].split(';')
            main_words = request.data["main"].split(';')


            user.profile.history_words.clear()
            for word in history_words:
                try:
                    user.profile.history_words.add(
                        Dictionary.objects.get(word=word.strip().lower())
                    )
                except:
                    pass

            user.profile.favorite_words.clear()
            for word in favorite_words:
                try:
                    user.profile.favorite_words.add(
                        Dictionary.objects.get(word=word.strip().lower())
                    )
                except:
                    pass

            user.profile.main_words.clear()
            for word in main_words:
                try:
                    user.profile.main_words.add(
                        Dictionary.objects.get(word=word.strip().lower())
                    )
                except:
                    pass

            user.save()

        except Exception as ex:
             return Response(ex, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


    def delete(self):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateUserView(CreateAPIView):
    model = User()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

# class UserCreateView(generics.ListCreateAPIView):
#     """This class defines the create behavior of our rest api."""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def perform_create(self, serializer):
#         """Save the post data when creating a new user."""
#         serializer.save(username=self.request.user.username, password=self.request.user.password)
