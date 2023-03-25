from assets import PictureCategory
from loader import texts


class Triggers:  # lowercase!
    AVATAR = [texts[10], texts[11], texts[12], texts[13]]
    PAIRED_AVATARS = [texts[14], texts[15], texts[16]]
    CUTE_PICTURE = [texts[17]]
    ANGRY_PICTURE = [texts[18], texts[19], texts[20]]


TRIGGERS_TO_CATEGORY = [
    (Triggers.AVATAR, PictureCategory.AVATAR),
    (Triggers.PAIRED_AVATARS, PictureCategory.PAIRED_AVATARS),
    (Triggers.CUTE_PICTURE, PictureCategory.CUTE),
    (Triggers.ANGRY_PICTURE, PictureCategory.ANGRY),
]
