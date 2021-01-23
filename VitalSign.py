class VitalSign:
    def __init__(self, name, unit, min_norm_val, max_norm_val):
        self.name = name
        self.unit = unit
        self.min_norm_val = min_norm_val
        self.max_norm_val = max_norm_val
        self.value = None


    def is_abnormal(self):
        normal = self.min_norm_val <= self.value <= self.max_norm_val
        return not normal
