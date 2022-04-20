"""This module contains the GetXPathWeb proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetXPathWeb(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.web.GetXPathWeb"
        )
        self.xpath = None
