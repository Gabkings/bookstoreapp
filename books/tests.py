from django.test import TestCase, Client
from .models import Book, Review
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.


class BookModelTests(TestCase):
    
    def test_book_model_str(self):
        book = Book.objects.create(
            price= 30.00,
            author = 'Gabriel',
            title = 'New revolutions'
        )
        self.assertEqual(str(book), book.title)
        
class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user( # new
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00'
        )
        self.review = Review.objects.create( # new
            book = self.book,
            author = self.user,
            review = 'An excellent review',
        )
        
    def test_book_listing(self):
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.author, 'JK Rowling')
        
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')
        
    def test_book_detail_view(self):
        responce = self.client.get(self.book.get_absolute_url())
        no_responce = self.client.get('books/1234')
        self.assertEqual(responce.status_code, 200)
        self.assertEqual(no_responce.status_code, 404)
        self.assertContains(responce, 'Harry Potter')
        self.assertTemplateUsed(responce, 'books/book_detail.html')
        self.assertContains(responce, 'An excellent review') # new
        self.assertTemplateUsed(responce, 'books/book_detail.html')