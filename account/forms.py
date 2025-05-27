# リスト4-29:新規作成。4.6.1 ユーザ認証のテスト実装、(4)手順4:
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    class meta:
        model = User
        fields = ["username", "password"]

#【リスト4-29の解説】
# 　リスト4-29はログインのフォームクラスLoginFormOを定義している。
# ここでは、リスト4-16:datashare/forms.pyと同じように、モデルを連携したフォームクラスを使用する。
# リスト4-16では、モデルpub_messageと連携したフォームクラスを定義するのに対し、
# リスト4-29はDjangoのユーザ管理モデルUserを使って(行2)、
# Userモデルのusernameとpasswordのフィールドを用いて、ログインフォームを定義する(行7)。
# また、フォームのひな型は、Djangoの認証フォーム「AuthenticationForm」を使用する(行1)。
