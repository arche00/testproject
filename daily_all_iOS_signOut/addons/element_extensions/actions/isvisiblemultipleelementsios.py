"""This module contains the IsVisibleMultipleElementsIOS proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class IsVisibleMultipleElementsIOS(ActionProxy):
    def __init__(self, byType: str, elementsLocators: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.ios.IsVisibleMultipleElementsIOS"
        )
        self.byType = byType
        self.elementsLocators = elementsLocators
        self.results = None
