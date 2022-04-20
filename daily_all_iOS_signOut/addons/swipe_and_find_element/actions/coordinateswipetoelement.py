"""This module contains the CoordinateSwipeToElement proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CoordinateSwipeToElement(ActionProxy):
    def __init__(self, startXMargin: int, startYMargin: int, endXMargin: int, endYMargin: int, amountOfSwipes: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="3nqfr8Djt0KB-sz43jU-0g",
            classname="io.testproject.addons.mobile.elementfinder.CoordinateSwipes.CoordinateAndroid.CoordinateSwipeToElement"
        )
        self.startXMargin = startXMargin
        self.startYMargin = startYMargin
        self.endXMargin = endXMargin
        self.endYMargin = endYMargin
        self.amountOfSwipes = amountOfSwipes
