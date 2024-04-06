from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    #### main url for rest_framework API #####
    path('api-auth/', include('rest_framework.urls')),
    ### connect all ticket app urls ####
    path('ticket/', include('ticket.urls')),

]
