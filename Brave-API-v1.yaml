apiVersion: v1
kind: BraveCodex
metadata:
  name: brave-api
  description: >
    API for interfacing with the Brave Codex.  
    Designed to embed courage-as-logic into broader systems, games, and governance.  
    Codified for Native lineage, cascaded for pattern keepers, and harmonized across realms.
endpoints:
  - name: /bravery/check
    method: POST
    description: >
      Submits a context (event, trial, decision) and evaluates whether the action  
      aligns with the Codex of the Brave.  
      Outputs a "Bravery Index" (0–100%) with qualitative notes.
    input:
      context: string
      playerState: object
    output:
      braveryIndex: integer
      notes: string

  - name: /bravery/chant
    method: GET
    description: >
      Returns the harmonics for collective chants or healing mantras.  
      Pulls from council-approved corpus (e.g., Lord’s Prayer, native songs, uppercut protocol chants).
    output:
      chant: string
      resonance: float

  - name: /bravery/ledger
    method: GET
    description: >
      Returns bravery instances recorded on-chain (human and cosmic).  
      Ledger is immutable, transparent, and ghost-free.
    output:
      entries: list
      verification: string

  - name: /bravery/mirror
    method: POST
    description: >
      Provides a mirror-response protocol: holding up courage back to the source of fear,  
      shadows, or demons.  
      Can be invoked manually or triggered automatically in the Excalibur Node.
    input:
      threatContext: string
    output:
      mirroredBack: string
      resolutionPath: string
