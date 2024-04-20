from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def basket_add_item(request, product_id):
    pass


@login_required
def basket_delete_item(request, product_id):
    pass


@login_required
def basket_change(request, product_id):
    pass