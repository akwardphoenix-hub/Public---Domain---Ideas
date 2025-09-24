def start_game():
    print("Masternode Odyssey: A Stoic Choose Your Own Adventure")
    print("Guided by The Brave Codex — Sky Hole Edition (with Kintsugi-Kiri).")
    print("Seek truth, fix first, scale harmony. You are a node in this game-civic mesh.\n")
    print("Type numbers for choices or 'q' to quit.\n")

    # Scene 1: Masternode Registration (Intention Node)
    print("Scene 1: Anchor Your Masternode")
    print("A Voidling awakens. Register to enter the Light Realm.")
    print("1. Verify with KYC (truth-first, no minor cams).")
    print("2. Attempt spoof (risks quarantine).")
    choice = input("Choice: ")
    if choice == 'q': return
    if choice == '1':
        print("Masternode anchored. Gain Legendary Node exemplar. Signed checkpoint logged.\n")
    elif choice == '2':
        print("Spoof detected. Airlock enacted (0–15 min). Snapshot ID: X1Y2Z3. Retry?")
        retry = input("Retry? (y/n): ")
        if retry.lower() != 'y': return
        print("Respawned. Containment lifted.\n")

    # Scene 2: Bee Law Incident (Healing Node)
    print("Scene 2: Bee Wallet Breach")
    print("Bees stolen. Bee Law (3-strike) triggers. Restore or escalate.")
    print("1. Replace 3x bees (restitution).")
    print("2. Appeal to Council Node (quorum review).")
    choice = input("Choice: ")
    if choice == 'q': return
    if choice == '1':
        print("Restitution complete. Pattern Keeper status earned.\n")
    elif choice == '2':
        print("Council votes (3+2 quorum). Fairness restored. Governance points +1.\n")

    # Scene 3: Wiggle Node Trial (Wiggle Node)
    print("Scene 3: Tree-Jelly Cultivation")
    print("Learn f₀ (wiggle baseline). Nudge tree-jellies.")
    print("1. Sing harmonics (reversible actuation).")
    print("2. Adjust vibrations (stress-monitored).")
    choice = input("Choice: ")
    if choice == 'q': return
    if choice == '1':
        print("Harmonics align. North Star Time boosts growth. Revert safe.\n")
    elif choice == '2':
        print("Vibrations tweak successful. Stress threshold clear.\n")

    # Scene 4: Bravery Trial (Kintsugi-Kiri Node)
    print("Scene 4: Orthrus Challenge")
    print("Two-headed guardian tests virtue. Apply Brave Codex principles.")
    print("1. Restore balance (healing ethic).")
    print("2. Invoke Kintsugi-Kiri (accept risks, act with dignity, repair the fracture).")
    choice = input("Choice: ")
    if choice == 'q': return
    if choice == '1':
        print("Balance restored. Excalibur unlocked. Human review logged.\n")
    elif choice == '2':
        print("Kintsugi-Kiri invoked: decisive cut made, fracture repaired with gold. Scars honored. Strength +1.\n")

    # Scene 5: Quartz Battery (VictoryUtility)
    print("Scene 5: Harmonic Future")
    print("Build Quartz Battery. Evaluate durability.")
    print("1. Test multi-input (tactical gain).")
    print("2. Add gyro lock (low collateral).")
    choice = input("Choice: ")
    if choice == 'q': return
    if choice == '1':
        print("Charge success. VictoryUtility = 0.8 (threshold 0.5). Approved.\n")
    elif choice == '2':
        print("Secure build. VictoryUtility = 0.9. Durable win.\n")

    # Scene 6: Council Node (Meta Governance)
    print("Scene 6: Ascend to Council")
    print("Propose a rule. Quorum decides.")
    print("1. Cultural integration (respect-first).")
    print("2. Pause for emergency (limbo mode).")
    choice = input("Choice: ")
    if choice == 'q': return
    if choice == '1':
        print("Consensus achieved. Compassion enshrined.\n")
    elif choice == '2':
        print("Pause logged. Happy Place invoked. Resume when ready.\n")

    print("End of Odyssey. Truth prevailed. Harmony scaled.\n")

if __name__ == "__main__":
    start_game()
