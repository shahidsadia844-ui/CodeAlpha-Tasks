class CloudDatabaseSystem:
    def __init__(self):
        # Shuru mein humara cloud database khali hai (Hum unique entries ke liye set use kar rahe hain)
        self.cloud_database = set()
        print("--- Cloud Database System Activated ---")

    def insert_data(self, data_entry):
        print(f"\n[Incoming Data]: '{data_entry}' ko add karne ki koshish ki ja rahi hai...")
        
        # Strip function taake faltu spaces ki wajah se data duplicate na ho
        cleaned_entry = data_entry.strip().lower()

        # 1. Validation Mechanism: Check karna ke data pehle se hai ya nahi
        if cleaned_entry in self.cloud_database:
            # Data redundant hai, isko block kar dein
            print(f"⚠️ [REJECTED]: Data Classify ho gaya hai as 'REDUNDANT'.")
            print(f"-> Verification Failed: '{data_entry}' pehle se database mein majood hai.")
        else:
            # 2. Append Only Unique Data: Agar unique hai toh database mein add karein
            self.cloud_database.add(cleaned_entry)
            print(f"✅ [SUCCESS]: Data verified as 'UNIQUE'.")
            print(f"-> '{data_entry}' successfully cloud database mein save ho gaya.")

    def display_database(self):
        # Current database accuracy aur efficiency dekhne ke liye
        print("\n=========================================")
        print("         CURRENT CLOUD DATABASE          ")
        print("=========================================")
        if not self.cloud_database:
            print("Database khali hai.")
        else:
            for index, entry in enumerate(self.cloud_database, 1):
                print(f"{index}. {entry.capitalize()}")
        print(f"-----------------------------------------")
        print(f"Total Unique Verified Entries: {len(self.cloud_database)}")
        print("=========================================")


# --- System Simulation ---
if __name__ == "__main__":
    db = CloudDatabaseSystem()

    # 1. Kuch unique data entries add karte hain
    db.insert_data("Sadia Shahid")
    db.insert_data("Computer Science")
    
    # 2. Duplicate data add karne ki koshish (Redundancy Test)
    db.insert_data("Sadia Shahid")  # Bilkul same entry
    db.insert_data("computer science ")  # Shuru/end mein space aur lower case ke sath check

    # 3. Ek aur unique entry
    db.insert_data("Data Analytics")

    # 4. Final Database Display
    db.display_database()
  
