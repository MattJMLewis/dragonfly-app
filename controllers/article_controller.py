from dragonfly import Controller
from dragonfly import View
from dragonfly import Response, RedirectResponse
from models.article import Article
from config import URL


class ArticleController(Controller):

    def index(self):
        return View("articles.index", articles=Article().all()).make()

    def show(self, id):
        return View("articles.show", article=Article().find(id)).make()

    def create(self):
        return View("articles.create").make()

    def edit(self, id):
        return View("articles.edit", article=Article().find(id)).make()

    def store(self, request_data):
        article = Article().create(request_data)
        return RedirectResponse(URL + f"/articles/{article.id}")

    def update(self, id, request_data):
        pass

    def delete(self, id):
        Article().delete()
