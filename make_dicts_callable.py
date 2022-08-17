class CallableDict:
    """Makes Python dictionaries callable by their keys."""

    def __init__(self, raw_dict):
        self.raw_dict = raw_dict
        self.initialize_attributes(self.raw_dict, self)

        @classmethod
        def initialize_attributes(cls, raw_dict, current_obj):
            for key, val in raw_dict.items():
                if isinstance(val, dict):
                    new_obj = cls(val)
                    setattr(current_obj, key, new_obj)
                else:
                    setattr(current_obj, key, val)
