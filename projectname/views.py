from projectname.models import Projectname
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from helpers.views.HybridViews import HybridDetailView, HybridListView
from django.contrib.auth.decorators import login_required, permission_required

class ProjectnameDetailView(HybridDetailView):
    model = Projectname
    
class ProjectnameListView(HybridListView):
    model = Projectname

class ProjectnameDeleteView(DeleteView):
    model = Projectname 
    success_url = reverse_lazy('projectname-list')

class ProjectnameCreateView(CreateView):
    model = Projectname
    fields = Projectname.Fields

class ProjectnameUpdateView(UpdateView):
    model = Projectname
    fields = Projectname.Fields
