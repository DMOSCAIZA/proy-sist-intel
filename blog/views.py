from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from app.blog import tests


# Create your views here.


def index(request):

    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        img_url = fs.url(filename)

        tests.escalagrises(img_url)

        return render(request, 'index.html', {
            'uploaded_file_url': img_url
        })
    return render(request, "index.html")