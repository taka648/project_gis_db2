# リスト4-17:追加。4.5.2 情報発信とファイルアップロードの機能実装、(3)手順3:
# リスト4-14:datashare/urls.py。4.5.1 情報表示とファイルダウンロードの機能実装、(2)手順2:記述追加
# リスト3-6:datashare/urls.py。3.3.2 複数ページのWebアプリのつながり、(2)手順2:urls.pyの編集
# リスト3-3:datashare/urls.py。3.3.1 初めてのDjangoアプリの作成、(2)手順2:ルーティングdatashare/urls.py(リスト3-3)の新規作成
from django.urls import path
from . import views

app_name = "datashare"

urlpatterns = [
   path("", views.index, name="index"),
   # リスト3-6:追加
   path("mypage/", views.mypage_funView, name="mypage"),
   # リスト3-14:追加、3.4.3 フォームビュークラスに紐付ける
   path("frmPublish/", views.frmPublishView.as_view(), name="frmPublish"),
   # リスト4-14:追加
   path("mypage_db/", views.mypage_dbView.as_view(), name="mypage_db"),
   # リスト4-17:追加。4.5.2 情報発信とファイルアップロードの機能実装、(3)手順3:
   path("publish_db/", views.publish_byModelfrmView, name="publish_db"),
]

# (2)手順2:ルーティングproject_gis/urls.pyへの追加とdatashare/urls.py(リスト3-3)の新規作成
# 　次に、アプリdatashare側のurls.pyを作成する。
#【リスト3-3の解説】
# 　前述のリスト3-2と同様、行6の関数path()が中心的な役割を果たしている。
# 第1引数のURLパターンは''(空白)であり、よってURLは'http://localhost=8000/datashare/'だけで、第2引数のviews.index関数と紐づけることになる。
# 行4のapp_name='datashare'と関数path()の第3引数name='index'は、URL逆引きとURLのnamespaceに関する記述であり、次の節でその意味を解説する。
#【リスト3.6の解説】
# 　行8にはmypage.htmlへのpathを追加する。ここでは、以下の2点を説明する。
# 　1つ目は、関数path()の第1引数の使い方である。関数path()の第1引数は、接続ページのURLパターンを記述する。
# 行7と行8には、それぞれ「''」と「'mypage'」と記載している。その結果、
# ページindex.htmへのURLはhttp://localhost:8OOO/datashare
# になり、
# マイページmypage.htmlへのURLはhttp://localhost:8000/datashare/mypage
# になる。つまり、第1引数のURLパターンは、実際のURL末端の部分に反映される。
# 　2つ目は名前空間を用いたURLの定義である。行4のapp_name='datashare'と、行7と行8の関数path()の第3引数であるname='index'とname='mypage'を用いて(図3-18)、
# Djangoアプリの名前空間を定義する。次に、定形の「アプリ名」:「ページ名」を使って、名前空間を用いたURL機能が実現される。
# リスト3-5:datashare/views.pyの'datashare:mypage'と'datashare:index'(行7と行15)では、名前空間を用いたURLが使われ、
# それぞれページmypageとページindexへのリックが明記されている。よって、名前空間は対象ページに名前を付け、通常のURL 
# http://localhost:8000/datashare
# と
# http://localhost:8000/datashare/mypage/
# の代わりに定形の「アプリ名」:「ページ名」を使うと、コードの簡潔性と可読性を格段に向上させることになる。
# 多数のページを有する複雑なアプリケーションにおいては名前空間の利用を勧める。
#
#【リスト3-14の解説】
# 　アプリのルーティングurls.pyファイルにおいて、フォーム処理するためのpath()を追加する。
# リスト3-14の行9のように、関数path()の3つの引数を記述する。
# URLパターンは'publish/'に、namespaceはname='publish'で設定するが、第2引数はこれまでとやや異なる。
# 行7と行8は、それぞれviewsの関数indexとmypageを紐付けるために、views.indexとviews.mypageで記述した。
# 今回のfrmPublishViewは、viewsの関数ではなくクラスであるので、frmPublishView.as_view()の記述でフォーラムクラスと紐付ける。
#
#【リスト4-14の解説】
# 　次は、URLとviewの紐付けを定義する。アプリケーションdatashareのurls.pyに、行10のpath関数を追加する。
# URLのdatashare/mypage_db/がリクエストされたとき、URLパターンのマッチングにより、行10の関数pathの第1引数の'mypage_db'が照会される。
# それによって、第2引数に記載されるviewクラスとの紐付けの指示により、リスト4-13のmypage_dbViewが参照される。
# また、第3引数のname='mypage_db'は、次の手順で作成するマイページmypage_db.htmlの名前をmypage_dbと定義し、名前空間URLの定形datashare:mypage_dbに使われる。
#
