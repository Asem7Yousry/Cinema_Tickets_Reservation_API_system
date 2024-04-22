from django.shortcuts import render
from django.http import JsonResponse
from .models import Guest , Reservation , Movie
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , mixins , generics , viewsets , filters
from django.http import Http404

# 1_ without rest_framework or models (static json data)
def no_model_no_rest_framework(request):
    data = [
        {
            'id':1,
            'title':'df',
            'hall':'3c-4g',
            'duration': 2.5,
        },
        {
            'id':2,
            'title':'fdbsjks',
            'hall':'5e-2p',
            'duration': 1.5,
        },
    ]
    return JsonResponse(data,safe=False)

# 2_ no rest_framework but take query set from data base
def models_no_rest(request):
    ### get all data from models ###
    data = Movie.objects.all()
    ### put data in jason formate ###
    responced_data = {
        'Guests':list(data.values('title','hall','duration'))
    }
    ## responce data ##
    return JsonResponse(responced_data)

############ ############ using rest_framework  ########### #############

############ 1_ function based views    #############
    
## 1_ GET & POST ##
@api_view(['GET','POST'])
def list_post_objects(request): ### for movies 
    ### check method of request ###
    if request.method == 'GET':
        ## get all data from models (database) ##
        all_movies = Movie.objects.all()
        ## serialize on query set ##
        serialized_data = Movie_Serializer(all_movies , many=True)
        ## responce serialized data ##
        return Response(serialized_data.data)
    ### if method POST ###
    elif request.method == 'POST':
        #### deserialize request data ####
        deserialized_data = Movie_Serializer(data= request.data)
        ## check validation ##
        if deserialized_data.is_valid():
            ## save request data #3
            deserialized_data.save()
            ## response with deserialized data and status code ##
            return Response(deserialized_data.data , status= status.HTTP_201_CREATED)
        ### if deserialized_data was not valid ###
        return Response(deserialized_data.data , status= status.HTTP_400_BAD_REQUEST)
        

## 2_ GET(specific object) , PUT(edit) , DELETE
@api_view(['GET','PUT','DELETE'])
def object_processes(request, id):
    ### get specific object from model ###
    # check if object is exist in data base or not #
    try:
        specific_object = Movie.objects.get(id= id)
    ### if id not exist ###
    except Movie.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    ######### check on request method ##########
    ## if request method is GET ##
    if request.method == 'GET':
        ### serialize for object ###
        serialized_movie = Movie_Serializer(specific_object)
        ## responce serialized movie  ##
        return Response(serialized_movie.data)
    elif request.method == 'PUT':
        ### deserialized requested data ###
        deserialized_data = Movie_Serializer(specific_object,data= request.data)
        ## check validation ##
        if deserialized_data.is_valid():
            deserialized_data.save()
            ## responce with deserialized_data with status ##
            return Response(deserialized_data.data )
        return Response(deserialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    ### if method request is delete ###
    elif request.method == 'DELETE':
        specific_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############## 2_ class based views    ############# 

###### GET & POST methods ####
class List_movies(APIView):
    ### for GET method ###
    def get(self, request):
        ### queryset ###
        all_movies = Movie.objects.all()
        ### serialize queryset ###
        serializer = Movie_Serializer(all_movies , many= True)
        ### response all data ###
        return Response(serializer.data, status= status.HTTP_200_OK)
    ### for POST method ###
    def post(self, request):
        #### serialize data from request ####
        serializer = Movie_Serializer(data= request.data)
        ### check validation of requested data ###
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response(serializer.data , status= status.HTTP_400_BAD_REQUEST)
         
###### GET & PUT & DELETE methods ####
class Object_process(APIView):
    #### method that get object from model ####
    def get_object(self , id ):
        try:
            return Movie.objects.get(id= id)
        except  Movie.DoesNotExist:
            raise Http404
    ##### for GET request method ######
    def get(self , request , id):
        ### get object ###
        movie = self.get_object(id=id)
        ### serialize object ###
        serializer = Movie_Serializer(movie)
        ## response ##
        return Response(serializer.data, status= status.HTTP_200_OK)
    ##### for PUT request method ######
    def put(self , request , id):
        ### get object ###
        movie = self.get_object(id=id)
        ### serialize request data ###
        serializer = Movie_Serializer(movie , data= request.data)
        ### check validation ###
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    ##### for DELETE request method ######
    def delete(self , request , id):
        ### get object ###
        movie = self.get_object(id=id)
        ### delete object ###
        movie.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

##### ########  CBV by using mixins  ########## ######
##### endpoint to list all movies and post new movie #####
class list_movies_mixins(mixins.ListModelMixin, mixins.CreateModelMixin , generics.GenericAPIView):
    ##### get queryset and serializer ######
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer
    ### get method for all movies ###
    def get(self , request):
        return self.list(request)
    ### post method for new movie ###
    def post(self, request):
        return self.create(request)

####### endpoint to retrieve spesific movie and update and delete ######
class spesific_movie_mixins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    ##### queryset and serializer #######
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer
    ### retrieve method #####
    def get(self , request , pk):
        return self.retrieve(request)
    ### retrieve method #####
    def put(self , request , pk):
        return self.update(request)
    ### retrieve method #####
    def delete(self , request , pk):
        return self.destroy(request)

##### ########  CBV by using generics  ########## ######
##### endpoint to list all movies and post new movie #####
class ListMoviesGeneric(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer

####### endpoint to retrieve spesific movie and update and delete ######
class MovieProcessGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer

##### ########  CBV by using ViewSet  ########## ######
        ##### For Movies #####
##### endpoint to list all movies and post new movie besides retrieve spesific movie and update and delete #####
class Movie_ViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
        #### for guests ######
class GuestsViewset(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = Guest_Serializer

        #### for reservation ######
class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = Reservation_Serializer


