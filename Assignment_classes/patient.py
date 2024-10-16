class MedicalRecord:
    def __init__(self, diagnosis, treatment):
        self.diagnosis = diagnosis
        self.treatment = treatment
    
    def display_medical_info(self):
        print(f"name: {self.name}")
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Treatment: {self.treatment}")

class Billing:
    def __init__(self, billing_amount, insurance_provider):
        self.billing_amount = billing_amount
        self.insurance_provider = insurance_provider
    
    def display_billing_info(self):
        print(f"Billing Amount: Ugx {self.billing_amount}")
        print(f"Insurance Provider: {self.insurance_provider}")

class Patient(MedicalRecord, Billing):
    def __init__(self, name, patient_ID, room, diagnosis, treatment, billing_amount, insurance_provider):
        self.name = name
        self.patient_ID = patient_ID
        self.room = room
    
        MedicalRecord.__init__(self, diagnosis, treatment)
        Billing.__init__(self, billing_amount, insurance_provider)
    
    def display_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Patient ID: {self.patient_ID}")
        print(f"Room: {self.room}")
        
        self.display_medical_info()
        self.display_billing_info()

patient = Patient("Josh Babes", 143, "Room 12", "Flu", "Rest and Hydration", 50000, "LUKI Insurance")
patient.display_info()
