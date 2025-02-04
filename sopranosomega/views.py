from django.shortcuts import render
from django.views.generic import TemplateView

class DefaultHomePage(TemplateView):
    display_name = "home"
    
    def get(self, request):
        context = {
                "title": "Home Page",
                "content": "Welcome to the home page",
                "description": "Buy high-quality products ranging from books to apparel"
            }
        return render(request, "home_page.html", context)