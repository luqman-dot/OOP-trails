class MedicalRecord:
    def __init__(self, diagnosis, treatment):
        self.diagnosis = diagnosis
        self.treatment = treatment
    
    def display_medical_info(self):
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Treatment: {self.treatment}")

class Billing:
    def __init__(self, billing_amount, insurance_provider):
        self.billing_amount = billing_amount
        self.insurance_provider = insurance_provider
    
    def display_billing_info(self):
        print(f"Billing Amount: Ugx {self.billing_amount}")
        print(f"Insurance Provider: {self.insurance_provider}")

class MedicalStaff:
    def __init__(self, doctor_name, nurse_name):
        self.doctor_name = doctor_name
        self.nurse_name = nurse_name
    
    def display_staff_info(self):
        print(f"Doctor: {self.doctor_name}")
        print(f"Nurse: {self.nurse_name}")

class Patient(MedicalRecord, Billing, MedicalStaff):
    def __init__(self, name, patient_ID, room, diagnosis, treatment, billing_amount, insurance_provider, doctor_name, nurse_name):
        self.name = name
        self.patient_ID = patient_ID
        self.room = room

        MedicalRecord.__init__(self, diagnosis, treatment)
        Billing.__init__(self, billing_amount, insurance_provider)
        MedicalStaff.__init__(self, doctor_name, nurse_name)
    
    def display_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Patient ID: {self.patient_ID}")
        print(f"Room: {self.room}")

        self.display_medical_info()
        self.display_billing_info()
        self.display_staff_info()

# Example usage
patient = Patient(
    name="Josh babes", 
    patient_ID=143, 
    room="Room 12", 
    diagnosis="Flu", 
    treatment="Rest and Hydration", 
    billing_amount=50000, 
    insurance_provider="LUKI Insurance", 
    doctor_name="Dr. ROland", 
    nurse_name="Nurse George"
)
patient.display_info()
