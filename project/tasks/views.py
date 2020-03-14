from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")


@csrf_exempt
def run_task(request):
    if request.POST:
        task_type = request.POST.get("type")
        return JsonResponse({"task_type": task_type}, status=202)


@csrf_exempt
def get_status(request, task_id):
    return JsonResponse({"task_id": task_id}, status=200)
