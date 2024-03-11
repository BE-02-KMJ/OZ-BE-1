from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("", views.Users.as_view()),    # api/v1/users/
    path("myinfo", views.MyInfo.as_view()),    # api/v1/users/myinfo

    # Authentication
    path("getToken", obtain_auth_token), # username, password를 보내면 토큰을 반환 (DRF token)
    path("login", views.Login.as_view()),   # Django session login
    path("logout", views.Logout.as_view()), # Django session logout

    # JWT Authentication
    path("login/jwt", views.JWTLogin.as_view()), # JWT login
    path("login/jwt/info", views.UserDetailView.as_view()), # JWT API 인증

    # Simple JWT Authentication
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),

    # {
    # "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTM1Nzg5OSwiaWF0IjoxNzEwMTQ4Mjk5LCJqdGkiOiJlYTA5NWEzOTNiN2E0NGY1YTg0NDAyMTM5NmVkNjlhMSIsInVzZXJfaWQiOjF9.Iie260KUAWpH_H5cx6lzg7b0x82tQl41m2Ex6CRw9gg",
    # "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMTUxODk5LCJpYXQiOjE3MTAxNDgyOTksImp0aSI6IjgxZmM4MDM0MTJhOTRmM2VhMDI4ZjI4YTg2ZWNhZGRiIiwidXNlcl9pZCI6MX0.LIo_OOqx0r_ruZSZAk_kIFj9iNdjWMZyVQl3_ftH-hk"
    # }
]