from django.shortcuts import render
from django.views import generic
from django.db.models import Q
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
    # This function is used to get the queryset for your ListView based on the search query
    def get_queryset(self):
        # Get the search query from the GET parameters
        query = self.request.GET.get('q')
        # If a query is provided, filter the items based on the query
        if query:
            return Item.objects.filter(
                # Return items where the meal name or description contains the query
                Q(meal__icontains=query) |
                Q(description__icontains=query)
            ).order_by('date_created')
        else:
            # If no query is provided, return all items
            return Item.objects.order_by('date_created')
    
#  the page will be represented by the MenuList class DetailView
# this class is send the Item class to the template_name 
class MenuItemDetail(generic.DetailView):
    
    model = Item
    template_name = 'menu_item_detail.html'
    
    # Override the get_context_data method to add the review form to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

    # Override the post method to handle form submissions
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the review and associate it with the current item and user
            review = form.save(commit=False)
            review.item = self.get_object()
            review.user = request.user
            review.save()
        return super().get(request, *args, **kwargs)