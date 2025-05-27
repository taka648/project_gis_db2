# リスト3-12:datashare/forms.py、3.4.1 フォームクラスの作成
from django import forms
# リスト4-16:追加
from .models import pub_message


class frmPublish(forms.Form):
    PROJECTS = (
        ("1", "地域防災関連"),
        ("2", "都市計画関連"),
        ("3", "地壌産婁関運"),
     )

    name = forms.CharField(label="Name", max_length=50)
    project = forms.ChoiceField(label="Project", choices=PROJECTS)
    contents = forms.CharField(label="Message", widget=forms.Textarea)

# リスト4-16:追加。4.5.2 情報発信とファイルアップロードの機能実装、(1)手順1:アプリdatashareのforms.pyの記述追加
class frmModelPublish(forms.ModelForm):
    class Meta:
        model = pub_message
        fields = ['sender', 'project', 'send_message', 'send_document']



#【リスト3-12の解説】
#　Djangoのフォームクラスを定義する構文は、以下の基本構造を持っている。
#
# class フォームクラス名(forms.Form)
#     事前処理コード
#
#     変数名1 = forms.フィールドクラス1(引数1、引数2、...)
#     変数名2 = forms.フィールドクラス2(引数1、引数2、...)
#     ...略...
#
# 　リスト3-12は、django.forms.Formクラスを継承し、フォームクラスfrmPublishを定義する(行3)。
# 図3-22画面上の3つのコンポーネント(部品)は、行10～行12の3つのフォームフィールドクラス(form field class)を用いて定義する。
# 　最初のコンポーネントは、氏名を記述するためのテキストボックス(text box)である。これはforms.
# CharField()のフィールドクラスを用いて定義し、変数nameに保存する(行10)。
# 引数のlabel='Name'は、画面上のテキストボックスの左側ラベル「Name」となり(図3-22)、次の引数max_length=50は最大入力文字数を示す。
# 　次のコンポーネントは、関連プロジェクトを選択するためのドロップダウンリスト(drop down list)であり、
# これは変数projectとforms.ChoiceFeild()が、引数choices=PROJECTSは、ドロップダウンリストの表示内容を定義している。
# 配列型の変数PROJECTS(行4)には、行5から行7まで3つの選択肢を記述している。
# 　最後は、投稿メッセージを記入するためのテキストエリア(text area)である。
# これもforms.CharField()で定義し、引数widget=forms.Textareaを用いてテキストエリアを指定する。そのフィールドクラスは変数contentsで保存される。
#
# 【リスト4-16の解説】
# 　第3章のリスト3-12:datashare/forms.pyには、Djangoのforms.Formクラスを継承し、それぞれのフォームフィールドクラスを使って(行10～行12)、投稿フォームを作成した。
# リスト4-16は、それと違って、Djangoのモデルpub_messageと連携したフォームの作成方法を紹介する。
# 　Djangoのforms.ModelFormクラスを継承し、新たにフォームクラスfrmModelPublish()を宣言する(行17)。
# フォームフィールドの定義は、既存のモデルpub_messageの定義(リスト4-6:datashare/models.py)を参照している。
# そのため、行2ではモデルpub_messageをインポートし、行19のmodel=pub_messageでは、モデルの使用を宣言する。
# 行20は、モデルに定義したフィールドの中から、使用するフィールドを記述する。
# 　リスト3-12:datashare/forms.pyのforms.Formを用いたフォーム作成と比べ、リスト4-16に示すforms.ModelFormを用いたフォーム定義は、モデルが生かされたことで、
# コードはより簡潔になった。

