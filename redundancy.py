class RedundancySystem:
    def __init__(self): self.db = set()
    def insert(self, data):
        clean = data.strip().lower()
        if clean in self.db: print(f"Rejected Duplicate: {data}")
        else: self.db.add(clean); print(f"Saved Unique: {data}")

sys = RedundancySystem()
sys.insert("Sadia")
sys.insert("Sadia")
