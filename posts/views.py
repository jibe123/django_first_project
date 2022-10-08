from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
import random
# Create your views here.


def post_search_view(request):
    query_dict = request.GET
    query_data = query_dict.get("query")
    try:
        if query_data:
            if int(query_data):
                object_from_db = Post.objects.get(id=query_data)
        else:
            object_from_db = None
    except Post.DoesNotExist:
        raise Http404
    except:
        object_from_db = "Вам нужно передавать только числа!"
    context = {
        "object": object_from_db
    }
    return render(request, "posts/post_search.html", context=context)


def post_list_view(request):
    print(request)
    # my_object = Post.objects.all().last()
    my_object = random.choice(Post.objects.all())
    # all_items_from_db = list(Post.objects.filter(title__contains='Hello'))
    # my_list = [1, 2, 50, 40, 44, 22]
    # list_ids = [1, 4, 2, 8]
    # all_items_from_db = list(Post.objects.filter(id__in=list_ids))
    #my_random_object = Post.objects.get(id=random.randint(1, len(my_object))
    # html_string = f"""
    # My first object's title is {my_object}
    # """
    all_posts = Post.objects.all()
    context = {"my_first_object": my_object,
               "posts": all_posts}
    return render(request, 'posts/test.html', context=context)


def post_detail_view(request, id=None):
    post_object = None
    print(id)
    if id is not None:
        try:
            post_object = Post.objects.get(id=id)
        except:
            raise Http404
    context = {
        "post_object": post_object
    }
    return render(request, "posts/post_detail.html", context=context)


@login_required
def post_create_view(request):
    form = PostForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        title = form.cleaned_data.get("title")
        description = form.cleaned_data.get("description")
        post_object = Post.objects.create(title=title, description=description)
        context["post_object"] = post_object
        context["created"] = True
    return render(request, "posts/post_create.html", context=context)


# def post_create_view(request):
#     message = False
#     context = {}
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         if title and description:
#             Post.objects.create(title=title, description=description)
#             return HttpResponseRedirect("/posts/create/")
#         else:
#             message = "You sent an empty form!"
#
#     context = {'message': message}
#     return render(request, "posts/post_create.html", context=context)




