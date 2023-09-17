from django.shortcuts import redirect
from django.urls import reverse
from pages.forms import SubscriptionForm


class SubscribePost:
    redirect_page = None

    def subscription(self, request):
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            form.save()
            url = reverse(self.redirect_page)
            return redirect(url)

        else:
            print(form.errors)