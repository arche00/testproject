"""This module contains the RelativeTapIOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class RelativeTapIOS(ActionProxy):
    def __init__(self, horizontal: int, vertical: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.ios.RelativeTapIOS"
        )
        self.horizontal = horizontal
        self.vertical = vertical
