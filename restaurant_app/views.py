from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE,Review
from .form import ReviewForm
# created two class-based views.
#  the page will be represented by the MenuList class ListView
class MenuList(generic.ListView):
    queryset = Item.objects.order_by('date_created')
    template_name = "index.html"
    # special parameter
    def get_context_data(self,**kwargs):
        # call the parent class(listView), access get_context_data
        # an existing dictionary from the ListView class 
        # get some default values already. 
        # this will be a dictionary,
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        context['reviews'] = Review.objects.all()
        return context
    
#  the page will be represented by the MenuList class DetailView
# this class is send the Item class to the template_name 
class MenuItemDetail(generic.DetailView):
    
    model = Item
    template_name = 'menu_item_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.item = self.get_object()
            review.user = request.user
            review.save()
        return super().get(request, *args, **kwargs)