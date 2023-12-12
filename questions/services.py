import os
from .models import QuestionMedia
from django.core.files.uploadedfile import InMemoryUploadedFile
from moviepy.editor import VideoFileClip


def handle_uploaded_files(question, files):
    allowed_extensions = ['.jpeg', '.jpg', '.png', '.mp4']

    for file in files:
        ext = os.path.splitext(file.name)[1].lower()
        if ext not in allowed_extensions:
            return {"error": f"{ext} 확장자는 허용되지 않습니다."}

        if isinstance(file, InMemoryUploadedFile) and file.content_type.startswith("video"):
            clip = VideoFileClip(file.temporary_file_path())
            if clip.duration > 30:
                return {"error": "영상 길이는 30초를 초과할 수 없습니다."}

    for file in files:
        QuestionMedia.objects.create(question=question, file=file)

    return {"message": "파일 업로드 성공"}
