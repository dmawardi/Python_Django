from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge_by_number(request, month):

    # grab keys from challenges and convert to list
    months = list(monthly_challenges.keys())

    # Detect error if month number is greater than number of months
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    # grab month by index
    forward_month = months[month-1]
    # redirect to new url using string verison of month in URL
    return HttpResponseRedirect('/challenges/'+forward_month)
