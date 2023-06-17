# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
import requests
from .parameters import * 

class CaseOperationView(ListView):

    def login(self, url, tokenUrl):
        result = {}
        # Kullanıcı sisteme login olur, token bilgisi alınır.
        try:
            loginResponse = requests.post(url, json = loginPrm)
            if loginResponse.status_code == 200:
                tokenResponse = requests.post(tokenURL, json = loginPrm)
                token = tokenResponse.json().get('token')
                result = {'status_code': 200, 'message': 'Login Olundu..', 'token': token}
        except:
            result = {'status_code': 400, 'message': 'Login Hata..'}
        
        return result

    def addBook(self, url, token, prm):
        # Sepete kitap eklenmesi yapılır.
        result = {}
        try:
            bookAddedResponse = requests.post(url, json = prm, headers={'Authorization': f'Bearer {token}'})
            if bookAddedResponse.status_code == 201:
                result = {'status_code': 200, 'message': 'Book Added'}
            else:
                bookAddedResponse = bookAddedResponse.json()
                result = {'status_code': 400, 'message': bookAddedResponse.get('message')}
        except:
            result = {'status_code': 400, 'message': 'Not Added. Error!'}

        return result

    def bookControl(self, url, isbn, token):
        # Kullanıcı listesinde ekli olan kitaplar kontrol edilir.
        addedSucces = False
        userData = requests.get(url, headers={'Authorization': f'Bearer {token}'})
        userDataResponse = userData.json()

        if userData.status_code == 201 and len(userDataResponse.get('books')) > 0:
            userBooks = userDataResponse.get('books')
            for book in userBooks:
                if book.get('isbn') == isbn:
                    addedSucces = True
                    break

        return addedSucces

    def deleteBook(self, token):
        # Sepetten kitap kaldırılır.
        try:
            userData = requests.delete(deleteBookURL, data=deletePrm, headers={'Authorization': f'Bearer {token}'})
            result = {'status_code': 200, 'message': 'Book Deleted'}
        except:
            result = {'status_code': 400, 'message': 'Not Deleted. Error!'}

        return result
