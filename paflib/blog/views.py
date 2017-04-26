from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post
from .forms import PostForm


class PostList(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'post_list': Post.objects.all()}
        )


class PostDetail(View):
    template_name = 'blog/post_detail.html'

    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug
        )
        return render(
            request,
            self.template_name,
            {'post': post}
        )


class PostCreate(View):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()}
        )

    def post(self,request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form}
            )
