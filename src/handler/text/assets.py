from assets import PictureCategory
from loader import texts

TRIGGERS = {
    PictureCategory.AVATAR: texts.get_words(10),
    PictureCategory.PAIRED_AVATARS: texts.get_words(11),
    PictureCategory.CUTE: texts.get_words(12),
    PictureCategory.ANGRY: texts.get_words(13),
}
