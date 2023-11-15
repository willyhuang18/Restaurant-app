from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE
# Create your views here.
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
        
        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'