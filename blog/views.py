from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    plist = Post.objects.all()
    template = 'blog\post_list.html'
    context = {'list': plist}
    return render(request, template, context)