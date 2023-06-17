from django.urls import reverse, resolve
from django.test import TestCase
from cases.views import *
from cases.parameters import * 


class BookStoreTests2(TestCase):
    @classmethod
    def setUpTestData(cls):
        view = CaseOperationView()
        loginResult = view.login(loginURL, tokenURL)
        status_code = loginResult.get('status_code')
        cls.token = loginResult.get('token')

    def test_added_book(self):
        view = CaseOperationView()
        bookResult = view.addBook(addedBooksURL, self.token, secondCaseBookPrm)
        status_code = bookResult.get('status_code')
        self.assertEqual(status_code, 200)
    
    def test_book_delete(self):
        view = CaseOperationView()
        bookResult = view.deleteBook(self.token)
        status_code = bookResult.get('status_code')
        self.assertEqual(status_code, 200)

    def test_book_control(self):
        view = CaseOperationView()
        bookResult = view.bookControl(userURL, isbnSecondCase, self.token)
        self.assertEqual(bookResult, False)
