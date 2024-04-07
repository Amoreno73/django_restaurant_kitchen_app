from django.views import generic
from .models import Item, MEAL_TYPE

# What is the purpose of a view?
# to get data from the models from the database model (models.py)
# and display those data back and forth to the HTML frontend

# Two main types of views: class-based and function-based

#here the menulist and detail view will connect
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"
# through context, we can send python to html 
# specifically, data from views to templates html
    def get_context_data(self):
        context = {} # we no longer have hard-coded entries
        context["meals"] = MEAL_TYPE
        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
