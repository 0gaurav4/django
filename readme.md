# django
 Learning django

 # pip3 install Django

1. Run <code> django-admin startproject PROJECT_NAME </code> to create a number of starter files for our project.
2. Run <code> cd PROJECT_NAME </code> to navigate into your new project’s directory.
3. Open the directory in your text editor of choice. You’ll notice that some files have been created for you. We won’t need to look at most of these for now, but there are three that will be very important from the start:
- manage.py is what we use to execute commands on our terminal. We won’t have to edit it, but we’ll use it often.
- settings.py contains some important configuration settings for our new project. There are some default settings, but we may wish to change some of them from time to time.
- urls.py contains directions for where users should be routed after navigating to a certain URL.
4. Start the project by running <code> python manage.py runserver </code> .This will open a development server, which you can access by visiting the URL provided. This development server is being run locally on your machine, meaning other people cannot access your website. This should bring you to a default landing page: