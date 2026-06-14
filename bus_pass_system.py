import random

class CloudBusPassSystem:
    def __init__(self):
        # Cloud database to store ticket details safely (Prevents theft/loss)
        self.ticket_database = {}
        # Base ticket price
        self.ticket_price = 500.0 
        # Server scale capacity simulation
        self.active_servers = 1 
        print("--- Cloud-Based Bus Pass System Online & Secure ---")

    def monitor_and_scale_traffic(self, active_users):
        """Simulating Dynamic Provisioning of Servers for High Traffic"""
        print(f"\n[Traffic Monitor]: Current Active Users on System: {active_users}")
        if active_users > 1000:
            self.active_servers = 3
            print("⚡ [CLOUD SCALABILITY]: High traffic detected! Dynamic provisioning active. Scaled up to 3 Servers.")
        else:
            self.active_servers = 1
            print("🟢 [CLOUD STATUS]: Normal traffic. Operating efficiently on 1 Server.")

    def book_ticket(self, passenger_name, route, active_users_at_time):
        # 1. Handle traffic scaling first
        self.monitor_and_scale_traffic(active_users_at_time)
        
        # 2. Correct Pricing Check (Prevents incorrect pricing errors)
        final_price = self.ticket_price
        print(f"\n[Booking Request]: Processing ticket for {passenger_name}...")
        
        # 3. Generate Secure Digital Pass ID (Prevents loss and theft)
        ticket_id = f"BUS-PASS-{random.randint(10000, 99999)}"
        
        # Saving directly into cloud database dict
        self.ticket_database[ticket_id] = {
            "Passenger": passenger_name,
            "Route": route,
            "Price": final_price,
            "Status": "Verified & Paid"
        }
        
        print(f"✅ [SUCCESS]: Digital Pass Generated! ID: {ticket_id}")
        return ticket_id

    def view_pass_details(self, ticket_id):
        """Seamless and secure booking verification mechanism"""
        print(f"\n--- Fetching Pass from Cloud Database: {ticket_id} ---")
        if ticket_id in self.ticket_database:
            pass_info = self.ticket_database[ticket_id]
            print(f"Passenger Name : {pass_info['Passenger']}")
            print(f"Travel Route   : {pass_info['Route']}")
            print(f"Fare Charged   : Rs. {pass_info['Price']}")
            print(f"Status         : {pass_info['Status']}")
        else:
            print("❌ Error! No record found. Pass ID is invalid.")
        print("-----------------------------------------------------")


# --- Cloud System Execution Simulation ---
if __name__ == "__main__":
    system = CloudBusPassSystem()

    # Simulation 1: Single user booking under normal traffic
    ticket1 = system.book_ticket("Sadia Shahid", "Multan to Lahore", active_users_at_time=45)
    system.view_pass_details(ticket1)

    # Simulation 2: High traffic situation (System scales up dynamically)
    ticket2 = system.book_ticket("Ayesha Khan", "Islamabad to Karachi", active_users_at_time=1500)
    system.view_pass_details(ticket2)
