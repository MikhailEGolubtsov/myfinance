from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.conf import settings

from .models import Payment #, Group, Follow
from .forms import PaymentForm
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
    # template = 'payments/index.html'
    # return render(request, template) 


def payment_detail(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    # author_post_count = Post.objects.filter(author=post.author).count()
    # comments = post.comments.select_related('post')
    # form = CommentForm(request.POST or None)
    context = {
        'payment': payment,
    }
    return render(request, 'payments/payment_detail.html', context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    context = {
    }
    return render(request, 'payments/profile.html', context)

@login_required
def payment_create(request):
    template = 'payments/create_payment.html'
    if request.method == 'POST':
        form = PaymentForm(
            request.POST,
            files=request.FILES or None
        )
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()
            return redirect('payments:index')
        return render(request, template, {'form': form})
    form = PaymentForm()
    return render(request, template, {'form': form})

@login_required
def payment_edit(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)

    form = PaymentForm(
        request.POST or None,
        files=request.FILES or None,
        instance=payment
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('payments:payment_detail', payment_id)
    context = {
        'payment': payment,
        'form': form,
        'is_edit': True
    }
    return render(request, 'payments/create_payment.html', context)

