from django.urls import (path, include)

from . views import(
    style_guide,
    tags,
    atoms,
    molecules,
    organisms, 
    templates,
    pages,
    )
app_name = 'library'

urlpatterns = [ path('', include(
    [
    # path('', style_guide, name='style-guide'),
    path('tags/', tags, name='tags'),
    path('atoms/', atoms, name='atoms'),
    path('molecules/', molecules, name='molecules'),
    path('organisms/', organisms, name='organisms'),
    path('templates/', templates, name='templates'),
    path('pages/', pages, name='pages'),
    ]
)),
]