import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .tasks import convert_images_to_pdf_task
from celery.result import AsyncResult


def index(request):
    return render(request, 'pdf_converter/index.html')


def upload_images(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        if not files:
            return JsonResponse({'success': False, 'error': 'No files uploaded.'})

        images_dir = os.path.join(settings.MEDIA_ROOT, 'images')
        os.makedirs(images_dir, exist_ok=True)

        file_paths = []
        for file in files:
            file_path = os.path.join(images_dir, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            file_paths.append(file_path)

        result = convert_images_to_pdf_task.delay(file_paths)
        request.session['task_id'] = result.id
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


def pdf_generation_in_progress(request):
    return render(request, 'pdf_converter/pdf_generation_in_progress.html')


def get_generated_pdf(request):
    task_id = request.session.get('task_id')
    if not task_id:
        return redirect('index')

    task_result = AsyncResult(task_id)
    pdf_output_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', 'output.pdf')
    pdf_url = os.path.join(settings.MEDIA_URL, 'pdfs/output.pdf')

    if task_result.status == 'SUCCESS' and os.path.exists(pdf_output_path):
        return redirect(pdf_url)
    else:
        return render(request, 'pdf_converter/pdf_generation_in_progress.html')
