from django.shortcuts import redirect
from django.urls import reverse
from pages.forms import SubscriptionForm


class SubscribePost:
    redirect_page = None

    def post(self, request):
        action = request.POST.get('action')
        if action == "subscribe":
            return self.subscription(request)

    def subscription(self, request):
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            form.save()
            url = reverse(self.redirect_page)
            return redirect(url)

        else:
            print(form.errors)