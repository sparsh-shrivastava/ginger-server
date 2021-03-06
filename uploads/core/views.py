from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import base64
import os
from uploads.core.models import Document
from uploads.core.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })

@csrf_exempt
def simple_upload(request):
    if request.method == 'POST' and request.POST['myfile']:
        myfileencode = request.POST['myfile']

        	
	myfile = base64.b64decode(myfileencode)
	"""	
	with open("Output.txt", "w") as text_file:
	    text_file.write(myfile)
        """

	print(type(myfile))
	#myfile=myfile.decode("utf-8")	
	#myfile = unicode(myfile, "utf-8")	
	#myfilecon = io.StringIO(myfile)	
	
	f = open("tryfile.jpg","w")
	f.write(myfile)
	f.close()
	f = open("tryfile.jpg","r")

	fs = FileSystemStorage()
        filename = fs.save("helloworld.jpg", f)
	f.close()
	os.remove(f.name)
	"""	
	f = open('helloworldnew.jpg','w')
	f.write(myfile)
	f.close()        
	"""	
		
	uploaded_file_url = fs.url(filename)
	print(uploaded_file_url)
	
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
	
	
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
