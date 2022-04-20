"""This package contains all the addon proxy's actions."""
from .countelementsfoundbyandroid import CountElementsFoundByAndroid
from .getelementlocationandroid import GetElementLocationAndroid
from .gettagnameandroid import GetTagNameAndroid
from .getxpathandroid import GetXPathAndroid
from .isvisiblemultipleelementsandroid import IsVisibleMultipleElementsAndroid
from .relativetapandroid import RelativeTapAndroid
from .countelementsfoundbyios import CountElementsFoundByIOS
from .getelementlocationios import GetElementLocationIOS
from .gettagnameios import GetTagNameIOS
from .getxpathios import GetXPathIOS
from .isvisiblemultipleelementsios import IsVisibleMultipleElementsIOS
from .relativetapios import RelativeTapIOS
from .countelementsfoundbyweb import CountElementsFoundByWeb
from .doubleclicknojs import DoubleClickNoJs
from .doubleclickweb import DoubleClickWeb
from .getelementlocationweb import GetElementLocationWeb
from .gettagnameweb import GetTagNameWeb
from .getxpathweb import GetXPathWeb
from .isvisiblemultipleelementsweb import IsVisibleMultipleElementsWeb
from .switchtodefault import SwitchToDefault
from .switchtoframe import SwitchToFrame
from .switchtoparentframe import SwitchToParentFrame

__all__ = ["CountElementsFoundByAndroid", "GetElementLocationAndroid", "GetTagNameAndroid", "GetXPathAndroid", "IsVisibleMultipleElementsAndroid", "RelativeTapAndroid", "CountElementsFoundByIOS", "GetElementLocationIOS", "GetTagNameIOS", "GetXPathIOS",
           "IsVisibleMultipleElementsIOS", "RelativeTapIOS", "CountElementsFoundByWeb", "DoubleClickNoJs", "DoubleClickWeb", "GetElementLocationWeb", "GetTagNameWeb", "GetXPathWeb", "IsVisibleMultipleElementsWeb", "SwitchToDefault", "SwitchToFrame", "SwitchToParentFrame"]
