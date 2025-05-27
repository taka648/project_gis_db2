# リスト4-17:追加。4.5.2 情報発信とファイルアップロードの機能実装、(2)手順2:
# リスト4-13:datashare/views.py。4.5 Webアプリケーションにおけるデータベース基本機能の実装、
# 4.5.1 情報表示とファイルダウンロードの機能実装、(1)手順1:追加
# リスト4-13:redirect追加
from django.shortcuts import redirect, render
# リスト3-13:追加
# リスト4-13:frmModelPublish追加
# from datashare.forms import frmPublish, frmModelPublish
from datashare.forms import frmPublish
from django.views.generic import TemplateView
# リスト4-13:追加
from .models import pub_message
# リスト4-17:追加
from .forms import frmModelPublish

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

# リスト4-17:追加。4.5.2 情報発信とファイルアップロードの機能実装、(2)手順2:
def publish_byModelfrmView(request):
    if (request.method == 'POST'):
        form = frmModelPublish(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("datashare:mypage_db")
        else:
            form = frmModelPublish()

    parmas = {
        "title":"地理空間情報の共有サイト",
        "msg":"これは投稿サイト(DB接続)です。",
        "form":frmModelPublish(),
        "goto_mypage_db":"datashare:mypage_db",
    }
    return render(request, "datashare/publish_db.html", parmas)

# リスト4-21:datashare/views.py、新規追加。4.5.3 情報更新と削除の機能実装、(1)手順1:
def edit(request, num):
    obj= pub_message.objects.get(id=num)
    if (request.method == "POST"):
        if "btn_update" in request.POST:
            form = frmModelPublish(request.POST, instance=obj)
            form.save()
            return redirect("datashare:mypage_db")
        elif "btn_delete" in request.POST:
            obj.delete()
            return redirect("datashare:mypage_db")
        elif "btn_back" in request.POST:
            return redirect("datashare:mypage_db")
    parmas = {
        "title":"地理空間情報の共有サイト",
        "msg":"これは投稿の編集サイトです。",
        "id":num,
        "form":frmModelPublish(instance=obj),
    } 
    return render(request, "datashare/edit.html", parmas)

# リスト4-13:新規作成
class mypage_dbView(TemplateView):
    template_name = 'datashare/mypage_db.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pub_message_list'] = pub_message.objects.all().order_by('id')

        context['title'] = '地理空間データの共有サイト'
        context['msg'] = 'これはマイページ(DB接続)です'
        context['goto_index'] = 'datashare:index'
        return context

# リスト3-13:datashare/views.py:56-75、3.4.2フォーム送信ためのビュークラスの作成
class frmPublishView(TemplateView):
    def __init__(self):
        self.parmas= {
            "title":"地理空間情報の共有サイト",
            "msg":"これは、投稿ページです。",
            "form":frmPublish(),
            "answer":None,
            "goto_index":"datashare:index",
        } 

    def get(self, request):
        return render(request, "datashare/frmPublish.html", self.parmas)

    def post(self, request):
        person = request.POST['name']
        proj = request.POST['project']
        cont = request.POST['contents']
        self.params['answer'] = 'name=' + person + ', project=' + proj + ',contents=' + cont+ '.'
        self.params['form'] = frmPublish(request.POST)
        return render(request, "daashare/frmPublish.html", self.parmas)

#【リスト3-13の解説】
# 　まず、行2ではリスト3-122:datashare/forms.pyで作成したfrmPublishフォームクラスをインポートする。
# 続いて、行3は継承するための上位クラスTemplateViewをインポートする。
# 　次の関数__init__(self)は、Pythonクラスの初期関数であり、クラスインスクンスが作成されたときに、自動的に実行される関数である。
# ここで、self.parmasの変数を用いて、これまでと同じように、必要な変数とその値を用意する(行58～行64)。
# 　関数get()は、これまでの静的な配信コードと同じように、関数render()を用いてself.parmasの情報をテンプレートのpublish.htmlへ渡す(行66～行67)。
# 一方、関数post()は、関数request.POST()を用いて、ユーザがフォームに記述した情報を取得する(行70～行73)。
# 行74は、ユーザの回答を編集し、変数parmas['answer']へ渡す。また、フォームフィールドに記述情報が残されたままの状態で、
# フォームfrmPublish()を変数parmas['form']へ渡す。最後に、こうしたユーザ記述した情報self.parmasをもう一度テンプレートのpublish.htmlに送る(行75)。
#
#【リスト4-17の解説】
# 　まず、フォームクラスfrmModelPublishをインポートする(行5)。
# 次は、ビュー関数publish_byModelfrmView()を定義する(行78)。
# フォームの投稿ボタン(図4-38)が押され、request.methodが'POST'の状態になったとき(行79)、行80～行85のコードが実行される。
# 入力されたフォームを取得し(行80)、入カデータの検証を行う(行81)。
#
# もし入カデータに問題がなければ、form.saveでデータをデータベースに格納し(行82)、その後マイページmypage_db.htmlへ戻る(行83)。
# もし、入カデータに不備があったら、入カフォームは初期状態に戻る(行84)。
#
# 　ここで、モデルとの連携により、form.saveだけでフォームフィールドに入力されたデータをデータベースに格納できる。
# 　最後の変数parmasには、投稿ページpublish_db.htmlへ渡す情報をまとめている(行86～行91)。
# 最後に、変数parmasの情報を投稿ページへ渡す(行92)。
#
#【リスト4-21の解説】
# 　アフリケーションdatashareのviews.pyにedit関数を追記する(行92)。
# マイページの編集用ボタン(図4-41)がクリックされたとき、投稿情報のIDが関数の引数[num]から取得されている(行92)。
# このnumを用いて、行93の[pub_message.objects.get(id=num)]でテーブルから該当のレコードを抽出し、
# 変数objに入れる。次の条件文(行94～行103)には、図4-42の3つのボタンが押された時の処理を記述されている。
# まず、「変更」が押されたとき、[btn_update]のメッセージが送られる(行95)。
# そのとき、フォーム画面に入力された情報をformに入れ、form.saveでデータベースヘ格納する。
# その後、マイページへ戻る(行96～行98)。
# [削除]ボクンが押され、[btn_delete]が送られられ(行99)、[obj.delete()]で該当のレコードを削除し、
# マイページヘ戻る(行100～行101)。
# 最後に、[戻る]ボタンが押され、[btn_back]が送られたら(行102)、直ちにマイページヘ戻る(行103)。
# それ以下のコードは、これまでと同じく、変数parmasの情報を編集ページedit.htmlへ渡す。
