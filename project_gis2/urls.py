# リスト3-2:project_gis/urls.py。3.3.1 初めてのDjangoアプリの作成、(2)手順2:ルーティングproject_gis/urls.pyへの追加
from django.contrib import admin
# リスト3-2:includeを追加
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # リスト3-2:追加
    path('datashare/', include('datashare.urls')),
]

# (2)手順2:ルーティングproject_gis/urls.pyへの追加とdatashare/urls.py(リスト3-3)の新規作成
# 　Djangoのルーティングは、ユーザのURLを認識し、処理経路を制御するための仕組みである(表3-1)。
# 具体的には、URLのパターンをプロジェクト側project_gis/urls.pyとアプリ側のdatashare/urls.pyを経由し、アプリdatashare側のviews.pyと紐づけをする(図3-11)。
# プロジェクト側のproject_gis/urls.pyは、プロジェクトが新規作成されたときに自動的に作られている(図3-6)が、
# 一方、アプリ側のdatashare/urls.pyは、新規作成の初期段階では存在しておらず(図3-8)、開発者が自ら作成する必要がある。
#【リスト3-2の解説】
# 　まず、DjangoのWebアプリに使われるURL構造を理解する必要がある。例えば、URLのhttp://localhost:8000/datashare/mypage/は3つの要索で構成される。
# 最初の「http://localhost:8000/」は、ホストサーバーのURLである。
# 次の「datashare/」は、project_gis/urls.pyに記載されているアプリのURLパターンを指す。
# 最後の「mypage/」は、datashare/urls.py[に]記載されるページのURLパターンである。
# 　よって、DjangoのWebアプリに使われるURLは、それぞれプロジェクトのURLパターンとアプリ側のURLパターンを結合したものである。
# 　リストの行4～行7には、リスト変数urlpatternsを用いて、複数の関数path()がリストされ、それぞれは特定のアプリヘの接続コードを記述している。
# 行5のコードは、ユーザ管理のアプリadminへの接続先を記載しているが、その詳細は第4章で説明する。
# 開発者が自ら入力する行6は、URLパターン'datashare/＇(第1引数)とアプリ側の'datashare/urls.py'(第2引数)、両者の紐付けを記述している。
# よって、プロジェクト側のproject_gis/urls.pyを読むと、図3-10でユーザがリクエストしたURLの前半部分のURLは、
# ホストサーバーのlocalhost:8000/とアプリのdatashare/であることが解読できる。
# URL後半部分のパターンは、第2引数のinclude('datashare.urls.py')により、アプリdatashare側のurl.pyから付け加えることになる。
# そのために、使用するinclude()関数を予めインポートする必要がある(行2の黒枠)。
