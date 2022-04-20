"""This module contains the CountElementsFoundByWeb proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CountElementsFoundByWeb(ActionProxy):
    def __init__(self, byType: str, byString: str, visibleOnly: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.web.CountElementsFoundByWeb"
        )
        self.byType = byType
        self.byString = byString
        self.visibleOnly = visibleOnly
        self.amount = None
