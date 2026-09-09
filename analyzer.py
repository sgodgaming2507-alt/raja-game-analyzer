import json
from datetime import datetime

class GameAnalyzer:
    def __init__(self, filename="game_history.json"):
        self.filename = filename
        self.history = self.load_data()

    def load_data(self):
        """Saved history load karta hai agar file mojood ho"""
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        """Data ko JSON file mein save karta hai"""
        with open(self.filename, "w") as f:
            json.dump(self.history, f, indent=4)

    def add_result(self, period_id, number, result_type):
        """Naya round record karta hai"""
        record = {
            "period": str(period_id),
            "number": int(number),
            "result": str(result_type).capitalize(), # 'Big' ya 'Small'
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.history.append(record)
        self.save_data()
        print(f"[+] Recorded -> Period: {period_id} | Number: {number} | Result: {result_type}")

    def show_statistics(self):
        """Total records par statistical summary dikhata hai"""
        total = len(self.history)
        if total == 0:
            print("[-] Koi data available nahi hai analysis ke liye.")
            return

        big_count = sum(1 for x in self.history if x["result"] == "Big")
        small_count = sum(1 for x in self.history if x["result"] == "Small")
        
        print("\n--- Game Statistics ---")
        print(f"Total Rounds Tracked: {total}")
        print(f"Big Count: {big_count} ({(big_count/total)*100:.2f}%)")
        print(f"Small Count: {small_count} ({(small_count/total)*100:.2f}%)")
        print("-----------------------\n")

# --- Example Usage ---
if __name__ == "__main__":
    analyzer = GameAnalyzer()
    
    # Test ke liye dummy data add kar sakte hain:
    # analyzer.add_result("2026091001", 7, "Big")
    # analyzer.add_result("2026091002", 3, "Small")
    
    analyzer.show_statistics()
