from django.shortcuts import render, HttpResponse
from .models import survey
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


        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            print('valid')
            a = form.save()
            b = form1.save(commit= False)
            c = form2.save(commit= False)
            d = form3.save(commit= False)
            e = form4.save(commit= False)
            f = form5.save(commit= False)


            b.name=a.name
            c.name=a.name
            d.name = a.name
            e.name=a.name
            f.name = a.name

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
    data1=list(Page1.objects.values())
    data2 = list(Page2.objects.values())
    data3 = list(Page3.objects.values())
    data4=list(Page4.objects.values())
    data5=list(Page5.objects.values())

    return JsonResponse(data1, data2, data3, data4, data5, safe=False)



