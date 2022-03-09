from distutils.log import error
from django.urls import reverse
from django.shortcuts import render
from megasena.forms import FormFile, FormSearch
from megasena.utils.upload_tsv_file import Upload
from megasena.models import MegaSenaModel
from django.views import generic
from django.views.generic import ListView

def index(request):
    return render(request, 'index.html', locals())

def loadfile(request):        
    if request.method == 'POST':        
        form = FormFile(request.POST, request.FILES)
        if form.is_valid():            
            upload = Upload(form['tsv_file'].data, MegaSenaModel)
            if form.cleaned_data['checkbox']:
                upload.remove_all_data_uploaded()
            upload.handling_data_in_tsv_file()            
    else:
        form = FormFile()

    return render(request, 'loadfile.html', locals())

class results(ListView):
    model = MegaSenaModel
    template_name = 'results.html'
    context_object_name = 'result_list'       
    paginate_by = 20

    def get_queryset(self):
        sorted = self.request.GET.get('sorted')
        if sorted != None:
            return MegaSenaModel.objects.all().order_by(sorted)            
        else:
            return MegaSenaModel.objects.all()
            

class resultDetail(generic.DetailView):
    model = MegaSenaModel
    template_name = 'result_detail.html'   
    
def contest(request):
    form = FormSearch(request.POST or None)
    if form.is_valid():       
        if MegaSenaModel.objects.filter(contest=request.POST.get('search')).exists():
            megasenamodel = MegaSenaModel.objects.get(contest=request.POST.get('search'))
            return render(request, 'result_detail.html', locals())
        else:
            contest = request.POST.get('search')
            return render(request, 'no_result.html', locals())           
    return render(request, 'results.html', locals())
    
