"""This module contains the IsVisibleMultipleElementsAndroid proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class IsVisibleMultipleElementsAndroid(ActionProxy):
    def __init__(self, byType: str, elementsLocators: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="Ow3LGSkBqUyGjzyAibUJig",
            classname="io.testproject.addons.element.android.IsVisibleMultipleElementsAndroid"
        )
        self.byType = byType
        self.elementsLocators = elementsLocators
        self.results = None
