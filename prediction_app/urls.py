from django.urls import path
from  . import views
#from api_app.views import CustomAuthToken
#from rest_framework.authtoken import views

urlpatterns = [
    path('ed74cf28e117c5f6dc9d4b8dfd76a7728d86000884abe0bffab1b9c881e0006ca6e057331ec536449b407bb0c5d4d947caff50d94e44772eccb6e6ad155e1a71/',views.index,name="index"),
    path('get_prediction_value/',views.get_prediction_value,name="get_prediction_value"),    
    path('get_prediction_table_data/',views.get_prediction_table_data,name="get_prediction_table_data"),
    path('get_token/',views.get_auth_token,name="get_auth_token"),        
    path('',views.login,name="login"),
    path('login/',views.login,name="login"),    
    path('logout/',views.logout,name="logout"),
    path('token_status/',views.token_status,name="token_status"),
    path('d7001cd8ba54d9f28d9b67be256a29ee4ed36da74d45055eaf0c4c0859c3ce9e62e8773ba7f77909b8dc3bd13ef0a67930f954bec6cdf4089013c2c2122e9e35/',views.token_error,name="token_error"),
    path('83f6dca96a652cbd4108901ba692a55e25274aa5eaca3692f9c447424c8115587a243fa783ed1c26de77b1e622db2e5938b4d40c7887eae0d7e8c9e6dc625687/',views.get_auth_token,name="login_auth"),
]
