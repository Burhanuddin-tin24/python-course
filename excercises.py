# # INSTAGRAM PROFILE INFORMARION:
# import instaloader


# # Replace 'instagram_username' with the username you want to scrape
# username = input("enter the username: ")

# # Create an Instaloader instance
# L = instaloader.Instaloader()

# try:
#     # Load the profile of the specified Instagram user
#     profile = instaloader.Profile.from_username(L.context, username)


#     for post in profile.get_posts():
#         print("Post URL:", post.url)
#         print("Caption:", post.caption)
#         print("Likes:", post.likes)
#         print("Comments:", post.comments)
#         print("Date:", post.date)
#         print("----------")
#     # Extract profile information
#     print("Username:", profile.username)
#     print("Full Name:", profile.full_name)
#     print("Bio:", profile.biography)
#     print("Followers:", profile.followers)
#     print("Following:", profile.followees)
#     print("Posts:", profile.mediacount)

#     # You can also iterate through the user's posts if needed
   

# except instaloader.exceptions.ProfileNotExistsException:
#     print(f"The Instagram user '{username}' does not exist.")
# except instaloader.exceptions.ConnectionException as e:
#     print(f"Connection error: {e}")

##NEWS PARSER: 
# import requests
# key = "799edfba41c841b3933c06a467c2e80e"
# def news():
#     n= int(input("~ENTER THE NO. OF NEWS YOU WANT TO READ:-->  "))
#     uchoice = int(input("Choose a category:\n1. BUSINESS NEWS\n2. TECH NEWS\nEnter the number of your choice: "))

    
#     if uchoice == 1:
#         source = f"https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey={key}"
#         news = requests.get(source).json()
#         # print(news)
#         headline = news["articles"]
#         # print(headline)
#     if uchoice == 2:
#         source = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={key}"
#         news = requests.get(source).json()
#         # print(news)
#         headline = news["articles"]
#     else:
#         print("invalid input")


#     loop = []
#     for info in headline:
#         loop.append(info["title" and "description"])
#         # print(loop)

#     for i in range(n):
#         print(loop[i])
# news()


# #POP NOTIFIER:
# from win10toast import ToastNotifier
# toast= ToastNotifier
# import time
# for i in range():
#     time.sleep(5)
#     toast.show_toast("WATER BREAK", "Please drink the water, it has been 1 hour since you drink water.")

# #CALENDER:
# from calendar import *
# year = int(input("enter year: "))
# print(calendar(year))