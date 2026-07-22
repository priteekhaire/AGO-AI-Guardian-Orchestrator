from detector import detect_attack
from event_sender import send_event

while True:

    payload = input("\nPayload (q to quit): ")

    if payload.lower() == "q":
        break

    attack = detect_attack(payload)

    if attack:
        print(f"\n[+] Attack Detected: {attack}")

        response = send_event(attack, payload)

        print("[+] Event sent to EventBridge")
        print(response)

    else:
        print("[-] No attack detected")
