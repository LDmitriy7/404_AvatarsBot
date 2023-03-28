from botty import TextHandler

from .assets import TRIGGERS


class Handler(TextHandler):
    def get_reply_text(self) -> str | None:
        for word in self.text_words:
            for category, triggers in TRIGGERS.items():
                if word in triggers:
                    return category
        return None


handler = Handler()
