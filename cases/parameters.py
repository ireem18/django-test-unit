
userID         = "ec624828-3e31-4cf5-a34b-860306cb335d"
isbnFirstCase  = "9781449331818"
isbnSecondCase = "9781449337711"

loginURL      = "https://demoqa.com/Account/v1/Login"
tokenURL      = "https://demoqa.com/Account/v1/GenerateToken"
userURL       = "https://demoqa.com/Account/v1/User/{UUID}".format(UUID=userID)
addedBooksURL = "https://demoqa.com/BookStore/v1/Books"
deleteBookURL = "https://demoqa.com/BookStore/v1/Book"

swaggerLoginURL        = "https://demoqa.com/swagger/Account/v1/Login"
swaggerTokenURL        = "https://demoqa.com/Account/v1/GenerateToken"
swaggerUserURL         = "https://demoqa.com/Account/v1/User/{UUID}".format(UUID=userID)
swaggerAddedBooksURL   = "https://demoqa.com/BookStore/v1/Books"

loginPrm = {
    "userName": "irem.demiroz",
    "password": "Ireem:1613%"
}

firstCaseBookPrm = {
  "userId": userID,
  "collectionOfIsbns": [
    {
      "isbn": isbnFirstCase
    }
  ]
}

secondCaseBookPrm = {
  "userId": userID,
  "collectionOfIsbns": [
    {
      "isbn": isbnSecondCase
    }
  ]
}

deletePrm = {
  "isbn": isbnSecondCase,
  "userId": userID
}