from django.shortcuts import render
from .models import *
from .forms import *
from datetime import datetime

def add_publication(request):

    form = PublicationForm()
    data = {'header_name': 'Блог / Добавление публикации' ,'rubrics': Rubric.objects.all(), 'tags': Tag.objects.all(), 'form': form}

    if request.method == 'POST':
        form_data = request.POST

        is_visible = False
        if form_data['IsVisible'] == 'on':
            is_visible = True

        date_pub = datetime.strptime(form_data['DateOfPublic'], "%d/%m/%Y")

        #защита от повторной публикации
        try:
            Publication.objects.get(Name=str(form_data['Name']), Text=str(form_data['Text']))
        except Publication.DoesNotExist:
            publication = Publication(Name=str(form_data['Name']), Text=str(form_data['Text']),
                                  IsVisible=is_visible, Image=request.FILES['Image'],
                                  DateOfPublic=date_pub, rubric=Rubric.objects.get(id=int(form_data['rubric'])))

            publication.save()

            keys = list(filter(lambda k: k[0] =='t' and k[1]=='a' and k[2]=='g', form_data.keys()))

            for key in keys:
                publication.tags.add(Tag.objects.get(id=int(form_data[key])))

    return render(request, 'add_publication.html', data)
