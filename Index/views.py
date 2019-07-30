from django.shortcuts import render
from PublicationAdd.models import Publication

def index(request):
    publications = list(Publication.objects.all())
    publications = \
        list(filter(lambda p: p.can_post(), \
          list(filter(lambda p: p.IsVisible, \
            list(sorted(publications, key=lambda p: p.DateOfPublic, reverse=True))))))

    length = len(publications)
    ran = None
    if length > 10:
        publications = publications[0:9]
        print(publications)
    elif length < 10:
        ran = range(0, 10-length)
    
    print(ran)
    first_publication = publications[0]

    length -= 1
    
    data = { 'header_name': 'Блог','range': ran, 'fst_publication': first_publication, 'publications': publications[1:length]}
    return render(request, 'index.html', data)