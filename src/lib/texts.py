from botty import texts

from lib import commands

PRIVATE_WELCOME = texts[3]
GROUP_WELCOME = texts[4].format(
    commands.GET_AVATARS,
    commands.GET_PAIRED,
    commands.GET_CUTE,
    commands.GET_ANGRY,
    commands.SEND_PICTURE,
)
DOES_NOT_WORK = texts[21]
ADMIN_PANEL = texts[14]
