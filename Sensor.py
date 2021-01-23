from VitalSign import VitalSign

BLOOD_PRESSURE_RANGES = {
    "normal": (120, 129),
    "hypertensive": (130, 140)
}

class Sensor:
    def __init__(self, comorbidities):
        self.body_temp = VitalSign("Body Temperature", "celcius", 36.5, 37.5)
        self.heart_rate = VitalSign("Heart Rate", "bpm", 50, 70)
        if "Hypertension" in comorbidities:
            print("Sensor will be adapted for hypertensive patient.")
            bpressure_range = BLOOD_PRESSURE_RANGES["hypertensive"]
        else:
            bpressure_range = BLOOD_PRESSURE_RANGES["normal"]
        self.bpressure = VitalSign("Blood Pressure", "mmHg", bpressure_range[0], bpressure_range[1])
        self.boxygen = VitalSign("Blood Oxygen", "percent", 95, 100)
        print("Sensor configured successfully.")


    def monitor_vital_signs(self):
        print("\n Monitoring Vital Signs ... \n")
        self.body_temp.value = float(input(f"{self.body_temp.name}: "))
        self.heart_rate.value = int(input(f"{self.heart_rate.name}: "))
        self.bpressure.value = int(input(f"{self.bpressure.name}: "))
        self.boxygen.value = int(input(f"{self.boxygen.name}: "))


    def is_emergency(self):
        # body temperature is not regarded as a reason for calling the ambulance
        is_emergency = False
        for vital_sign in [self.heart_rate, self.bpressure, self.boxygen]:
            if vital_sign.is_abnormal():
                print(f"{vital_sign.name} has an abnormal value of {vital_sign.value} {vital_sign.unit}")
                is_emergency = True
        if is_emergency:
            print("Emergency detected!")
        return is_emergency


    def generate_emergency_vital_sign_report(self):
        report_lines = ["Vital signs of the patient at emergency: "]
        for vital_sign in [self.body_temp, self.heart_rate, self.bpressure, self.boxygen]:
            report_lines.append(f"{vital_sign.name}: {vital_sign.value} {vital_sign.unit}")
        return "\n".join(report_lines)
        
        # TODO: Is the for loop understandable enough or should we leave this?
        # return f"""
        #     Vital signs of the patient at emergency:
        #     {self.body_temp.name}: {self.body_temp.value} {self.body_temp.unit}
        #     {self.heart_rate.name}: {self.heart_rate.value} {self.heart_rate.unit}
        #     {self.bpressure.name}: {self.bpressure.value} {self.bpressure.unit}
        #     {self.boxygen.name}: {self.boxygen.value} {self.boxygen.unit}
        # """


    def detect_emergency(self):
        emergency_detected = False
        while not emergency_detected:
            self.monitor_vital_signs()
            emergency_detected = self.is_emergency()
        return self.generate_emergency_vital_sign_report()
