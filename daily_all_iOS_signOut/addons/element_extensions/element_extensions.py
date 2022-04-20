from .actions import CountElementsFoundByAndroid, GetElementLocationAndroid, GetTagNameAndroid, GetXPathAndroid, IsVisibleMultipleElementsAndroid, RelativeTapAndroid, CountElementsFoundByIOS, GetElementLocationIOS, GetTagNameIOS, GetXPathIOS, IsVisibleMultipleElementsIOS, RelativeTapIOS, CountElementsFoundByWeb, DoubleClickNoJs, DoubleClickWeb, GetElementLocationWeb, GetTagNameWeb, GetXPathWeb, IsVisibleMultipleElementsWeb, SwitchToDefault, SwitchToFrame, SwitchToParentFrame


class ElementExtensions:
    @staticmethod
    def countelementsfoundbyandroid(byType: str, byString: str, visibleOnly: str) -> CountElementsFoundByAndroid:
        """Count element found by {{locator}}.

        Counts the amount of elements found by provided locator.
        """
        return CountElementsFoundByAndroid(byType, byString, visibleOnly)

    @staticmethod
    def getelementlocationandroid() -> GetElementLocationAndroid:
        """Get {{element}} location.

        Retrieves the location (x,y) of an element.
        """
        return GetElementLocationAndroid()

    @staticmethod
    def gettagnameandroid() -> GetTagNameAndroid:
        """Get {{element}} tag name.

        Retrieves a tag name of an element.
        """
        return GetTagNameAndroid()

    @staticmethod
    def getxpathandroid() -> GetXPathAndroid:
        """Get {{element}} XPath.

        Retrieves the xpath of an element.
        """
        return GetXPathAndroid()

    @staticmethod
    def isvisiblemultipleelementsandroid(byType: str, elementsLocators: str) -> IsVisibleMultipleElementsAndroid:
        """Check if given elements are visible, delimit elements locatorsby newline.

        check if provided elements are visible.
        """
        return IsVisibleMultipleElementsAndroid(byType, elementsLocators)

    @staticmethod
    def relativetapandroid(horizontal: int, vertical: int) -> RelativeTapAndroid:
        """Tap {{element}} at {{horizontal}}% width and {{vertical}}% height.

        Tap element at point relative to it's top-left corner.
        """
        return RelativeTapAndroid(horizontal, vertical)

    @staticmethod
    def countelementsfoundbyios(byType: str, byString: str, visibleOnly: str) -> CountElementsFoundByIOS:
        """Count element found by {{locator}}.

        Counts the amount of elements found by provided locator.
        """
        return CountElementsFoundByIOS(byType, byString, visibleOnly)

    @staticmethod
    def getelementlocationios() -> GetElementLocationIOS:
        """Get {{element}} location.

        Retrieves the location (x,y) of an element.
        """
        return GetElementLocationIOS()

    @staticmethod
    def gettagnameios() -> GetTagNameIOS:
        """Get {{element}} tag name.

        Retrieves a tag name of an element.
        """
        return GetTagNameIOS()

    @staticmethod
    def getxpathios() -> GetXPathIOS:
        """Get {{element}} XPath.

        Retrieves the xpath of an element.
        """
        return GetXPathIOS()

    @staticmethod
    def isvisiblemultipleelementsios(byType: str, elementsLocators: str) -> IsVisibleMultipleElementsIOS:
        """Check if given elements are visible, delimit elements locatorsby newline.

        check if provided elements are visible.
        """
        return IsVisibleMultipleElementsIOS(byType, elementsLocators)

    @staticmethod
    def relativetapios(horizontal: int, vertical: int) -> RelativeTapIOS:
        """Tap {{element}} at {{horizontal}}% width and {{vertical}}% height.

        Tap element at point relative to it's top-left corner.
        """
        return RelativeTapIOS(horizontal, vertical)

    @staticmethod
    def countelementsfoundbyweb(byType: str, byString: str, visibleOnly: str) -> CountElementsFoundByWeb:
        """Count element found by {{locator}}.

        Counts the amount of elements found by provided locator.
        """
        return CountElementsFoundByWeb(byType, byString, visibleOnly)

    @staticmethod
    def doubleclicknojs() -> DoubleClickNoJs:
        """Double Click {{element}}."""
        return DoubleClickNoJs()

    @staticmethod
    def doubleclickweb() -> DoubleClickWeb:
        """Double Click {{element}} using JavaScript."""
        return DoubleClickWeb()

    @staticmethod
    def getelementlocationweb() -> GetElementLocationWeb:
        """Get {{element}} location.

        Retrieves the location (x,y) of an element.
        """
        return GetElementLocationWeb()

    @staticmethod
    def gettagnameweb() -> GetTagNameWeb:
        """Get {{element}} tag name.

        Retrieves a tag name of an element.
        """
        return GetTagNameWeb()

    @staticmethod
    def getxpathweb() -> GetXPathWeb:
        """Get {{element}} xpath."""
        return GetXPathWeb()

    @staticmethod
    def isvisiblemultipleelementsweb(byType: str, elementsLocators: str) -> IsVisibleMultipleElementsWeb:
        """Check if given elements are visible, delimit elements locatorsby newline.

        check if provided elements are visible.
        """
        return IsVisibleMultipleElementsWeb(byType, elementsLocators)

    @staticmethod
    def switchtodefault() -> SwitchToDefault:
        """Run Switch to default content."""
        return SwitchToDefault()

    @staticmethod
    def switchtoframe() -> SwitchToFrame:
        """Run Switch to iFrame."""
        return SwitchToFrame()

    @staticmethod
    def switchtoparentframe() -> SwitchToParentFrame:
        """Run Switch to parent frame."""
        return SwitchToParentFrame()
