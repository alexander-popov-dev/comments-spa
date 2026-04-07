import logging
import os

from celery import shared_task
from django.core.files.base import ContentFile

from .models import Comment
from .services import CommentService

logger = logging.getLogger(__name__)


@shared_task
def comment_image_resize_task(comment_id: int):
    """Resize the image attached to a comment. Silently skips if the comment no longer exists."""
    logger.info("Image resize task started for comment %s", comment_id)

    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        logger.warning("Comment %s not found, skipping image resize", comment_id)
        return

    if not comment.image_file:
        return

    resized = CommentService.resize_image(comment.image_file)
    if not isinstance(resized, ContentFile):
        logger.debug("Image for comment %s is within bounds, skipping replace", comment_id)
        return

    original_path = comment.image_file.path
    tmp_path = original_path + ".tmp"
    with open(tmp_path, "wb") as f:
        f.write(resized.read())
    os.replace(tmp_path, original_path)
    logger.info("Image resize task completed for comment %s", comment_id)
