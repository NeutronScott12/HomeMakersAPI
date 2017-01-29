from django.shortcuts import render, get_object_or_404, redirect
from django.views import View


# Create your views here.

class ShopIndex(View):

    template_class = "HMFrontEnd/public/index.html"

    def get(self, request):
        return render(request, self.template_class)
