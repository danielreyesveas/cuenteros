from django import template
from blog.models import Category, Post
from django.db.models import Q, Count
from django.db.models.functions import ExtractMonth, ExtractYear, TruncDate
from django.utils.dateformat import format
from taggit.models import Tag


register = template.Library()

@register.simple_tag
def get_latest_posts():
    qs = Post.active.order_by('-created_at')[:3]
    if qs.exists():
        return qs
    return []

@register.simple_tag
def get_popular_posts():
    qs = (Post.active.annotate(
            likes=(Count('votes', filter=Q(votes__like=True)) - Count('votes', filter=Q(votes__like=False)))
        ).order_by('-likes', '-created_at'))[:3]
    if qs.exists():
        return qs
    return []

@register.simple_tag
def get_categories_total():
    qs = Category.objects.all().annotate(
                                posts_count=(Count('posts', filter=Q(posts__is_active=True)))
                            ).order_by('name')
    if qs.exists():
        return qs
    return []

@register.simple_tag
def get_popular_tags():
    qs = Tag.objects.all().order_by('name')[:6]
    if qs.exists():
        return qs
    return []

@register.simple_tag
def get_archives():
    qs = (Post.active.annotate(month=ExtractMonth('created_at'), year=ExtractYear('created_at'),)
            .order_by('-year', '-month')
            .values('month', 'year')
            .annotate(total=Count('*'))
            .values('month', 'year', 'total'))[:6]
    if qs.exists():
        return qs
    return []

@register.simple_tag
def get_related_posts(post):
    if post:
        return post.related_posts()
    return []