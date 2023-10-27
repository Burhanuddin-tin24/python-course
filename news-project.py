import requests
key = "799edfba41c841b3933c06a467c2e80e"
def news():
    n= int(input("~ENTER THE NO. OF NEWS YOU WANT TO READ:-->  "))
    uchoice = int(input("Choose a category:\n1. BUSINESS NEWS\n2. TECH NEWS\nEnter the number of your choice: "))

    # uchoice2= int(input())
    if uchoice == 1:
        source = f"https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey={key}"
        news = requests.get(source).json()
        # print(news)
        headline = news["articles"]
        # print(headline)
    if uchoice == 2:
        source = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={key}"
        news = requests.get(source).json()
        # print(news)
        headline = news["articles"]
    else:
        print("invalid input")
    loop = []
    for info in headline:
        loop.append(info["title" and "description"])
        # print(loop)

    for i in range(n):
        print(loop[i])
news()