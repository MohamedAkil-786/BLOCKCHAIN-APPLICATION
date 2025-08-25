# BLOCKCHAIN-APPLICATION

#🎟 Blockchain-for-Event-Tickets

A beginner-friendly blockchain implementation in Python for securely storing and verifying event tickets (movie shows, concerts, sports matches, etc.).
This project demonstrates how blockchain can ensure tamper-proof tickets, prevent fake/scalped tickets, and enable secure ticket transfer.

#🚀 Features

✅ Genesis block creation – the first block starts the event’s ticket registry.
✅ Add tickets – issue tickets to users with seat number, event name, and ID.
✅ Transfer tickets – re-assign tickets securely (no black marketing).
✅ Event-wise blockchain – each event has its own ticket chain.
✅ Verify ticket ownership – check if a ticket is valid & who owns it.
✅ Tamper-proof validation – ensures tickets haven’t been faked.
✅ Interactive CLI menu – issue, transfer, and verify tickets with user input.

#⚙ How It Works

When an event is created, it starts with a Genesis block (ticket registry).

Each issued ticket is stored as a block (with seat number + owner).

Tickets can be transferred to another person (new block added).

The blockchain links each record with SHA-256 hashes, ensuring no tampering.

Both organizers and customers can verify tickets to avoid scams.

#🔑 Concepts Used

🧱 Blockchain basics – tickets are stored as linked blocks.
🔒 SHA-256 hashing – prevents fake ticket creation.
✨ Immutability – no duplicate or forged tickets.
📜 Traceability – full history of ticket ownership.
✅ Tamper detection – validates ticket authenticity.
