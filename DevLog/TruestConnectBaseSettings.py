# Let's programmatically generate the highly structured, machine-readable text file containing the entire blueprint.
import os

war_plan_content = """#===============================================================================
# TRUESTCONNECT: SYSTEM BLUEPRINT & ALPHA PROTOCOL WAR PLAN
# MODE: SECURE, LOCAL-ONLY, ZERO-CLOUD, HUMAN-CENTRIC PERSONAL CHRONICLE
# TARGET INGESTION: EXTREME CONTEXT LLM ARCHITECT / CODE ACCELERATOR (CURSOR/CLAUDE)
#===============================================================================

#-------------------------------------------------------------------------------
# SECTION 1: SYSTEM ONTOLOGY & CORE MANIFESTO
#-------------------------------------------------------------------------------
[SYSTEM_OVERVIEW]
TruestConnect is an anti-surveillance, local-first conversational context engine designed to solve modern human isolation. It functions as an un-compromised digital mirror of the user's social network. It runs entirely on client hardware, keeping zero databases, logs, or analytics in the cloud. It features zero subscriptions, zero advertisements, and zero centralized tracking vectors.

[CORE_DATA_PRINCIPLE]
The data processed by this system represents a mathematical duplicate of the user's social memory. Under no circumstances should raw transcript text or user identifiers be transmitted outside the device's physical RAM/storage boundary. 

[THE ALPHA OBJECTIVE]
A single-user "Ambient Whisper-Interview Engine" running on a personal mobile device via React Native/Expo. The application operates in the background during real-world interactions, streams audio into an isolated local memory ring, distills the semantic payload using an on-device Small Language Model (SLM), permanently purges the raw wiretap transcripts, and provides a local natural language interface to query past memories and commitments.

#-------------------------------------------------------------------------------
# SECTION 2: ARCHITECTURAL EVOLUTION (ALPHA TO V1 BETA)
#-------------------------------------------------------------------------------
Phase 0 (Current Alpha): 
  - User-driven manual ambient session initiation.
  - In-RAM transcription using a quantized local engine or zero-retention runtime.
  - Immediate local SLM extraction of entity structures.
  - Offline vector encoding using a lightweight embedding matrix.
  - Natural language querying via local Cosine Similarity index over an Expo-SQLite ledger.
  - Focus: 100% utility for a single user tracking peers who do not possess the system.

Phase 1 (Future V1 Beta): 
  - Agent-to-Agent (A2A) protocol handshakes over local Bluetooth/WiFi mesh.
  - Zero-Knowledge latent space consensus (comparing vector coordinates directly).
  - 30-Day Permission Decay ladders and cryptographic chaffing/noise injection.
  - Aggregate Local Differential Privacy (LDP) macro-trend telemetry extraction.

#-------------------------------------------------------------------------------
# SECTION 3: WEEKLY SPRINT EXECUTION ROADMAP (1-2 HOURS/WEEK BINDINGS)
#-------------------------------------------------------------------------------

[SPRINT_WEEK_1]: THE SHELL & DATA CONTAINER
- Objective: Initialize cross-platform environment and establish the immutable local storage layer.
- Tech Vector: Expo Core, Expo-SQLite, React Native Paper.
- Milestones: 
  1. Bootstrapped clean TypeScript Expo project with Native Prebuild compatibility.
  2. SQLCipher/Expo-SQLite schema initialized for `ambient_history` and `contacts`.
  3. Simple 2-button control panel: [Record Interaction] and [Query Memory Engine].

[SPRINT_WEEK_2]: THE AMBIENT AUDIO CAPTURE PIPELINE
- Objective: Capture real-world acoustic waves and write them to a structured local temporary directory.
- Tech Vector: expo-av, expo-file-system.
- Milestones:
  1. Implement persistent background audio recording permissions.
  2. Implement a rolling audio buffer or fixed-session WAV recorder outputting 16kHz mono audio.
  3. Visual UI indicator showing active acoustic tracking status.

[SPRINT_WEEK_3]: ON-DEVICE SPEECH-TO-TEXT INFRASTRUCTURE
- Objective: Transform binary audio into memory-resident strings without cloud APIs.
- Tech Vector: expo-whisper / whisper.cpp WebAssembly or native bindings.
- Milestones:
  1. Integrate a quantized Whisper-Base or Whisper-Tiny model (GGML format) directly into app bundle.
  2. Implement an automated processing hook that routes the Week 2 audio file straight into the local model.
  3. Output the raw text string to volatile RAM memory only.

[SPRINT_WEEK_4]: THE DISTILLATION ENGINE & TRANSCRIPT PURGE
- Objective: Compress chaotic human speech into high-order structures and execute the core privacy shield.
- Tech Vector: Local model bindings (react-native-executorch or ONNX runtime executing SmolLM2-360M / Qwen-1.5B-Chat).
- Milestones:
  1. Load a local sub-1B parameter LLM engine inside custom native dev builds.
  2. Direct the raw RAM transcript to the model with a rigid structural prompt.
  3. Extract highly compressed JSON artifacts (Names, places, specific topics, promises).
  4. Save the JSON string into SQLite and trigger a secure memory purge of the raw string.

[SPRINT_WEEK_5]: THE VECTOR MAP & COSINE SEARCH INTERACTION
- Objective: Build the semantic retrieval engine to interview your social matrix.
- Tech Vector: Basic TF-IDF / local array mapping or small WebAssembly embedding model (e.g., Xenova/all-MiniLM-L6-v2 via Voy).
- Milestones:
  1. Convert conversational artifacts into a localized numerical coordinate matrix.
  2. Create a chat box UI allowing natural language entries ("Who told me they were moving to Seattle?").
  3. Execute a local mathematical search across the SQLite database, yielding immediate contextual references.

#-------------------------------------------------------------------------------
# SECTION 4: PRODUCTION-GRADE CODE GENERATION PROMPTS
#-------------------------------------------------------------------------------

[PROMPT_ENGINEERING_BATCH_1]
[TARGET]: SPRINT_WEEK_1 (Execute this prompt first)
\"\"\"
Act as a Principal React Native Architect specializing in local-first, privacy-hardened application architectures. I need to build the foundational container for an offline app named TruestConnect using Expo with TypeScript.

Strict Architectural Requirements:
1. Setup a clean Expo structure using standard TypeScript templates. Ensure compatibility with custom native code (`npx expo prebuild`).
2. Implement a local storage architecture using `expo-sqlite`. Write a database initialization module named `DatabaseInitializer.ts` that safely spins up two tables if they do not exist:
   
   Table A: `contacts`
   - id: TEXT PRIMARY KEY (UUID)
   - name: TEXT NOT NULL
   - dynamic_tier: TEXT DEFAULT 'Ecosystem'
   - last_interaction_timestamp: INTEGER

   Table B: `interaction_summaries`
   - id: TEXT PRIMARY KEY (UUID)
   - contact_id: TEXT REFERENCES contacts(id)
   - timestamp: INTEGER
   - extracted_entities: TEXT (To hold stringified JSON maps containing places, keywords, promises)
   - high_order_vector: TEXT (To hold a stringified flat array of floating-point embeddings)

3. Provide a minimalist, stark user interface using standard React Native components. It must features a dashboard tracking total stored contacts, an interaction session action button [Record Interaction], and a global query engine input bar [Query Memory Engine].
4. Enforce strict type safety across all interfaces. Write clean, modular, documented code optimized for rapid execution inside my limited 1-2 hour development sprints.
\"\"\"

[PROMPT_ENGINEERING_BATCH_2]
[TARGET]: SPRINT_WEEK_2 (Execute after Week 1 settles)
\"\"\"
Act as a Mobile Audio Engineer. Integrate the audio processing layer into our existing React Native/Expo SQLite application container.

System Pipeline Targets:
1. Use `expo-av` and `expo-file-system` to build a background-resilient audio capture module named `AudioCaptureEngine.ts`.
2. Configure the hardware recorder settings precisely for low-resource local machine learning inputs:
   - Audio Sample Rate: 16000 Hz (16kHz)
   - Number of Channels: 1 (Mono)
   - Bit Rate: 16000 bps
   - Output Extension: .wav (PCM audio container format)
3. Build robust permission handling workflows. If microphone access is denied or revoked, explicitly change the UI component state to visually signal an error boundary.
4. Implement safe file caching strategies: save the binary data to a temporary workspace directory (`FileSystem.cacheDirectory`), ensuring it can be quickly loaded into RAM by our future transcription phase, and provide an interface to easily trigger file system purges.
\"\"\"

[PROMPT_ENGINEERING_BATCH_3]
[TARGET]: SPRINT_WEEK_3 & SPRINT_WEEK_4 (Execute for the intelligence engine)
\"\"\"
Act as an Embedded Device AI/ML Engineer. We need to implement the on-device transcription and extraction pipeline for our local React Native application without calling any external cloud APIs.

Operational Logic:
1. Interface with our existing `AudioCaptureEngine` to grab the 16kHz mono `.wav` cache file.
2. Utilize a local speech-to-text module (assuming a GGML-quantized tiny/base Whisper layer) to convert the binary recording into an in-memory plain text string inside a service named `LocalTranscriptionPipeline.ts`.
3. Immediately pass this raw text string into a native local Small Language Model execution layer (configured via ONNX runtime or optimized mobile ExecuTorch). Target the processing using a highly structured system prompt wrapper:
   
   \"System Prompt: You are a private human memory anchor. Below is a raw, messy transcript fragment of a real-world social conversation. Analyze the text and extract a strict JSON structure containing exactly three attributes:
   - 'detected_peer': (String identifying the primary person spoken to, or 'Unknown' if ambiguous)
   - 'core_topics': (An array of distinct proper nouns, locations, or topics mentioned, e.g., ['Seattle', 'care facility', 'logistics'])
   - 'promises_and_commitments': (An array of absolute statements or task dependencies made by the user, e.g., ['Check in next week regarding Seattle search progress'])
   
   Do not include any pleasantries, preamble, or markdown blocks outside the JSON format.\"

4. Save the resulting JSON payload into our `interaction_summaries` table inside SQLite.
5. EXTREMELY CRITICAL CRITERION: The moment the SQLite write operation confirms a success token, permanently erase the raw text transcript string from system RAM and overwrite the temporary audio file block from the file system. The raw conversation text must never be committed to disk.
\"\"\"

#-------------------------------------------------------------------------------
# SECTION 5: FAILSALFES & SYSTEM INTEGRITY DEBUG RULES
#-------------------------------------------------------------------------------
1. MEMORY OVERFLOW PREVENTION: Keep SLM context constraints capped at 2048 tokens during local inference cycles. If a transcript threatens context windows, slice it sequentially into 3-minute structural windows.
2. API REJECTION POLICIES: If local execution blocks on underpowered older chips during testing, allow a clean debug flag to temporarily fallback to an official, stateless, zero-retention API node (like Gemini or Claude with data sharing toggled OFF). Maintain the identical JSON structure so shifting back to native client execution requires zero codebase rewrites.
3. ABSOLUTE CRASH RULE: If a native dependency fails to bind, isolate the script into a web-assembly standard context rather than letting the host platform app layer collapse. Keep UI operations async relative to the local database write locks.
#===============================================================================\"\"\"

with open("truestconnect_alpha_war_plan.txt", "w") as f:
    f.write(war_plan_content)