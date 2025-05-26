# リスト4-6:datashare/models.py。4.4.2 データベースの設計とモデルの定義
from django.db import models
from django.contrib.auth.models import User, Group

class pub_message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Group, on_delete=models.CASCADE)
    send_message = models.CharField(max_length=1000)
    send_document = models.FileField(upload_to='documents/')
    send_date = models.DateTimeField(auto_now_add=True)

#【リスト4-6の解説】
# 　モデルは、pub_messageと名付け(行4)、Djangoモデルクラスmodels.Modelを継承している(行1)。行5から行9までは、5つのフィールドを定義している。
# 　フィールドsenderは、外部キーフィールド(models.Foreign Key)として、Userテーブルと関連付ける(行5)。
# 同じ方法で、フィールドprojectも外部キーとして、Groupテーブルをつなぐ(行6)。
# そのために、UserとGroupのモデルは、予めインプットしておく(行2)。
# 　フィールドsend_messageはmodels.CharFieldを用いて、文字列フィールドとして定義する(行7)。
# 　フィールドsend_documentはファイルアップロードをするために、models.Filefieldを使って定義する。
# 　最後のsend_dateは投稿日付を保存するために、models.DateTimeを用いて定義する。
