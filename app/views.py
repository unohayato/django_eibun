# ListViewとDetailViewを取り込み
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# ListViewは一覧を簡単に作るためのView
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Post

# DetailViewは詳細を簡単に作るためのView
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = Post
    


# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    model = Post

    # 編集対象にするフィールド
    fields = ["title", "body"]



class Update(UpdateView):
    model = Post
    fields = ["title", "body"]