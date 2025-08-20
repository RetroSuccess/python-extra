"""
class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_name, emergency_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone
        
    def get_first_name(self): return self.first_name
    def get_last_name(self): return self.last_name
    def get_phone_number(self): return self.phone_number
    
    def set_phone_number(self, phone_number): self.phone_number = phone_number
        
        
class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner, charges):    
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practitioner = practitioner
        self.charges = charges
        
    def get_procedure_name(self): return self.procedure_name
    def get_charges(self): return self.charges
    
def main():
    # Create patient
    patient = Patient("John", "A", "Doe", "123 Main St", "Cape Town", "WC", "8000", "0123456789", "Jane Doe", "0987654321")

    # Create procedures
    p1 = Procedure("Physical Exam", "2025-08-19", "Dr. Irvine", 250.00)
    p2 = Procedure("X-ray", "2025-08-19", "Dr. Jamison", 500.00)
    p3 = Procedure("Blood Test", "2025-08-19", "Dr. Smith", 200.00)

    # Display info
    print("Patient Information:")
    print(f"{patient.first_name} {patient.middle_name} {patient.last_name}")
    print(f"Address: {patient.address}, {patient.city}, {patient.state}, {patient.zip_code}")
    print(f"Phone: {patient.phone_number}")
    print(f"Emergency Contact: {patient.emergency_name} ({patient.emergency_phone})\n")

    print("Procedures:")
    for p in [p1, p2, p3]:
        print(f"{p.procedure_name} on {p.procedure_date} by {p.practitioner} -- R{p.charges}")

    total = p1.charges + p2.charges + p3.charges
    print(f"\nTotal Charges: R{total}")


main()
"""

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_name, emergency_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

    def __str__(self):
        return (f"Patient: {self.first_name} {self.middle_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state}, {self.zip_code}\n"
                f"Phone: {self.phone_number}\n"
                f"Emergency Contact: {self.emergency_name} ({self.emergency_phone})")


class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner, charges):    
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practitioner = practitioner
        self.charges = charges

    def __str__(self):
        return f"{self.procedure_name} on {self.procedure_date} by {self.practitioner} -- R{self.charges:.2f}"


def main():
    # Create patient
    patient = Patient("John", "A", "Doe", "123 Main St", "Cape Town", "WC", "8000", "0123456789", "Jane Doe", "0987654321")

    # Create procedures
    procedures = [
        Procedure("Physical Exam", "2025-08-19", "Dr. Irvine", 250.00),
        Procedure("X-ray", "2025-08-19", "Dr. Jamison", 500.00),
        Procedure("Blood Test", "2025-08-19", "Dr. Smith", 200.00)
    ]

    # Display info
    print("")
    print(patient, "\n")
    print("Procedures:")
    for p in procedures:
        print(p)

    total = sum(p.charges for p in procedures)
    print(f"\nTotal Charges: R{total:.2f}")

main()
