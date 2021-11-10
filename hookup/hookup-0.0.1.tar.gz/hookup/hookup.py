from typing import List


class Hookup:
    """
    A decorator to wrap a class and modify it's __setattr__ call
    allowing us to trap changes on certain named attributes, and fire a callback when the change occurs
    """

    def __init__(self, attrs: List[str], callback: str):
        """
        __init__ takes the attributes from the callback:
            - attrs - a List of attributes to trap changes for
            - callback - the function name on the class that will be used as a callback on change
        """
        self.__attribute_list = attrs
        self.__callback = callback

    def __call__(self, cls):
        """
        The __call__ function is used to directly modify the decorated class
        Here we implement a custom setattr function, and directly override cls.__setattr__ on the decorated class
        """
        __original_setattr = cls.__setattr__
        __attribute_list = self.__attribute_list
        __callback = getattr(cls, self.__callback)

        def setattr(self, name, value):
            """
            Keep in mind that `self` here refers to the decorated object, NOT the decorator `Hotwire` object
            """
            # We need the current value to determine if a change has occurred
            current = getattr(self, name, None)

            # Execute the original __setattr__ to actually perform the work first
            # since we want all of the attribute values to be in place _before_ calling any callback
            __original_setattr(self, name, value)

            # Note: we only care about _change_, not instantiation, so ignore current values of None
            # If the original value is not None, and the value has changed, call the callback function
            if current is not None and name in __attribute_list:
                if current != value:
                    __callback(self)

        # Replace the decorated class' __setattr__ with the above setattr function
        cls.__setattr__ = setattr

        return cls
