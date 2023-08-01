from turtle import title
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm, contactForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from enquiry.models import Enquiry
from django.core.mail import send_mail, EmailMultiAlternatives
from socialLink.models import SocialLink

def testPage(request):
    data = {
        'title': 'Home',
        'clist': ['PHP','Laravel','dJango'],
        'numbers': [10,20,30,40,50]
    }
    return render(request, "test.html", data);

def homePage(request):
    # send_mail(
    #     'Django Mail',
    #     'This is a test mail from Django admin',
    #     'arijit.wizkraft@gmail.com',
    #     ['arijitsamaddar21@gmail.com'],
    #     fail_silently=False,
    # )

    # subject = "Test Mail Django"
    # froms = 'arijit.wizkraft@gmail.com'
    # msg = 'This is a test email from <b>Django using EmailAlternatives</b>'
    # to = 'arijitsamaddar21@gmail.com'
    # msgs = EmailMultiAlternatives(subject,msg,froms,[to])
    # msgs.content_subtype='html'
    # msgs.send()


    # data = {
    #     'title': 'Home',
    #     'clist': ['PHP','Laravel','dJango'],
    #     'numbers': [10,20,30,40,50]
    # }
    # serviceData = Service.objects.all()

    #Order by Ascending
    # serviceData = Service.objects.all().order_by('service_title')

    #Order by Discending
    # serviceData = Service.objects.all().order_by('-service_title')

    #Order by Ascending and Limit using list Slicing method of Python
    serviceData = Service.objects.all().order_by('service_title')[:3]

    newsData = News.objects.all()

    footerData = SocialLink.objects.all()

    data = {
        'serviceData':serviceData,
        'newsData':newsData,
        'footerData':footerData
    }
    return render(request, "index.html", data);

def newsDetails(request,slug):
    details = News.objects.get(news_slug=slug)
    data={
        'details':details
    }
    return render(request,'newsdetails.html', data)

def aboutUs(request):
    # return HttpResponse("Hello World! This is About Us page.");
    return render(request, "about.html");

def contactUs(request):
    # return HttpResponse("Hello World! This is Contact Us page.");
    fn = contactForm()
    data = {
        'total': '',
        'form':fn
    }
    if request.method == "GET":
        output = request.GET.get('output')
        data = {
            'total': '',
            'form': fn
        }
    return render(request, "contact.html", data);

def saveEnquiry(request):
    fn = contactForm()
    data = {
        'total': '',
        'form':fn
    }

    if request.method == "POST":
        en_name = request.POST.get('name')
        en_email = request.POST.get('email')
        en_phone = request.POST.get('phone')
        en_message = request.POST.get('message')

        en = Enquiry(en_name=en_name,en_email=en_email,en_phone=en_phone,en_message=en_message)
        en.save()

        subject = "New Enquiry Submitted"
        froms = 'arijit.wizkraft@gmail.com'
        msg = 'This is a enquiry email from <b>Django website using EmailAlternatives</b>.<br><h3>Name:</h3> '+en_name+'<br><h3>Email:</h3> '+en_email+'<br><h3>Phone:</h3> '+en_phone+'<br><h3>Message:</h3> '+en_message+'<br>'
        to = 'arijitsamaddar21@gmail.com'
        msgs = EmailMultiAlternatives(subject,msg,en_email,[to])
        msgs.content_subtype='html'
        msgs.send()

    return render(request,"contact.html", data)

def services(request):
    # return HttpResponse("Hello World! This is Course page.");
    #Order by Ascending
    serviceData = Service.objects.all()

    paginator = Paginator(serviceData,2)
    page_number = request.GET.get('page')
    serviceDataFinal = paginator.get_page(page_number)
    totalpage = serviceDataFinal.paginator.num_pages


    #Order by Discending
    # serviceData = Service.objects.all().order_by('-service_title')

    if request.method == "GET":
        st = request.GET.get('searchterm')
        if st !=None:
            #Get all data from services where title matches exactly the search term
            # serviceData = Service.objects.filter(service_title=st)

            #Get all data from services where title matches any of the search term
            serviceData = Service.objects.filter(service_title__icontains=st)

    data = {
        # 'serviceData':serviceData
        'serviceData':serviceDataFinal,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, "services.html",data)

def blog(request):
    # return HttpResponse("Hello World! This is Course page.");
    return render(request, "blog.html")

def userForm(request):
    # return HttpResponse("Hello World! This is Course page.");
    total = 0;
    fn = usersForm()
    data = {'form':fn};
    try:
        # n1 = int(request.GET.get('name1'))
        # n2 = int(request.GET.get('name2'))
        # print(n1+n2)
        # total = n1+n2
        if request.method == "POST":
            n1 = int(request.POST.get('name1'))
            n2 = int(request.POST.get('name2'))
            print(n1+n2)
            total = n1+n2
            data = {
                # 'n1':n1,
                # 'n2':n2,
                'form':fn,
                'output':total
            }
            url = "/contact-us/?output={}".format(total)
            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass

    # return render(request, "userform.html",{'output':total})
    return render(request, "userform.html",data)

def submitForm(request):
    total = 0;
    data = {};
    try:
        # n1 = int(request.GET.get('name1'))
        # n2 = int(request.GET.get('name2'))
        # print(n1+n2)
        # total = n1+n2
        if request.method == "POST":
            n1 = int(request.POST.get('name1'))
            n2 = int(request.POST.get('name2'))
            print(n1+n2)
            total = n1+n2
            data = {
                'n1':n1,
                'n2':n2,
                'output':total
            }
            url = "/contact-us/?output={}".format(total)
            # return HttpResponseRedirect(url)
            # return redirect(url)
            return HttpResponse(total)
    except:
        pass
    # return HttpResponse(request);

def mycalculator(request):
    c = 0
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('operator')
            if opr == "+":
                c = n1+n2
            elif opr == "-":
                c = n1-n2
            elif opr == "x":
                c = n1*n2
            elif opr == "/":
                c = n1/n2

    except:
        c ="Invalid Operation"

    return render(request,"calculator.html",{'c':c})

def evenodd(request):
    c = ''
    # try:
    if request.method == "POST":
        if request.POST.get('num1') == "":
            return render(request,"evenodd.html",{'error':True})

        n1 = eval(request.POST.get('num1'))
        if n1%2 == 0:
            c = 'Even Number'
        else:
            c = 'Odd Number'

    # except:
    #     c ="Invalid Number Format"

    return render(request,"evenodd.html",{'c':c})

def marksheet(request):
    data = {}
    c = ''
    try:
        if request.method == "POST":
            s1 = eval(request.POST.get('num1'))
            s2 = eval(request.POST.get('num2'))
            s3 = eval(request.POST.get('num3'))
            s4 = eval(request.POST.get('num4'))
            s5 = eval(request.POST.get('num5'))

            c = s1+s2+s3+s4+s5
            p = c*100/500
            if p>=60:
                d = '1st Division'
            elif p>=48:
                d = '2nd Division'
            elif p>=35:
                d = '3rd Division'
            else:
                d = 'Fail'
            
            data={
                'c':c,
                'p':p,
                'd':d
            }

    except:
        c ="Invalid Number Format"

    return render(request,"marksheet.html",data)

def courses(request):
    return HttpResponse("Hello World! This is Course page.");

def courseInteger(request, courseid):
    return HttpResponse("Hello World! This is Course Details with integer value into URL page.===> ", courseid);

def courseString(request, courseid):
    return HttpResponse("Hello World! This is Course Details with String value into URL page.===> "+courseid);

def courseSlug(request, courseid):
    return HttpResponse("Hello World! This is Course Details with Slug value into URL page.===> "+courseid);

def courseAny(request, courseid):
    return HttpResponse("Hello World! This is Course Details with Any value into URL page.===> "+courseid);

# def courseInteger(request, courseid):
#     return HttpResponse("Hello World! This is Course Details with integer value into URL page.===> "+courseid);
