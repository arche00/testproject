"""This module contains the CountElementsFoundByIOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CountElementsFoundByIOS(ActionProxy):
    def __init__(self, byType: str, byString: str, visibleOnly: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.ios.CountElementsFoundByIOS"
        )
        self.byType = byType
        self.byString = byString
        self.visibleOnly = visibleOnly
        self.amount = None
