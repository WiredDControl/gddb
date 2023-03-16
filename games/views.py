from unicodedata import numeric
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.utils import timezone
from .models import Game,GLP,Release,Image,Disk,Extra
from .forms import GLPForm,ImageForm

'''
def games_list(request):
    games = Game.objects.filter(published_date__lte=timezone.now()).order_by('title').prefetch_related('glps')
    return render(request, 'games/games_list.html', {'games': games})
'''

def releasesearch(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        releases = Release.objects.filter(rlstitle__icontains=url_parameter)
    else:
        releases = Release.objects.all()

    ctx["releases"] = releases
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:

        html = render_to_string(
            template_name="releases-results-partial.html", context={"releases": releases}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "releases/releases.html", context=ctx)

class games_list(ListView):
    model = Game
    paginate_by = 20
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class releases_list(ListView):
    model = Release
    paginate_by = 20
    ordering = ['-created_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
def eulisker_list(request):
    try:
        eulisker_list = Release.objects.filter(toEulisker=1).order_by('rlstitle')
    except:
        eulisker_list = None
    try:
        eulisker_archivelist = Release.objects.filter(toEuliskerArchivelink=not "").order_by('rlstitle')
    except:
        eulisker_archivelist = None
    return render(request, 'eulisker/eulisker_list.html', {'eulisker_list': eulisker_list, 'eulisker_archivelist': eulisker_archivelist})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    try:
        glpid = GLP.objects.get(title_id=pk)        
    except:
        glpid = None
    try:
        releases = Release.objects.filter(title_id=pk,published_date__lte=timezone.now()).order_by('year')
    except:
        releases = None
    return render(request, 'games/game_detail.html', {'game': game, 'glpid' : glpid, 'releases' : releases})

def glp_list(request):
    glps = GLP.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'glp/glp_list.html', {'glps': glps})

def glp_detail(request, pk):
    glp = get_object_or_404(GLP, pk=pk)
    return render(request, 'glp/glp_detail.html', {'glp': glp})

def release_detail(request, pk):
    release = get_object_or_404(Release, pk=pk)
    try:
        gameid = Game.objects.get(id=release.title_id)
    except:
        gameid = None    
    try:
        images = Image.objects.filter(rlstitle_id=pk)
    except:
        print("no images found")
        images = None    
    try:
        disks = Disk.objects.filter(rlstitle_id=pk)
    except:
        print("no disks found")
        disks = None
    try:
        extras = Extra.objects.filter(rlstitle_id=pk)
    except:
        print("no disks found")
        extras = None
    return render(request, 'releases/release_detail.html', {'release': release, 'images': images, 'disks': disks, 'extras': extras, 'gameid': gameid})

def glp_new(request):
    if request.method == "POST":
        form = GLPForm(request.POST)
        if form.is_valid():
            glp = form.save(commit=False)
            glp.published_date = timezone.now()
            glp.save()
            return redirect('glp_detail', pk=glp.pk)
    else:
        form = GLPForm()
    return render(request, 'glp/glp_edit.html', {'form': form})

def glp_edit(request, pk):
    glp = get_object_or_404(GLP, pk=pk)
    if request.method == "POST":
        form = GLPForm(request.POST, instance=glp)
        if form.is_valid():
            glp = form.save(commit=False)
            glp.published_date = timezone.now()
            glp.save()
            return redirect('glp_detail', pk=glp.pk)
    else:
        form = GLPForm(instance=glp)
    return render(request, 'glp/glp_edit.html', {'form': form})

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'images/image_upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'images/image_upload.html', {'form': form})