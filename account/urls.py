# リスト4-32:新規作成。4.6.1 ユーザ認証のテスト実装、手順6:
from django.urls import path
from account.views import MyLoginView, MyLogoutView, TopView

app_name = "account"

urlpatterns = [
    path("", TopView.as_view(), name = "top"),
    path("login/", MyLoginView.as_view(), name = "login"),
    path("logout/", MyLogoutView.as_view(), name = "logout"),
]
