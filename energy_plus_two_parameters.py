# Two parameter classes for energy enhancement simulation
class EnergyPlus(object):
    # Create the attributes of the class
    def __init__(self):
        self.window_u_key = None
        self.window_u_values = None
        self.window_s_key = None
        self.window_s_values = None

    #  U attribute value assignment
    def set_window_u(self, window_u_key, window_u_values, val_range):
        window_u_max_value = max(window_u_values)
        window_u_min_value = min(window_u_values)
        # Checks that all values are in the range. If they are, they are assigned to the class attribute. Otherwise, they are not assigned
        if val_range[1] >= window_u_max_value and val_range[0] <= window_u_min_value:
            self.window_u_key = window_u_key
            self.window_u_values = window_u_values
            return True
        else:
            return False

    # Returns the value of the class U attribute
    def get_window_u(self):
        if self.window_u_values is not None and self.window_u_values is not None:
            return self.window_u_key, self.window_u_values

    #  The S attribute value is assigned
    def set_window_s(self, window_s_key, window_s_values, val_range):
        # Checks that all values are in the range. If they are, they are assigned to the class attribute. Otherwise, they are not assigned
        window_s_max_value = max(window_s_values)
        window_s_min_value = min(window_s_values)
        if val_range[1] >= window_s_max_value and val_range[0] <= window_s_min_value:
            result = True
            self.window_s_key = window_s_key
            self.window_s_values = window_s_values
            return True
        else:
            return False

    # Returns the class S attribute value
    def get_window_s(self):
        if self.window_s_key is not None and self.window_s_values is not None:
            return self.window_s_key, self.window_s_values
