from django.urls import path , include
from .views import *

urlpatterns = [
    path('no_rest/',no_model_no_rest_framework),
    path('no_rest_using_model/', models_no_rest),
            ################ rest framework urls ###################

            ####################### FBV ###########################
    #### if method is GET & POST ######
    path('list_objects_and_post/', list_post_objects),
    #### if method is GET & PUT & DELETE ###### 
    path('list_objects_and_post/<int:id>', object_processes),

        ########################## CBV ##########################
    #### for GET (list objects) & POST methods #####
    path('cbv/list_movies/', List_movies.as_view()),
    #### for GET (one object by id) & PUT (update) & DELETE  methods #####
    path('cbv/list_movies/<int:id>', Object_process.as_view()),
    
            ########## by mixins ############
    #### for GET (list objects) & POST methods #####
    path('cbv/mixins/list_movies/', list_movies_mixins.as_view()),
    #### for GET (one object by id) & PUT (update) & DELETE  methods #####
    path('cbv/mixins/list_movies/<int:pk>', spesific_movie_mixins.as_view()),
    
]
