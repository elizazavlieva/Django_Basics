
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from urlsAndViews.departments.models import Department


def index(request):
    # url = reverse('redirect-view')
    url_lazy = reverse_lazy('redirect-view')
    return HttpResponse(f"<h1>{url_lazy}</h1>")


def view_with_name(request, variable):
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request,'departments/name_template.html', {'variable': variable})

def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")

def view_with_int_pk(request, pk):
    return JsonResponse({'pk': pk})


def view_with_slug(request, pk, slug):

    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404

    department = get_object_or_404(Department, pk=pk, slug=slug)

    # return HttpResponseNotFound()
    # return HttpResponse(status=404)

    # return HttpResponse(f"<h1>Department from slug: {department}</h1>")
    raise Http404

def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")

def redirect_to_softuni(request):
    return redirect('https://www.softuni.bg/')


def redirect_to_view(request):
    # return redirect('http://localhost:8000/numbers')
    # return redirect(index)
    return redirect('numbers', pk=2)