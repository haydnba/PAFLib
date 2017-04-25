from django.views.generic import View
from django.shortcuts import get_object_or_404, render

from .models import Post


class PostList(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'post_list': Post.objects.all(),
            # 'parent_template': parent_template
            }
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
            {'post': post,
            # 'parent_template': parent_template
            }
        )
