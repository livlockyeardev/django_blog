from django.shortcuts import render, get_object_or_404
from .models import About
# Create your views here.
def about(request):
    """
    Display an individual :model:`about.About`.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about.html`
    """

    about = About.objects.order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )