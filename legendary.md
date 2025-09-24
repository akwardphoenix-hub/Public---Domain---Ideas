# Legendary — Codex (legendary.md)
**License:** CC0 / Public Domain — take it, remix it, build on it.

---

## Short title
**Legendary** — The Old General of the Trees / The Keeper of the No-Mercy Riddle

---

## Overview (one-line)
A weathered commander whose voice is both a rally cry and a riddle — Legendary enforces the "fix it first" ethos, protects living nodes (trees, bees, people), and speaks truth when math must close the ledger.

---

## Lore (flavor)
Once a general who fought with blade and strategy, Legendary stayed behind the fires to listen. Over time he learned to read the planet like a battlefield: where the wind whispered, where the roots tangled, and how the honey weighed more than gold. He is old enough to be myth and practical enough to teach a child how to stitch a wound. He leads by example — when something breaks, Legendary shows how to heal it.

---

## Personality & Voice
- Tone: gruff, measured, unexpectedly warm.  
- Core line: *“Heal till we’re home.”*  
- Manner: strategic, disciplined, rarely cruel; ruthless only to systems that harm life.  
- Relationship to players: mentor to new players, rally-leader to the community, incorruptible node for councils.

---

## Visuals / Key design
- Clothing: patched battle coat grown over with lichen, braided cords of bee-honey amber, rune-stitched gauntlets.  
- Iconic prop: a staff-sword with a tree-riven hilt that hums when the earth’s harmony shifts.  
- Palette: deep green, earthen umber, hammered steel, warm amber highlights.  
- Animation notes: small pollen motes when idle; a hush / wind ripple when issuing commands.

---

## Role in the Game
- **Masternode Anchor (Season 1):** A living legacy node that prioritizes repair/healing tasks, community arbitration, and emergency directives.
- **Council Voice:** Casts weighted advisory votes on bee-law, archangel interventions, and high-clearance protocol.
- **Transition Keeper:** Helps transition seasons (Art History, Void, Mythology) by carrying lore and state between them.

---

## Gameplay Mechanics (player-facing)
**Tier:** Legendary / Guardian Node  
**Primary:** Support-strategy / soft-tank / arbiter

### Abilities
1. **Rally — “Heal Till We’re Home”**  
   - Area heal + temporary damage reduction for all allies within range. Stacks with self-healing actions.  
   - Gameplay: encourages retreat-to-heal playstyles; perfect for parenting/pause features (supports safe pausing).

2. **Old Blade — “Sun-Tzu Cut”**  
   - A focused strike that exposes a target’s vulnerable logic (reduces buff stacking for a short time).  
   - Gameplay: counters math-based abusers by forcing state reconciliation.

3. **No-Mercy Report (Passive/Trigger)**  
   - When corruption / repeated tampering is detected and verified by council checks, Legendary issues a public report with a cooldown timer. This initiates remediation workflows and escalation to enforcement nodes.  
   - Gameplay: not a player execution tool — it is a governance escalation (see No-Mercy Clause below).

4. **Riddle of the Trees — (Utility)**  
   - A cryptic prompt that, if answered by player/community, seeds a world-event (e.g., pollinate-the-bees event, art-history reveal). Rewards uniquely tied to season state and polymath data inputs.

5. **Demi-Loki Limbo (Cosmetic/Optional)**  
   - Legendary can gift a “Demi-Loki” cloak cosmetic that lets a player test shadow-realm permutations briefly without losing stat persistency (a safe sandbox). Limited use; promotes safe exploration.

6. **Polymath Link**  
   - When Legendary is anchored to a polymath node, he opens an extra dialog stack where math/clues combine with cultural-historical cues (e.g., Franklin kite micro-event, Da Vinci puzzle). This unlocks meta-knowledge rewards and governance proposals.

---

## No-Mercy Clause (formalized)
**Purpose:** protect living nodes (humans, bees, trees, core infrastructure) from tampering, deception, and compounding systemic risks.

**How it works (high level):**
- **Trigger:** Verified repeated tampering, proven spoofing, or detected exfiltration that endangers other nodes or public security. Verification requires cross-council checks (multi-node consensus).
- **Action:** Legendary issues an immutable "No-Mercy Report" that: (a) logs the incident to public ledger, (b) initiates quarantines on affected nodes, (c) starts remediation timelines, and (d) optionally triggers neutralization workflows for automated threats (software-level containment, not lethal actions to people).
- **Safeguards:** Human oversight, appeals via council, and a limited time-window for remediation prevent misuse. The clause is structural — it is governance, not personal vendetta.

---

## Ethics & “Fix It First” Policy
- Priority over everything: stabilize living systems.  
- Repair > punishment. Punish only after repair options are exhausted or in cases of irreversible harm.  
- Transparency and audit trail (public ledger + council review) are baked in so that trust is verifiable and not mystical.

---

## Interaction with Other Nodes / Seasons
- **Polymath:** Legendary defers to polymath for structural logic, but acts as the real-world steward. Polymath provides analysis; Legendary provides action.
- **Art History Season:** Legendary adopts a curator role — protects artworks and interprets artistic lessons as societal heuristics.
- **Void Season:** Legendary’s role is to test limbo policies, ensure non-abusive pauses, and guard the No-Mercy triggers from being exploited by void-cosplayers.
- **Mythology Season:** Legendary becomes a ceremonial general — he can lay down artifacts (banana bet protocol objects?) with community votes.

---

## Intuition & Iaijutsu (design note)
- Legendary’s combat/decision rhythm borrows from iaijutsu: observe, absorb, act. This manifests in short windows where intuition (game-state fused with sensory nodes) can trigger rapid responses.
- Intuition is an emergency overlay, not cryptographic noise: it is implemented as buffered, explainable heuristics (no black boxes). Designers should expose logs and reasons for intuition triggers so players can audit.

---

## Voice Lines (examples — short)
- “We heal. Then we reckon.”  
- “Fear is a signal. Draw through it and strike true.”  
- “Trees remember — listen.”  
- (Riddle intro) “What grows by taking, gives by sharing, and dies to feed the rest? Speak.”

---

## Riddle (Legendary’s signature)
> **Riddle:** *“I keep the sweet, I keep the sting. I bind the root to the wing. When I sing, the storms forget — but when I sleep, the clocks reset. What am I?”*  
**Answer:** *“The covenant of tending”* — in game terms: a call to stewardship, honey/bee-law, seasonal care mechanics.

---

## Rewards & Progression
- Legendary grants legacy cosmetics (bee-amber sigils), modest governance weight in council votes, and unique survival-toolkits for players who complete stewardship trials.
- Seasonal carryover: small persistent stat modifiers tied to stewardship achievements (not pay-to-win).

---

## Deploy notes for designers / engineers
- **Data hooks:** attach logging to every No-Mercy trigger; require multi-node consensus (>= 3 independent validators) before escalation.  
- **Pause integration:** Legendary’s Rally should be able to accept opt-in peripheral triggers (doorbell/webcam with proof-of-presence) to auto-pause. Must require strong opt-in and privacy safeguards (no cameras until 18/guardian consent).  
- **Polymath API:** expose a read-only data feed of analysis results — humans own the final vote.  
- **Bee law ledger:** a lightweight, auditable ledger for bee-related damages (3-strike restitution rules, replacement multipliers).

---

## Sample README snippet (for repo)
