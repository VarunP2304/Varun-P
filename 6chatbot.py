class ChatBot:
    def __init__(self, name="Bot", company_name=""):
        self.name = name
        self.company_name = company_name
        self.custom_fields = {}

    def start_conversation(self):
        print(f"Hey, my name is {self.name} from {self.company_name}. What can I help you with today?")
        self.book_appointment()

    def book_appointment(self):
        self.get_specialist()
        self.get_doctor()
        self.get_appointment_details()
        self.confirm_appointment()
        self.get_customer_details()
        self.confirm_booking()

    def get_specialist(self):
        specialists = ["General Medicine", "Ophthalmology", "Orthopaedics"]
        print("What specialist would you like to book?")
        for i, specialist in enumerate(specialists, 1):
            print(f"{i}. {specialist}")
        choice = int(input("Enter the number of your choice: ").strip())
        self.custom_fields['specialist'] = specialists[choice - 1]

    def get_doctor(self):
        doctors = {
            "General Medicine": ["Dr. Smith", "Dr. Johnson"],
            "Ophthalmology": ["Dr. Brown", "Dr. Davis"],
            "Orthopaedics": ["Dr. Miller", "Dr. Wilson"]
        }
        chosen_specialist = self.custom_fields['specialist']
        print(f"Which doctor would you like to book for {chosen_specialist}?")
        for i, doctor in enumerate(doctors[chosen_specialist], 1):
            print(f"{i}. {doctor}")
        choice = int(input("Enter the number of your choice: ").strip())
        self.custom_fields['doctor'] = doctors[chosen_specialist][choice - 1]

    def get_appointment_details(self):
        date_time = input("What date and time would you like to book an appointment? (e.g., YYYY-MM-DD HH:MM) ").strip()
        self.custom_fields['appointment_date'], self.custom_fields['appointment_time'] = date_time.split()

    def confirm_appointment(self):
        confirmation = input(f"Confirm booking with {self.custom_fields['doctor']} on {self.custom_fields['appointment_date']} at {self.custom_fields['appointment_time']}? (yes/no) ").lower()
        if confirmation != "yes":
            self.get_appointment_details()
            self.confirm_appointment()

    def get_customer_details(self):
        self.custom_fields['customer_name'] = input("May I have your name? ")
        self.custom_fields['contact_details'] = input("Please provide your contact details: ")

    def confirm_booking(self):
        print(f"Thank you, {self.custom_fields['customer_name']}. Your appointment with {self.custom_fields['doctor']} is booked for {self.custom_fields['appointment_date']} at {self.custom_fields['appointment_time']}.")
        print("Is there anything else I can help you with?")

# Example usage
chatbot = ChatBot(name="Alice", company_name="XYZ Corp")
chatbot.start_conversation()
