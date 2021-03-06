import datetime
from haystack import indexes
from .models import Note, Author

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,
    template_name='search/note_text.txt')
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note
    
    def index_queryset(self, using=Note):
        """ Used when the entire index for model is updated. """
        return self.get_model().objects.all()

class AuthorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,
    template_name='search/author_text.txt')
    salutation = indexes.CharField(model_attr='salutation')
    author = indexes.CharField(model_attr='name')
    # email = indexes.EmailField(model_attr='email')    

    def get_model(self):
        return Author
    
    def index_queryset(self, using=Author):
        """ Used when the entire index for model is updated. """
        return self.get_model().objects.all()
