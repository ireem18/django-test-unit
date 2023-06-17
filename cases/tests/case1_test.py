from django.urls import reverse, resolve
from django.test import TestCase
from cases.views import *
from cases.parameters import * 


class BookStoreTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        view = CaseOperationView()
        loginResult = view.login(loginURL, tokenURL)
        status_code = loginResult.get('status_code')
        cls.token = loginResult.get('token')

    def test_added_book(self):
        view = CaseOperationView()
        bookResult = view.addBook(addedBooksURL, self.token, firstCaseBookPrm)
        status_code = bookResult.get('status_code')
        message = bookResult.get('message')
        if not self.assertEqual(message, "ISBN already present in the User's Collection!"):
            self.assertEqual(status_code, 200)

    def test_book_control(self):
        view = CaseOperationView()
        bookResult = view.bookControl(userURL, isbnFirstCase, self.token)
        self.assertEqual(bookResult, True)

