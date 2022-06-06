from django.http import HttpResponse


def get_emojis(request):
    return HttpResponse("get emojis")

def decide_emoji(request):
    return HttpResponse("decide emoji")

