from django.shortcuts import render, HttpResponse
from .models import survey,Page1, Page2, Page3, Page4, Page5
from .forms import SurveyForm, Page1Form, Page2Form, Page3Form, Page4Form, Page5Form
from django.http import JsonResponse
import json


def index(request):
    if request.method == "POST":
        print('post')
        form = SurveyForm(request.POST, request.FILES)
        form1 = Page1Form(request.POST)
        form2 = Page2Form(request.POST)
        form3 = Page3Form(request.POST)
        form4 = Page4Form(request.POST)
        form5 = Page5Form(request.POST)

        print (form.errors)
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            print (form.errors)
            print('valid')
            a = form.save()
            b = form1.save(commit= False)
            c = form2.save(commit= False)
            d = form3.save(commit= False)
            e = form4.save(commit= False)
            f = form5.save(commit= False)


            b.name= a
            b.document = a
            b.uploaded_at = a

            c.name = a
            c.document = a
            c.uploaded_at = a

            d.name = a
            d.document = a
            d.uploaded_at = a

            e.name = a
            e.document = a
            e.uploaded_at = a

            f.name = a
            f.document = a
            f.uploaded_at = a


            b.save()
            c.save()
            d.save()
            e.save()
            f.save()

            context = {'form': form,'form1':form1,'form2':form2,'form3': form3,'form4':form4,'form5':form5}

        return HttpResponse("Thanks for participating in survey")


    else:
        form = SurveyForm
        form1 = Page1Form
        form2 = Page2Form
        form3 = Page3Form
        form4 = Page4Form
        form5 = Page5Form

        context = {'form': form,'form1':form1,'form2':form2,'form3': form3,'form4':form4,'form5':form5}
        return render(request, 'annotator/index.html',context )



def json(request):

    data1 = list(survey.objects.values())
    data2 = list(Page2.objects.values())
    data3 = list(Page3.objects.values())
    data4 = list(Page4.objects.values())
    data5 = list(Page5.objects.values())

    return JsonResponse(data1, safe=False)
