from django.shortcuts import render
# リスト3-13:追加
from datashare.forms import frmPublish
from django.views.generic import TemplateView

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
