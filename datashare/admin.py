# リスト4-7:datashare/admin.py。(1)手順1:必要な環境設定、(1-A)モデルの登録
from django.contrib import admin
# リスト4-7:追加
from .models import pub_message

# リスト4-7:追加
admin.site.register(pub_message)

#【リスト4-7の解説】
# 　リスト4-66:datashare/models.pyで定義したモデルpub_messageをアプリケーションdatashareに登録する。
