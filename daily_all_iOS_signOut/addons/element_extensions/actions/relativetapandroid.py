"""This module contains the RelativeTapAndroid proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class RelativeTapAndroid(ActionProxy):
    def __init__(self, horizontal: int, vertical: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.android.RelativeTapAndroid"
        )
        self.horizontal = horizontal
        self.vertical = vertical
