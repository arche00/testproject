"""This module contains the GetTagNameIOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetTagNameIOS(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.ios.GetTagNameIOS"
        )
        self.tagName = None
