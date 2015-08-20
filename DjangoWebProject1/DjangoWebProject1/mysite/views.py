#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from mysite.models import Article,Tag,Classification
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json


def index(request):
    return render(request, 'mysite/index.html')


def home(request):

     articles = Article.objects.all()
     paginator = Paginator(articles,6)#每个页面最多显示6篇文章
     page_num = request.GET.get('page')
     try:
         articles = paginator.page(page_num)
     except PageNotAnInteger:
         articles = paginator.page(1)
     except EmptyPage:
         articles = paginator.page(paginator.num_pages)


     #显示最新发布的前10篇文章
     #ar_newpost = Article.objects.order_by('-publish_time')[:10]
     

     classification = Classification.class_list.get_Class_list()#分类,以及对应的数目
     tagCloud = json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)#标签,以及对应的文章数目
     date_list = Article.date_list.get_Article_onDate()#按月归档,以及对应的文章数目
  
     return render_to_response('mysite/home.html',
            locals(), #它返回的字典对所有局部变量的名称与值进行映射。
            context_instance=RequestContext(request))


def detail(request, year,month,day,id):
    try:
       article = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
       raise Http404

    #ar_newpost = Article.objects.order_by('-publish_time')[:10]
    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)#标签,以及对应的文章数目
    date_list = Article.date_list.get_Article_onDate()

    return render_to_response('mysite/content.html',
            locals(),
            context_instance=RequestContext(request))

def classfiDetail(request, classfi):
    
    is_classfi = True
    temp = Classification.objects.get(name=classfi) #获取全部的Article对象
    articles = temp.article_set.all()
    paginator = Paginator(articles,6)
    page_num = request.GET.get('page')
    try:
         articles = paginator.page(page_num)
    except PageNotAnInteger:
         articles = paginator.page(1)
    except EmptyPage:
         articles = paginator.page(paginator.num_pages)

    #ar_newpost = Article.objects.order_by('-publish_time')[:10]
    classification = Classification.class_list.get_Class_list()    
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)#标签,以及对应的文章数目
    date_list = Article.date_list.get_Article_onDate()
        
    return render_to_response('mysite/home.html',
            locals(),
            context_instance=RequestContext(request))

def tagDetail(request, tag):
    
    is_tag = True
    temp = Tag.objects.get(name=tag) #获取全部的Article对象
    #articles = Article.objects.filter(tags=tag)
    articles = temp.article_set.all()
    paginator = Paginator(articles,6)
    page_num = request.GET.get('page')
    try:
         articles = paginator.page(page_num)
    except PageNotAnInteger:
         articles = paginator.page(1)
    except EmptyPage:
         articles = paginator.page(paginator.num_pages)

    #ar_newpost = Article.objects.order_by('-publish_time')[:10]


    classification = Classification.class_list.get_Class_list()    
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)#标签,以及对应的文章数目
    date_list = Article.date_list.get_Article_onDate()
     
    return render_to_response('mysite/home.html',
            locals(),
            context_instance=RequestContext(request))

class DetailView(generic.DetailView):
 
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
  
    template_name = 'polls/results.html'
