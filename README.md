# poppy-web-app
Web services to control Poppy

#installation

get the softwares

    pip install Django
    pip install uwsgi

get the sources

    cd dev
    git clone https://github.com/HumaRobotics/poppy-web-app.git

initialize

    cd poppy-web-app
    python manage.py collectstatic

run server

    uwsgi - - ini uwsgi.ini

then open url http://poppy.local:3031 in your browser.

# current state

Very basic web app, only showing right_ankle position when clicking on 'compliant' button.

Many problem to create a PoppyHumanoid object

# creating a Django app


poppy-web-app uses Django to create a Python-based webapp. Django distinguishes between projects and apps. Here, the project is poppy_web_app, you don't need to create it. This project contains by default only one app, called poppy_main_controls.

This is a really really quick and incomplete intro to the Django framework. To do anything more complicated, first follow the Django tutorial : https://docs.djangoproject.com/en/1.8/intro/tutorial01/

To create your own app, go to the poppy-web-app directory (the one with the manage.py file) and enter:


    python manage.py startapp yourappname

It creates a directory named yourappname with some default files in it.

in poppy_main_controls/settings.py, add your app to the installed_apps list:


    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        'poppy_main_controls',
        'yourappname'
    )

This will tell the webapp to integrate your app.

    urlpatterns = [
    url(r'^your_web_app_url/', include('yourappname.urls', namespace='yourappname')),
    url(r'^/', include('poppy_main_controls.urls', namespace='poppy_main_controls')),
    ]

This will tell the webapp when to call your app. WARNING (TO CHECK): be aware that the urls are regular expressions and that they are tested in the order set in urlpatterns. As r'^/' will match any url, put your app before the poppy_main_controls one.

Now is time to start your app. Inside your app directory, create a 'static' folder containing a 'yourappname' folder. In this folder, you will put your static files (CSS files, images...)

 Inside your app directory, create a 'template' folder containing a 'yourappname' folder. In this folder, you will put your templates, i.e. html files that will be used and modified by Python code to display what you want.

Let create a simple one (index.html):

    <h1>Poppy app test</h1>
    
    <p>I think your name is {{my_name}}.</p>
    
    <form action="{% url 'poppy_main_controls:index' %}" method="post">
    {% csrf_token %}
    <input type="submit" value="click here" name="button_clicked"/>
    </form>

In your app directory, create a urls.py file containing this:

    from django.conf.urls import url
    
    from . import views
    
    urlpatterns = [
        url(r'^$', views.index, name='index'),
        ]

As the urls.py file from the project, it helps linking urls to actual Python code, here the index function in the views file. So the final url is of the form <domain_name><project_url><app_url> with, in our case, <domain_name> being http://poppy.local/ , <project_url> being your_web_app_url/ and <app_url> being empty, so the full url is
http://poppy.local/your_web_app_url/

Let create the index function in the view.py file:

    from django.shortcuts import render
    
    # Create your views here.
    
    def index(request):
        context = {}
        if 'button_clicked' in request.POST.keys():
            context['my_name'] = "something else"
        else:
            context['my_name'] = "Poppy"
        return render(request, 'poppy_main_controls/index.html',context )

Let's look first at the last line: return render(request, 'poppy_main_controls/index.html',context )
It creates an HttpResponse by filling the index.html file with the data in context. The first time the webpage is displayed, the request is empty, so {{my_name}} is replaced by Poppy and the webpage displays: I think your name is Poppy.

But if you click the button, it calls this same index function with a POST request (remember : <form action="{% url 'poppy_main_controls:index' %}" method="post"> ) 
So we put "something else" in the context instead of Poppy and the webpage now displays
I think your name is something else.

Now you know how to link a webpage to a Python file, linking it to any Poppy library is easy!

If you want to add static files to your template (remember the static files should be in yourappname/static/yourappname directory), add {% load staticfiles %} at the beginning  and then use {% static 'yourappname/filename' %}

example:

    {% load staticfiles %}
    
    <link rel="stylesheet" type="text/css" href="{% static 'yourappname/my-style.css' %}" />

You have to redo 

    python manage.py collectstatic

each time you add a static file, so uWSGI can find it