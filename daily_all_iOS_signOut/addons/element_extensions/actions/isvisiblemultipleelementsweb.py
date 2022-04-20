"""This module contains the IsVisibleMultipleElementsWeb proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class IsVisibleMultipleElementsWeb(ActionProxy):
    def __init__(self, byType: str, elementsLocators: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.web.IsVisibleMultipleElementsWeb"
        )
        self.byType = byType
        self.elementsLocators = elementsLocators
        self.results = None
