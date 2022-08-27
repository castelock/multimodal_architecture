import zope.interface

class IEventInteraction(zope.interface.Interface):

    def __init__(self) -> None:
        super().__init__()
