# リスト3-5:datashare/views.py。3.3.2 複数ページのWebアプリのつながり、(1)手順1:views.pyの編集、redirect追加
# リスト3-1:datashare/views.py。3.3.1 初めてのDjangoアプリの作成、(1)手順1:views.pyの作成
from django.shortcuts import redirect, render

def index(request):
    parmas = {
        "title":"地理空間情報の共有サイト",
        "msg":"これはトッブページです。",
        # リスト3-5:追加
        "goto_mypage":"datashare:mypage",
    } 
    return render(request, "datashare/index.html", parmas)

# リスト3-5:追加
def mypage_funView(request):
    parmas = {
        "title":"地理空間情報の共有サイト",
        "msg":"これはマイページです。",
        "goto_index":"datashare:index",
    }
    return render(request, "datashare/mypage.html", parmas)

#【リスト3-1の解説】
# 　関数indexを定義し(行3)、辞書型の変数parmasの中に、titleとmsgの文字情報(行4～行7)をフォルダtemplates/datashareの下にあるindex.htmlファイルヘ返す(行8)。
# 現段階において、フォルダtemplates/datashareとファイルindex.htmlは存在していないが、後ほど作成する予定である。
# 　行3にあるdef index(request)は、indexというpython関数を宣言するコードである。引数requestは、クライアント側のリクエスト情報を受け取ることができる。
# また、行8のreturn render()は、renderという関数を使って、第3引数の変数parmas(行4～行7)をrendering(成形表現)した後、
# 第2引数のindex.htmlへreturn(返す)ためのコードである。そのため、行1にはDjangoライブラリからrender関数をimportしておく必要がある。
#【リスト3.5の解説】
# 　リスト3.5は、リスト3.1をベースに、
# (1)新たな関数mypage_funView()の追加(行11～行17)、
# (2)URLの逆引き機能の追加(行7と行15)を行う。
# 　それを実行すると、図3-15の左のトップページと右の「マイページ」が相互リンクしていることが反映される。
# 関数index()と関数mypage_funView()の構造上は全く同じであるので、行7と行15の逆引き機能の説明を除き、その他のコードに関する解説は省略する。
# 　リスト3-5の辞書型変数parmasにおいて、
# 'goto_mypage':'datashare:mypage'
# と
# 'goto_index':'datashare:index'(行7と行15)
# が追加された。ここで、datashare:mypageとdatashare:indexが示された定形の「アプリ名」:「ページ名」は名前空間(namespace)と呼ぶ。
# Djangoでは、名前空間を使用すると、ページの場所を特定することができる。それが名前空間を使ったURLと呼ばれる。
# その名前空間の定義については、次の手順2のdatashare/urls.py編集に解説する。名前空間の使用により、URLの逆引き機能が形成される。
# 　リスト3-5において、アプリdatashareにあるページindex.htmlとmypage.htmlが双方リンクし合うとき、
# 'goto_mypage':'datashare:mypage'(行7)と'goto_index':'datashare:index'(行15)の名前空間が使われる。
# こうした名前空間を利用したURLの逆引きは、通常のURLに関する詳細な記載は不要となり、記載ミスなどによる接続障害が避けられることで、
# システムの安定性とコードの可読性が向上させた。
# 　URLの逆引きはviews.py、datashare/urls.py、templates/index.htmlとtemplates/mypage.htmlの連携で実現されるので、
# 次はその順に説明していく。
