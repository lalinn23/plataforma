from django.urls import path
from users.api.views import RegisterView,UserView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


# #aqui agrego las rutas de la app usuarios
urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/obtener', UserView.as_view())

]

# urlpatterns = [
#     path('auth/register', RegisterView.as_view()),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#
# ]