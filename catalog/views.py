from django.shortcuts import render
from django.views import generic
from .models import Film, Director, FilmInstance, Genre

def index(request):
    num_films=Film.objects.all().count()
    num_instances=FilmInstance.objects.all().count()
    num_instances_available=FilmInstance.objects.filter(status__exact='a').count()
    num_directors=Director.objects.count()
    film_images=Film.get_img_path
    return render(
        request,
        'index.html',
        context={'num_films':num_films,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_directors':num_directors, 'film_images':film_images},
    )

class FilmListView(generic.ListView):
    model = Film
    paginate_by = 4
    def get_context_data(self, **kwargs):
        context = super(FilmListView, self).get_context_data(**kwargs)
        context['some_data'] = 'Some data'
        return context

class FilmDetailView(generic.DetailView):
    model = Film

    def film_detail_view(request,pk):
        try:
            film_id=Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404("Film does not exist")

        #film_id=get_object_or_404(Film, pk=pk)
        
        return render(
            request,
            'catalog/film_detail.html',
            context={'film':film_id,}
        )

class DirectorListView(generic.ListView):
    model = Director
    paginate_by = 4

class DirectorDetailView(generic.DetailView):
    model = Director

    def get_context_data(self, **kwargs):
        context = super(DirectorDetailView, self).get_context_data(**kwargs)
        context['films_data'] = Film.objects.all()
        return context

    def director_detail_view(request,pk):
        try:
            director_id=Director.objects.get(pk=pk)
        except Director.DoesNotExist:
            raise Http404("Director does not exist")

        #director_id=get_object_or_404(Director, pk=pk)
        
        return render(
            request,
            'catalog/director_detail.html',
            context
        )

class FilmAvailableListView(generic.ListView):
    model = FilmInstance
    template_name = 'catalog/available_now.html'
    paginate_by = 4
    
    def get_queryset(self):
        return super(FilmAvailableListView, self).get_queryset().filter(status__exact='a')