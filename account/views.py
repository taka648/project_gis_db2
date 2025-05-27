# リスト4-30:新規作成。4.6.1 ユーザ認証のテスト実装、(5)手順5:
from .forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TopView(LoginRequiredMixin, TemplateView):
    template_name = "account/top.html"

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"

class MyLogoutView(LogoutView):
    template_name = "account/logout.html"

#【リスト4-30の解説】
# 　ここでは、3つのビュークラスを定義する。
# 1つ目はトップページ用のTopView()である(行6～行7)。
# 第1引数の[LoginRequiredMixin]は、ユーザ認証の指定である。
# それを設定すると、トップページヘtop_htmlは「認証付き」のページになり、ユーザ認証が成功しない限り、
# ページヘのアクセスは不可になる。
# 第2引数は、すでに紹介したDjangoのビュークラスの親クラスである。
# ここに、第1引数と第2引数の順序は大切である。間違って逆にすると、
# トップページの前にログインページは開かない。行7はトップページtop.htmlへの紐付けを記述する。
# 　2つ目と3つ目は、それぞれログインページとログアウトページ用のビュークラスである。
# クラスMyLoginView()は、DjangoのLoginViewクラスを継承し(行9)、前に定義したLoginFormを使い(行10)、
# ログインページLogin.htmlと紐付ける(行11)。
# 同じように、クラスLogoutView()は、DjangoのLogoutViewクラスを継承し(行13)、フォームは使用せず、
# ログアウトページLogout.htmlと紐付ける。
