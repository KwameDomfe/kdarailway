from django.shortcuts import render

# Create your views here.

def style_guide(request):

    context={}

    return render(request, 'library/library.html', context)


def tags(request):
    context={

    }
    return render(request, 'library/library_tags.html', context)

def atoms(request):
    context={

    }
    return render(request, 'library/library_atoms.html', context)


def molecules(request):
    context={

    }
    return render(request, 'library/library_molecules.html', context)

def organisms(request):
    context={

    }
    return render(request, 'library/library_organisms.html', context)

def templates(request):
    context={

    }
    return render(request, 'library/library_templates.html', context)

def pages(request):
    context={

    }
    return render(request, 'library/library_pages.html', context)

        