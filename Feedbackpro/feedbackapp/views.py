from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime
date1=datetime.datetime.now()

def feedback_view(requst):
    if requst.method=="POST":
        fform=FeedbackForm(requst.POST)
        if fform.is_valid():
            name=requst.POST.get('name','')
            rating=requst.POST.get('rating','')
            feedback=requst.POST.get('feedback','')

            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )

            data.save()
            fform=FeedbackForm()
            fdata=FeedbackData.objects.all()
            return render(requst,'feedback.html',{'fform':fform,'fdata':fdata})

        else:
            return HttpResponse("Invlid form")

    else:
        fdata=FeedbackData.objects.all()
        fform=FeedbackForm()
        return render(requst,'feedback.html',{'fform':fform,'fdata':fdata})

