from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from books.models import Book,Author,Publisher
import logging

logger = logging.getLogger(__name__)

# TemplateView
class BooksModelView(TemplateView):
    logger.info("ENTER TO Book index")
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_list"] = ['Book', 'Author', 'Publisher']
        return context
    
# ListView
class BookList(ListView):
    model = Book

class AuthorList(ListView):
    logger.info("AUTHOR LIST")
    model = Author

class PublisherList(ListView):
    model = Publisher

# DetailView
class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher