from django.urls import reverse, resolve
from django.test import TestCase
from cases.views import *
from cases.parameters import * 


class BookStoreTests3(TestCase):

    @classmethod
    def setUpTestData(cls):
        view = CaseOperationView()
        loginResult = view.login(swaggerLoginURL, swaggerTokenURL)
        status_code = loginResult.get('status_code')
        cls.token = loginResult.get('token')

    def test_added_book(self):
        view = CaseOperationView()
        bookResult = view.addBook(swaggerAddedBooksURL, self.token, secondCaseBookPrm)
        status_code = bookResult.get('status_code')
        self.assertEqual(status_code, 200)

    def test_book_control(self):
        view = CaseOperationView()
        bookResult = view.bookControl(swaggerUserURL, isbnSecondCase, self.token)
        self.assertEqual(bookResult, True)

