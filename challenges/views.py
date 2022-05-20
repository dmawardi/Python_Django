from http.client import HTTPResponse
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}


def index(request):
    # Init list items
    # list_items = ""
    months = list(monthly_challenges.keys())

    # Below code is not conventional as presentation logic should be in templates

    # Loop through months of monthly challenges
    # for month in monthly_challenges.keys():
    # Generate URL for link
    # month_path = reverse("str-monthly-challenge", args=[month])
    # Build list item
    # list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

    # Set list items in unordered list
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {
        "months": months
    })

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
    # Render html template to string
    # template_string = render_to_string("challenges/challenge.html")
    # return HttpResponse(template_string)

    # render converts to string and returns response
    # requires request as first argument
    # third argument is key value pair of vars to use in templates
    # note: render is always a successful request
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        # Raise Http404 will automatically look for a Django template file with 404 and serve
        raise Http404()


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
