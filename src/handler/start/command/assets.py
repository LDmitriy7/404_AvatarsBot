import commands
from loader import texts


class Texts:
    private_welcome = texts[3]
    group_welcome = texts[4].format(
        commands.GET_AVATARS,
        commands.GET_PAIRED,
        commands.GET_CUTE,
        commands.GET_ANGRY,
        commands.SEND_PICTURE,
    )
