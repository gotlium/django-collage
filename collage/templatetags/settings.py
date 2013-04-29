from django.conf import settings


ROW_WIDTH = getattr(settings, 'COLLAGE_ROW_WIDTH', 540)
IMAGE_HEIGHT = getattr(settings, 'COLLAGE_IMAGE_HEIGHT', 120)
MARGIN = getattr(settings, 'COLLAGE_MARGIN', 1)
MAX_IN_ROW = getattr(settings, 'COLLAGE_MAX_IN_ROW', 4)
