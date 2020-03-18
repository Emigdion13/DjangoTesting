from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article

class ArticleObjectMixin(object):
    model = Article
    
    def get_object(self):
        id = self.kwargs.get('pk')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_success_url(self):
    #    return '/'

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() #blog/modelname_list.html


class ArticleDetailView1(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all() #blog/modelname_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    #queryset = Article.objects.all() #blog/modelname_list.html
    #queryset = Article.objects.filter(id__get=1)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    
    def get(self, request, id, *args, **kwargs):
        print("Hiciste un get")
        return render(request, self.template_name, { "object" : get_object_or_404(Article, id=id) })


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    #success_url = '/'

    def get_object(self):
        print(self)
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_success_url(self):
    #    return '/'

class ArticleDeleteView(ArticleObjectMixin, DeleteView): #Use Mixin for common operations betwwen controllers
    template_name = 'articles/article_delete.html'
    #queryset = Article.objects.all() #blog/modelname_list.html
    #queryset = Article.objects.filter(id__get=1)

    def get_success_url(self):
        return reverse('articles:article-list')





#if id is not None: