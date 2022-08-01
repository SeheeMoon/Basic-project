#from django.shortcuts import render FBV코드를 모두 주석처리하였음.
#from .models import Post

#def index(request):
    #posts = Post.objects.all().order_by('-pk')
    #return render(
        #request,
        #'blog/index.html',
        #{
            #'posts': posts,
        #}
    #)

#def single_post_page(request, pk):
    #post = Post.objects.get(pk=pk)

    #return render(
        #request,
        #'blog/single_post_page.html',
        #{
          #  'post': post,
        #}
    #)


from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

