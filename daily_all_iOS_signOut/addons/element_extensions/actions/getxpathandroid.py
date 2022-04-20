"""This module contains the GetXPathAndroid proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetXPathAndroid(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.android.GetXPathAndroid"
        )
        self.xpath = None
