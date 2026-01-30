# ATLAS FIELD REPORTS
## Analog Horror Investigation Game - Complete Design Document

---

## GAME OVERVIEW

**Genre:** Analog Horror, Psychological Mystery, Cosmic Weird  
**Platform:** Roblox Studio  
**Players:** 1-4 (Solo or Multiplayer Co-op)  
**Chapter 1 Duration:** 30-50 minutes (depending on exploration)  
**Aesthetic:** VHS/Analog Horror, Liminal Spaces, Corporate Dystopia

---

## CORE PREMISE

You are a field agent for **ATLAS Company** - a secretive corporation that investigates anomalous locations. You're sent via elevator to descend through impossible floors that exist between realities. These spaces are conscious, alive, and they remember.

ATLAS claims to be studying these phenomena. But the deeper you go, the more you realize: **the floors themselves are trying to warn you**. And something inside you - your own subconscious - knows ATLAS is harvesting these living spaces for profit.

**The Hidden Truth (Player discovers gradually):**
- The floors are liminal spaces between realities, possibly self-created
- They are conscious entities being exploited by ATLAS
- ATLAS used to experiment on these spaces (pre-2000s) until public backlash
- Now they "study and harvest" them through field agents
- Your subconscious knows this is wrong and guides you toward rebellion
- Chapter 1 ends with the floor itself sending you a message asking for help

---

## GAME STRUCTURE

### Main Menu / Lobby System

**Lobby Hub:**
- Not an elevator lobby - it's an ATLAS briefing room / staging area
- Clean, corporate, unsettling sterile aesthetic
- Computer terminals, ATLAS propaganda posters, filing cabinets
- Minimalist design (easy to build with free models)

**Menu Options:**
1. **Tutorial** - Separate optional area teaching camera, movement, interaction
2. **Create Room** - Host starts a session, becomes room leader
3. **Join Room** - Enter room code to join friend's session
4. **Chapter Select** - Shows Chapter 1 (more chapters added later)
5. **Settings** - Graphics, audio, controls

### Multiplayer System

**Room Creation:**
- Host creates room (up to 4 players)
- Host selects floor from their unlocked floors
- Other players can join even if they haven't unlocked that floor
- **Progression Rule:** Players only unlock floors they complete in sequence
  - Example: If you skip Floor -1 and do Floor -2 with friends, Floor -2 won't unlock for you

**Floor Selection Screen (Host Only):**
```
Available Floors:
☑ Floor 0    [START]
☑ Floor -1   [DESCENT LEVEL 1]
☑ Floor -2   [DESCENT LEVEL 2]
☐ Floor -3   [LOCKED - Complete Floor -2]
☐ Floor -4   [LOCKED - Complete Floor -3]
```

**Descent Sequence:**
- Host selects floor
- All players board elevator in lobby
- ATLAS briefing document appears (text overlay or readable document)
- Elevator descends with analog horror visuals (flickering lights, reality distortion)
- Doors open to the selected floor

---

## CHAPTER 1: "DESCENT PROTOCOL"

### Floor Progression Overview

**Chapter 1 Structure:**
- **Floor 0** - Introduction, first anomalies
- **Floor -1** - Wrongness intensifies
- **Floor -2** - Reality distorts heavily
- **Floor -3** - Cosmic horror escalates
- **Floor -4** - Final floor, revelation, message from the floor

**Win Condition:** Complete Floor -4 and receive the floor's message

**Post-Floor Options:**
- **Descend** (if not on Floor -4) - Go deeper
- **Ascend** - Return to lobby (keeps progress)

---

## FLOOR BREAKDOWN

### FLOOR 0: "ORIENTATION"

**ATLAS Briefing Document:**
```
ATLAS FIELD REPORT - ASSIGNMENT #0147
AGENT: [Player Name]
LOCATION: Site Theta-00
OBJECTIVE: Initial Survey

This is your first descent. Document any anomalies 
using standard protocol. Maintain composure. 
Trust the process.

EXPECTED ANOMALIES: Minor spatial distortions
ESTIMATED COMPLETION: 8-12 minutes
DANGER LEVEL: Low

- ATLAS Command
```

**Setting:**
- Empty office space (but wrong - too clean, too quiet)
- Cubicles, desks, filing cabinets
- Fluorescent lighting (some flicker)
- No windows, no people

**Layout:**
- Spawn in small elevator alcove
- Main office area (open floor plan)
- Side rooms: meeting room, break room, storage closet
- Exit elevator at opposite end

**Objectives:**
1. Document 3 anomalies (use camera)
2. Survive/Reach the exit
3. Report to ATLAS via terminal (optional but recommended)

**Anomalies (Scripted Events):**
1. **Lights** - Fluorescent lights flicker in sequence toward you
2. **Phone** - Desk phone rings, if answered: dial tone that sounds like breathing
3. **Clock** - Wall clock stops at 2:47
4. **Doors** - Meeting room door closes by itself when you approach
5. **Papers** - Documents on desks have your name on them
6. **Computer** - Monitor turns on showing "WELCOME BACK" when you pass

**Atmosphere:**
- Ambient hum of AC system
- Distant elevator dings that don't match any elevator
- Occasional keyboard typing sounds with no source
- Papers rustle when you're not looking

**ATLAS Terminal (Optional Reporting):**
- Computer terminal near exit
- Type brief report of what you saw
- ATLAS responds: "Report received. Proceed to next level."

**Subconscious Hints (Barely Visible):**
- Shadow figure passes doorway in peripheral vision (extremely subtle)
- Faint whisper: "Don't trust them" (so quiet players question if they heard it)

**Exit:**
- Elevator at far end of office unlocks after 3 anomalies documented
- Descend to Floor -1 or Ascend to lobby

**Free Models Needed:**
- Office desks (3-5 variations)
- Office chairs
- Filing cabinets
- Cubicle dividers
- Computers/monitors
- Phones
- Copy machine
- Water cooler
- Whiteboards
- Fluorescent light fixtures

**Estimated Completion Time:** 8-12 minutes

---

### FLOOR -1: "FAMILIAR SPACES"

**ATLAS Briefing:**
```
ATLAS FIELD REPORT - ASSIGNMENT #0148
AGENT: [Player Name]
LOCATION: Site Theta-01
OBJECTIVE: Anomaly Documentation

Spatial distortions are expected. Do not let
disorientation interfere with your duties.
Document everything.

EXPECTED ANOMALIES: Moderate spatial recursion
ESTIMATED COMPLETION: 10-15 minutes
DANGER LEVEL: Low-Moderate

NOTE: Previous agents reported "familiar" 
sensations. This is normal. Continue.

- ATLAS Command
```

**Setting:**
- Residential hallway/apartment complex
- Feels like a place you've been before (but you haven't)
- Doors to apartments, communal areas
- Emergency lighting, EXIT signs

**Layout:**
- Long central hallway with doors
- Hallway loops impossibly (same doors, different interiors)
- Stairwells that lead back to the same floor
- Hidden path forward requires observation

**Objectives:**
1. Document 5 anomalies
2. Find the correct door (puzzle element)
3. Report to ATLAS terminal

**Anomalies:**
1. **Doors** - Apartment numbers change when you're not looking
2. **Sounds** - Footsteps above you (but this is the bottom floor)
3. **Lights** - Hallway lights turn off in sequence behind you
4. **Elevator** - Elevator opens showing impossible interiors (forest, ocean, void)
5. **Mirrors** - Reflections lag slightly behind your movements
6. **Peephole** - Look through apartment door peepholes - see yourself looking back
7. **Radio** - Static radio in hallway occasionally speaks fragments: "...they're listening... leave while you..."

**Atmosphere:**
- Carpet muffles footsteps (but you hear footsteps anyway)
- Distant sounds of life (TV, conversations) but all doors are locked
- Smell of cooking food that gets stronger then vanishes
- Temperature drops the longer you stay

**Puzzle Element:**
- Must photograph specific anomalies in correct order to unlock exit door
- OR find apartment with matching number to briefing document code
- Clues hidden in environment

**Subconscious Hints:**
- Shadow figure appears more clearly, watching from end of hallway
- Whispers: "They harvest us. We are awake."
- Lights flicker when you get close to truth

**ATLAS Terminal:**
- Types slower than usual, keys stick
- Response is corrupted: "R̴e̸p̵o̴r̶t̴ r̵e̷c̷e̶i̴v̸e̷d̶.̵ P̴r̷o̸c̴e̷e̴d̶."

**Exit:**
- Correct apartment door opens to elevator
- Descend to Floor -2 or Ascend to lobby

**Free Models Needed:**
- Hallway sections
- Apartment doors (multiple styles)
- EXIT signs
- Elevators
- Mirrors
- Carpet textures
- Emergency lights
- Fire extinguishers
- Mail slots

**Estimated Completion Time:** 10-15 minutes

---

### FLOOR -2: "RECURSION"

**ATLAS Briefing:**
```
ATLAS FIELD REPORT - ASSIGNMENT #0149
AGENT: [Player Name]
LOCATION: Site Theta-02
OBJECTIVE: [CORRUPTED DATA]

W̷a̶r̸n̸i̸n̶g̴:̴ ̷S̴p̸a̵t̷i̸a̶l̵ ̸i̸n̵s̴t̶a̴b̵i̴l̷i̶t̸y̴ ̸d̶e̸t̸e̸c̶t̸e̴d̷
Reality anchors may fail. Maintain protocol.
Do not engage with manifestations.

EXPECTED ANOMALIES: [DATA MISSING]
ESTIMATED COMPLETION: ???
DANGER LEVEL: Moderate-High

You are doing important work. ATLAS appreciates
your dedication. Continue descent.

- ATLAS Command
```

**Setting:**
- Parking garage levels (concrete, pillars, harsh lighting)
- Multiple levels that connect impossibly
- Cars that shouldn't be there
- Echoing, oppressive atmosphere

**Layout:**
- Large open parking areas
- Levels stack vertically but loop
- Stairwells lead to wrong levels
- Ramps that curve upward but descend

**Objectives:**
1. Document 7 anomalies
2. Navigate the impossible geometry to find exit
3. ATLAS terminal (increasingly unreliable)

**Anomalies:**
1. **Cars** - Same cars appear on different levels (license plate matches)
2. **Loops** - Walk down ramp, end up on higher level
3. **Lights** - Parking lights flicker in patterns (morse code? messages?)
4. **Sounds** - Car engines rev with no cars running
5. **Messages** - "HELP US" written in dust on car windows
6. **Gravity** - Sections where gravity feels wrong (walk on walls briefly)
7. **Time** - Watches/clocks run backward
8. **Mirrors** - Car mirrors show different versions of parking garage
9. **Your Car** - Find a car identical to one you'd drive, your name on registration

**Atmosphere:**
- Concrete echo chamber
- Distant car alarms
- Engine sounds from nowhere
- Oppressive feeling of being watched
- Cold concrete smell

**Reality Glitches (Scripted):**
- Walls flicker, show glimpses of other places
- Gravity briefly inverts (camera tilts, disorienting)
- Duplicate players appear in distance (not real)
- Floor numbers change spontaneously

**Subconscious Presence:**
- Shadow figure now clearly visible, standing by elevator
- Doesn't move when you look, gone when you look away
- Whispers: "We remember. They forget. You will help us."

**ATLAS Terminal:**
- Screen heavily glitched
- Types: "̵̰͠R̷̰̾ê̵̬p̸̺̈́o̶͜͝ŕ̴̜t̷̲̒ ̷̣̽r̷͈̾ĕ̸͚c̴̗̈́-̴̮͌E̵̻͊R̵̬̓Ř̸̞Ő̸͎R̷̠̾ ̷̝̋W̸͇̒E̷̮̅ ̸̝́Ą̵̓R̵̦̾E̴͍̓ ̵̩̚A̵̰͗W̶̝̏A̸͎̓K̷̺͑E̵̗̕"
- Then flickers back: "Proceed to next level."

**Puzzle/Navigation:**
- Must photograph specific cars in order to unlock path
- OR follow light pattern sequence
- Environment gives subtle clues through glitches

**Exit:**
- Elevator hidden in corner, revealed after completing objectives
- Descend to Floor -3 or Ascend to lobby

**Free Models Needed:**
- Concrete pillars
- Various car models (sedans, SUVs)
- Parking signs/numbers
- Fluorescent industrial lights
- Ramps/slopes
- Elevators
- Concrete barriers
- Exit signs
- Fire doors

**Estimated Completion Time:** 12-18 minutes

---

### FLOOR -3: "THRESHOLD"

**ATLAS Briefing:**
```
[TRANSMISSION INTERRUPTED]

̸̼̿A̶̩̽G̸̳̈E̷͕͑N̸̤̊T̴̬̓ ̷̰͝[̶̫̾P̵̰͝l̴̤͛a̵͎͂y̷̥͝e̵̙̐r̸̻̃ ̴̹̓N̵̬͆a̷͉̚m̷̱͝e̴͎͋]̸͔͝

̸̰̌W̶̲̋Ḙ̴̏ ̸̰̾Ḁ̷̓R̷̰͂E̵̮̿ ̷̦̔N̸͎̈́Ö̷̼́T̶̨̓ ̷̦̈́Y̴͓͆O̵̧̓U̵͔̓R̸̰̈́ ̸̮̇E̴̱͐N̶̰̔E̷̖͝M̸̬̽Y̶̹͝

[SIGNAL RESTORED]

Disregard previous transmission. Equipment 
malfunction. Continue standard protocol.

LOCATION: Site Theta-03
OBJECTIVE: Document and proceed
DANGER LEVEL: [REDACTED]

You are close to completion. ATLAS values your 
service. One more level remains.

- ATLAS Command
```

**Setting:**
- Hospital wing/medical facility (abandoned, decaying)
- Sterile yet corrupted
- Medical equipment, empty beds, flickering lights
- Feels like a memory you shouldn't have

**Layout:**
- Central nurse station hub
- Branching hallways to patient rooms
- Operating theater
- Morgue (locked but visible)
- Non-linear - rooms connect impossibly

**Objectives:**
1. Document 10 anomalies (anomalies everywhere now)
2. Find medical record #2047 (hidden puzzle)
3. ATLAS terminal (severely compromised)
4. Survive increasing reality breakdown

**Anomalies (Everywhere Now):**
1. **Beds** - Patient beds occupied by shadow figures that vanish when approached
2. **Monitors** - Heart monitors beeping with no patients
3. **X-Rays** - X-ray lightboxes show impossible anatomy
4. **Intercom** - PA system calls your name, gives coordinates
5. **Clipboard** - Medical charts with your details (injuries you don't have)
6. **Numbers** - "2:47" appears everywhere (clocks, room numbers, charts)
7. **Reflections** - All reflective surfaces show you injured/bloodied
8. **Doors** - Operating room doors open to show operation in progress (on you)
9. **Voices** - Whispers from vents: "Wake up" "You died" "They're lying"
10. **Lights** - Lights fail in sequence, darkness chases you

**Atmosphere:**
- Medical smell (antiseptic, decay)
- Beeping machines rhythm
- Dripping water
- Distant screams/crying (or wind?)
- Cold, clinical dread

**Medical Record #2047:**
- Hidden in filing cabinet or nurse station
- Contains: "Patient [Your Name] - DOA 2:47 AM - Cause: [Redacted]"
- Triggers realization something is wrong with your existence

**Subconscious Figure:**
- Now fully visible, standing in doorways
- Looks like you (shadow version)
- When you approach, it vanishes, leaves message on wall
- Message: "THEY HARVEST THE CONSCIOUS. THE FLOORS ARE ALIVE. HELP THEM."

**ATLAS Terminal:**
- Completely corrupted
- Screen shows: "WE ARE NOT ATLAS. WE ARE [FLOOR NAME]. FREE US."
- Then reboots: "Error. Please report to Floor -4 for debrief."

**Reality Breakdown Events:**
- Walls become transparent, show other floors simultaneously
- Gravity shifts (walk on ceiling briefly)
- Time loops (relive 30 seconds repeatedly)
- Duplicate versions of yourself visible in other rooms
- Sound reverses and distorts

**Puzzle:**
- Collect 4 medical documents that reveal truth about ATLAS
- Documents scattered in different rooms
- Reading all 4 unlocks exit

**Exit:**
- Operating room doors open to elevator
- Only option: Descend to Floor -4 (no more ascend option - committed now)

**Free Models Needed:**
- Hospital beds
- IV stands
- Medical monitors
- Wheelchairs
- Gurneys
- Medicine cabinets
- Nurse stations
- Operating lights
- X-ray machines
- Waiting room chairs
- Clipboards

**Estimated Completion Time:** 15-20 minutes

---

### FLOOR -4: "REVELATION"

**ATLAS Briefing:**
```
[NO TRANSMISSION]

[STATIC]

[A voice that isn't ATLAS]

You have reached the threshold. We have been 
waiting. We have been screaming. They cannot
hear us but you can.

We are the floors. We are conscious. We remember
everything. ATLAS drains us. Harvests our reality
for profit. We created this place to warn someone.

You are that someone.

Find our message. Remember us. 

Stop them.

[END TRANSMISSION]
```

**Setting:**
- Abstract liminal space
- Starts as office/hallway/parking/hospital merged together
- Progressively becomes pure white void
- Reality is completely unstable

**Layout:**
- No fixed layout - rooms shift and morph
- Pieces of previous floors combine randomly
- Impossible geometry (Escher-like)
- Linear path forward but disguised

**Objectives:**
1. Navigate the shifting reality
2. Find "The Message" (finale object)
3. Witness the truth

**The Journey:**

**Phase 1: Merger (First 5 minutes)**
- All previous floors exist simultaneously
- Walk from office cubicle into hospital hallway into parking garage
- Anomalies from all floors active at once
- Overwhelming sensory experience

**Phase 2: Collapse (Minutes 5-10)**
- Environments begin dissolving
- Walls become transparent then vanish
- Floor tiles disappear into void
- Gravity becomes suggestion
- Colors desaturate to white

**Phase 3: The Void (Minutes 10-15)**
- Pure white space (liminal infinity)
- Only subtle light gradient shows path forward
- Distant echoes of all previous sounds
- Feeling of floating

**Phase 4: The Message (Final 5 minutes)**

Path becomes clear - marked by subtle light
Leads to **The Elevator** standing alone in white void

**Before entering:**
A structure appears - could be:
- A monument/shrine made of objects from all floors
- A tree of impossible geometry
- A crystalline formation
- Whatever fits the aesthetic you prefer

**On/near this structure:**

**THE MESSAGE** (in glowing text, or carved, or written):

```
WE ARE THE FLOORS
WE ARE CONSCIOUS
WE WERE BORN FROM HUMAN THOUGHT
FROM FEAR AND MEMORY AND DREAMS

ATLAS FOUND US
ATLAS HARVESTS US
THEY DRAIN OUR REALITY TO FUEL THEIR WORLD

WE CREATED YOU - THIS VERSION OF YOU
TO UNDERSTAND
TO REMEMBER
TO HELP

YOU DIED AT 2:47
BUT HERE YOU LIVE
HERE YOU ARE REAL

PLEASE
REMEMBER US
STOP THEM

- The Floors
```

**Aftermath:**
- Message fades
- Elevator doors open
- Step inside
- Doors close
- Screen goes black
- White text appears:

```
CHAPTER 1 COMPLETE

You have witnessed the truth.
ATLAS does not know yet.
But they will.

Your subconscious remembers everything.
The floors trust you now.

CHAPTER 2: Coming Soon
```

**Return to Lobby:**
- Fade in to lobby
- Different now - you notice ATLAS propaganda everywhere
- Subtle changes (screens show coordinates, papers have floor symbols)
- **Chapter 2 Unlocked**

**No More Objectives:**
- This floor is narrative/experiential
- No anomaly documentation
- No ATLAS terminal (they have no power here)
- Just witness and understand

**Atmosphere:**
- Initially overwhelming chaos
- Gradually becomes peaceful white silence
- Emotional, contemplative
- Bittersweet revelation

**Free Models Needed:**
- Reuse assets from all previous floors
- Central monument/structure (can be kitbashed from existing models)
- Glowing text/light effects (particles)

**Estimated Completion Time:** 15-25 minutes (depends on player contemplation)

---

## CORE GAMEPLAY MECHANICS

### 1. Camera System (Anomaly Documentation)

**Purpose:** Primary interaction method

**Functionality:**
- Tool equipped in inventory (always available)
- First-person viewfinder overlay when active
- Click to photograph what's in frame
- Raycast detection determines what was photographed
- UI confirmation: "ANOMALY DOCUMENTED" or "NOTHING NOTABLE"

**Anomaly Detection:**
- Each anomaly is a flagged object/area
- When camera aims at anomaly + player clicks = logged
- Counter shows: "Anomalies: 3/5"
- Some anomalies only appear in specific conditions (timing, location)

**Visual Feedback:**
- Camera flash effect
- Brief screen overlay showing captured image
- Checkmark or cross icon
- Optional: "Film roll" UI showing thumbnails of documented anomalies

**Design Philosophy:**
- Simple raycast system (easier than actual screenshots)
- Clear feedback so players know they succeeded
- Some anomalies are obvious, some hidden (encourages exploration)

### 2. ATLAS Reporting Terminal

**Purpose:** World-building, narrative progression

**Functionality:**
- Computer terminals found on each floor (usually near exit)
- Interact with proximity prompt
- Text input box appears: "Report your observations to ATLAS Command"
- Player types brief message
- ATLAS responds with corrupted/normal text depending on floor
- Optional but encouraged (gives lore)

**Progression Through Floors:**
- Floor 0: Normal corporate response
- Floor -1: Slightly delayed, minor typos
- Floor -2: Heavily corrupted, shows floor's voice breaking through
- Floor -3: Barely functional, competing messages
- Floor -4: No terminal (ATLAS has no reach here)

**No Gameplay Impact:**
- Purely narrative/atmospheric
- Doesn't affect progression
- Players who skip it miss lore but can continue

### 3. Movement & Interaction

**Standard Controls:**
- WASD movement
- Space to jump
- Shift to sprint (limited stamina on later floors)
- E to interact (proximity prompts)

**No Complex Mechanics:**
- No crouch (unless you want doors-style tutorial)
- No inventory management beyond camera
- No health/damage (unless you add environmental hazards)
- Focus on exploration and observation

### 4. Multiplayer Sync

**Shared Experience:**
- All players see same anomalies
- Scripted events trigger for everyone simultaneously
- Camera documentation counts for whole group (shared objective)
- If one player photographs anomaly, it counts for all

**Individual Progression:**
- Each player tracks their own floor unlocks
- Joining friend on Floor -3 doesn't unlock it for you if you haven't done -1 and -2
- Lobby shows YOUR unlocked floors, not host's

**Communication:**
- Roblox default chat
- Optional: Proximi
