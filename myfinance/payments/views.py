from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.conf import settings

from .models import Payment #, Group, Follow
# from .forms import PostForm, CommentForm
from .utils import pagination


User = get_user_model()


@cache_page(settings.CASHE_TIME, key_prefix='index_page')
def index(request):
    payment_list = Payment.objects.all()
    page_obj = pagination(payment_list, request)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'payments/index.html', context)
