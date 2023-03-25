from django.shortcuts import render
from django.views import View

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from animals.forms import CattleForm,MachineryForm,GoatForm, SheepForm
from .models import Cattle,Machinery,Goat, Sheep
from datetime import datetime
from django.db.models import Q


# Create your views here.
class HomePageView(View):
    def get(self,request,*args,**kwargs):
        
        return render (request,'agric/home.html')


class MainPageView(LoginRequiredMixin, TemplateView):
    template_name='agric/main.html'
    login_url = 'account_login'


class AnimalPageView(LoginRequiredMixin,TemplateView):
    template_name='agric/main.html'
    login_url = 'login'

    #FOR CATTLE
class CattleListView(LoginRequiredMixin,ListView):
    model=Cattle
    success_url=reverse_lazy('cattle_list')
    template_name='agric/cattle/cattle_list.html'
    login_url = 'account_login'
class SearchPageView(LoginRequiredMixin,ListView):
    model=Cattle
    template_name='agric/cattle/search.html'
    def get_queryset(self):
        querry=self.request.GET.get('cattlesearch')
        object_list=Cattle.objects.filter(
            Q(weight__icontains=querry) | Q(breed__icontains=querry) | Q(location__icontains=querry) | Q(cattle_age__icontains=querry) | Q(selling_price_range__icontains=querry) 
            )
        return object_list
    login_url = 'login'
class CattleUpdateView(LoginRequiredMixin,UpdateView):
    model=Cattle
    # fields='__all__'
    form_class=CattleForm
    success_url=reverse_lazy('cattle_list')
    template_name='agric/cattle/cattle_edit.html'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class CattleDeleteView(LoginRequiredMixin,DeleteView):
    model=Cattle
    success_url=reverse_lazy('cattle_list')
    template_name='agric/cattle/cattle_delete.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class CattleSellView(LoginRequiredMixin,DeleteView):
    model=Cattle
    success_url=reverse_lazy('cattle_list')
    template_name='agric/cattle/cattle_sell.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class CattleUploadView(LoginRequiredMixin,CreateView):
    day = datetime.now().time()
    {'day':day}
    model=Cattle
    # form=CattleForm
    form_class=CattleForm
    # fields=('owner_contact','breed','weight','selling_price_range','location','cattle_age','cattle_sex_based_on','health_record_book','cattle_picture')
    success_url=reverse_lazy('cattle_list')
    template_name='agric/cattle/cattle_upload.html'
    def form_valid(self, form): 
        form.instance.owner_name = self.request.user
        return super().form_valid(form)


    #for goat
class GoatPageView(LoginRequiredMixin, ListView):
    model=Goat
    template_name='agric/goat/goat.html'
    login_url = 'account_login'
class GoatSearchPageView(ListView):
    model=Goat
    template_name='agric/goat/goat_search.html'
    def get_queryset(self):
        goatsearch=self.request.GET.get('goatsearch')
        object_list=Goat.objects.filter(
            Q(location__icontains=goatsearch) | Q(breed__icontains=goatsearch) | Q(weight__icontains=goatsearch) | Q(goat_age__icontains=goatsearch) | Q(maximum_selling_price__icontains=goatsearch)
            )
        return object_list
class GoatDeleteView(DeleteView):
    model=Goat
    success_url=reverse_lazy('goat_list')
    template_name='agric/goat/goat_delete.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class GoatSellView(LoginRequiredMixin,DeleteView):
    model=Goat
    success_url=reverse_lazy('goat_list')
    template_name='agric/goat/goat_sell.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class GoatUpdateView(UpdateView):
    model=Goat
    form_class=GoatForm
    success_url=reverse_lazy('goat_list')
    template_name='agric/goat/goat_edit.html'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class GoatUploadView(CreateView):
    day = datetime.now().time()
    {'day':day}
    model=Goat
    form=GoatForm
    form_class=GoatForm
    # fields=('owner_contact','breed','weight','selling_price_range','location','cattle_age','cattle_sex_based_on','health_record_book','cattle_picture')
    success_url=reverse_lazy('goat_list')
    template_name='agric/goat/goat_upload.html'
    def form_valid(self, form): 
        form.instance.owner_name = self.request.user
        return super().form_valid(form)


# for sheep
class SheepPageView(LoginRequiredMixin, ListView):
    model=Sheep
    template_name='agric/sheep/sheep.html'
    login_url = 'account_login'
class SheepUploadView(LoginRequiredMixin,CreateView):
    day = datetime.now().time()
    {'day':day}
    model=Sheep
    form_class=SheepForm
    success_url=reverse_lazy('sheep_list')
    template_name='agric/sheep/sheep_upload.html'
    def form_valid(self, form): 
        form.instance.owner_name = self.request.user
        return super().form_valid(form)

class SheepSellView(LoginRequiredMixin,DeleteView):
    model=Sheep
    success_url=reverse_lazy('sheep_list')
    template_name='agric/sheep/sheep_sell.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class SheepSearchPageView(ListView):
    model=Sheep
    template_name='agric/sheep/sheep_search.html'
    def get_queryset(self):
        sheepsearch=self.request.GET.get('sheepsearch')
        object_list=Sheep.objects.filter(
            Q(location__icontains=sheepsearch) | Q(breed__icontains=sheepsearch) | Q(weight__icontains=sheepsearch) | Q(sheep_age__icontains=sheepsearch) | Q(maximum_selling_price__icontains=sheepsearch)
            )
        return object_list
class SheepUpdateView(UpdateView):
    model=Sheep
    form_class=SheepForm
    success_url=reverse_lazy('sheep_list')
    template_name='agric/sheep/sheep_edit.html'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class SheepDeleteView(DeleteView):
    model=Sheep
    success_url=reverse_lazy('sheep_list')
    template_name='agric/sheep/sheep_delete.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
     #FOR ANIMALS MACHINES AND TOOLS
class MachineryPageView(LoginRequiredMixin,ListView):
    model=Machinery
    template_name='agric/machinery/machinery.html'
    login_url = 'account_login'
class ToolSearchPageView(LoginRequiredMixin,ListView):
    model=Machinery
    template_name='agric/machinery/machinery_search.html'
    def get_queryset(self):
        feedback=self.request.GET.get('machinerysearch')
        object_list=Machinery.objects.filter(
            Q(location__icontains=feedback) | Q(tool_name__icontains=feedback) | Q(brief_its_usage__icontains=feedback) | Q(animals_type__icontains=feedback)
            )
        return object_list
    login_url = 'account_login'

class MachinerySellView(LoginRequiredMixin,DeleteView):
    model=Machinery
    success_url=reverse_lazy('machinery')
    template_name='agric/machinery/machinery_sell.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class MachineryUploadView(LoginRequiredMixin,CreateView):
    day = datetime.now().time()
    {'day':day}
    model=Machinery
    form_class=MachineryForm
    success_url=reverse_lazy('machinery')
    template_name='agric/machinery/machinery_upload.html'
    def form_valid(self, form): 
        form.instance.owner_name = self.request.user
        return super().form_valid(form)
class MachineryDeleteView(DeleteView):
    model=Machinery
    template_name='agric/machinery/machinery_delete.html'
    success_url=reverse_lazy('machinery')
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class MachineryUpdateView(UpdateView):
    model=Machinery
    form_class=MachineryForm
    template_name='agric/machinery/machinery_edit.html'
    success_url=reverse_lazy('machinery')
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

#FOR ANIMALS FEEDS
class AnimalfeedPageView(TemplateView):
    template_name='agric/animalfeeds/animalfeed.html'

class AnimalmedicinePageView(ListView):
    template_name='animalmedicine/animalmedicine.html'

class AccountPageView(TemplateView):
    template_name='account/profile.html'
