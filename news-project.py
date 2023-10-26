import requests
key = "799edfba41c841b3933c06a467c2e80e"
def news():
    source = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={key}"
    news = requests.get(source).json()
    # print(news)
    headline = news["articles"]
    # print(headline)

    loop = []
    for info in headline:
        loop.append(info["title"])
        # print(loop)

    for i in range(1):
        print(loop[i])
news()