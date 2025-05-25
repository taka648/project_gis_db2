# リスト3-12:datashare/forms.py、3.4.1 フォームクラスの作成
from django import forms

class frmPublish(forms.Form):
    PROJECTS = (
        ("1", "地域防災関連"),
        ("2", "都市計画関連"),
        ("3", "地壌産婁関運"),
     )

    name = forms.CharField(label="Name", max_length=50)
    project = forms.ChoiceField(label="Project", choices=PROJECTS)
    contents = forms.CharField(label="Message", widget=forms.Textarea)

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
