from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    # dictionaries are ordered in Python 3
    "january": "Eat Meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Walk for at least 20 minutes every day!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Walk for at least 20 minutes every day!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Walk for at least 20 minutes every day!",
    "october": "Walk for at least 20 minutes every day!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Walk for at least 20 minutes every day!",
}


def index(request):
    # Init list items
    list_items = ""

    # Loop through months of monthly challenges
    for month in monthly_challenges.keys():
        # Generate URL for link
        month_path = reverse("str-monthly-challenge", args=[month])
        # Build list item
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

    # Set list items in unordered list
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# Functions in views can accept the request object for usage within
# def january(request):
#     # You can pass response data to client using Http Response
#     return HttpResponse("Eat Meat for the entire month!")


# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")


# Function to handle above requests dynamically
# url parameters can be added as argument to the function to access
def monthly_challenge(request, month):
    print("Monthly challenge request: " + month)
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")


def monthly_challenge_by_number(request, month):

    # grab keys from challenges and convert to list
    months = list(monthly_challenges.keys())

    # Detect error if month number is greater than number of months
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    # grab month by index
    redirect_month = months[month-1]
    # reverse allows you to create paths by using path names declared in urls
    # also accepts args
    redirect_path = reverse("str-monthly-challenge", args=[redirect_month])
    # redirect to new url using string verison of month in URL
    return HttpResponseRedirect(redirect_path)
