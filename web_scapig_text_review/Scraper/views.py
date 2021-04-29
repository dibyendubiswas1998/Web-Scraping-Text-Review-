from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InputForm
from .models import Review_Details
from .scraper import FScraper


# Create your views here.
def Home(request):
    try:
        if request.method == 'POST':
            fm = InputForm(request.POST)
            if fm.is_valid():
                inp = fm.cleaned_data['input']
                domain = fm.cleaned_data['category']
                if domain == 'Flipkart':
                    sc = FScraper(inp, domain)
                else:
                    sc = FScraper(inp, domain)
                data = sc.Get_Text_Data()
                try:
                    reg = Review_Details(json_data=data, domain_name=domain)
                    reg.save()
                    fm = InputForm()
                    return HttpResponseRedirect('/db/')
                except Exception as e:
                    print(e)
        else:
            fm = InputForm()
        context = {'form': fm, "title": "Web Scraping"}
        return render(request, 'index.html', context)
    except Exception as e:
        print(e)


def DB(request):
    try:
        obj = Review_Details.objects.all()
        # print(obj)
        return render(request, 'db.html', {'object': obj, 'title': 'DB'})
    except Exception as e:
        print(e)


def Review(request, id):
    try:
        obj = Review_Details.objects.get(pk=id)
        customer_name = []
        customer_review = []
        customer_comments = []
        customer_rating = []
        for key, value in obj.json_data.items():
            if key == 'Customer_Name':
                customer_name.append(value)
            elif key == 'Review':
                customer_review.append(value)
            elif key == 'Customer_Comments':
                customer_comments.append(value)
            else:
                customer_rating.append(value)
        # print(customer_comments)
        context = {
            'customer_name': customer_name,
            'customer_review': customer_review,
            'customer_comments': customer_comments,
            'customer_rating': customer_rating,
            'title': 'Customer Review',
        }
        return render(request, 'data.html', context)
    except Exception as e:
        print(e)


def Delete(request, id):
    try:
        pi = Review_Details.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/db/')

    except Exception as e:
        print(e)

