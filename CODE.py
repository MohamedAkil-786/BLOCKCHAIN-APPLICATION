import hashlib, json, time

# Utility function: SHA-256 hashing
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Define a Block
class Block:
    def _init_(self, index, prev_hash, data, timestamp=None):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "prev_hash": self.prev_hash,
            "data": self.data,
            "timestamp": self.timestamp
        }, sort_keys=True)
        return sha256(block_string)

# Blockchain for Tickets
class TicketBlockchain:
    def _init_(self):
        self.chain = []
        self.create_genesis()

    def create_genesis(self):
        genesis = Block(0, "0", {"msg": "Genesis Block"})
        self.chain.append(genesis)

    # ✅ Issue new ticket (only if TicketID not already used)
    def issue_ticket(self, ticket_id, owner, seat):
        # Prevent duplicate ticket issuance
        if self.verify_ticket(ticket_id) != "❌ Ticket not found.":
            return f"⚠ Ticket ID {ticket_id} already exists. Cannot issue again."

        prev = self.chain[-1]
        ticket_data = {"TicketID": ticket_id, "Owner": owner, "Seat": seat}
        new_block = Block(len(self.chain), prev.hash, ticket_data)
        self.chain.append(new_block)
        return f"✅ Ticket {ticket_id} issued to {owner} (Seat {seat})"

    # ✅ Transfer ticket with duplicate-owner prevention
    def transfer_ticket(self, ticket_id, new_owner):
        ticket_record = self.verify_ticket(ticket_id)
        if ticket_record == "❌ Ticket not found.":
            return "❌ Ticket not found."

        current_owner = ticket_record["Owner"]

        if current_owner == new_owner:
            return f"⚠ Ticket {ticket_id} is already owned by {new_owner}. Transfer not needed."

        prev = self.chain[-1]
        transfer_data = {
            "TicketID": ticket_id,
            "Owner": new_owner,
            "Seat": ticket_record["Seat"],
            "TransferredFrom": current_owner
        }
        new_block = Block(len(self.chain), prev.hash, transfer_data)
        self.chain.append(new_block)
        return f"✅ Ticket {ticket_id} transferred from {current_owner} to {new_owner}"

    # ✅ Verify and show only the latest ticket status
    def verify_ticket(self, ticket_id):
        latest_record = None
        for b in self.chain:
            if isinstance(b.data, dict) and b.data.get("TicketID") == ticket_id:
                latest_record = b.data
        return latest_record if latest_record else "❌ Ticket not found."

    # ✅ Validate blockchain integrity
    def is_valid(self):
        for i in range(1, len(self.chain)):
            prev = self.chain[i-1]
            curr = self.chain[i]
            if curr.prev_hash != prev.hash:
                return False
        return True


# -----------------------------
# Interactive CLI Menu
# -----------------------------
if _name_ == "_main_":
    bc = TicketBlockchain()

    while True:
        print("\n🎟 Ticket Blockchain Menu")
        print("1. Issue New Ticket")
        print("2. Transfer Ticket")
        print("3. Verify Ticket")
        print("4. Check Blockchain Validity")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            tid = input("Enter Ticket ID: ")
            owner = input("Enter Owner Name: ")
            seat = input("Enter Seat Number: ")
            print(bc.issue_ticket(tid, owner, seat))

        elif choice == "2":
            tid = input("Enter Ticket ID to transfer: ")
            new_owner = input("Enter New Owner Name: ")
            print(bc.transfer_ticket(tid, new_owner))

        elif choice == "3":
            tid = input("Enter Ticket ID to verify: ")
            record = bc.verify_ticket(tid)
            print("Status:", record)

        elif choice == "4":
            print("Blockchain valid?", bc.is_valid())

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")
