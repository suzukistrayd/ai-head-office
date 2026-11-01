import os

# 1. Define folder hierarchy
folders = [
    "dashboard",
    "publishing team",
    "characters",
    "knowledge",
    "manuscript_raw",
    "manuscript",
    "scripts"
]

# 2. Define empty files with title headers
files = {
    # Publishing Team Bios & Directives
    "publishing team/martin-strayd.md": "# PUBLISHING TEAM // MARTIN STRAYD\n\n## Persona & Voice\n\n## Directive & Role\n",
    "publishing team/suzuki.md": "# PUBLISHING TEAM // SUZUKI (EDITOR & PUBLISHER)\n\n## Pacing & Structure Directives\n\n## Amazon KDP Quality Control\n",
    "publishing team/veg-anna.md": "# PUBLISHING TEAM // VEG-ANNA (BOOK VALUE EDITOR)\n\n## Atmospheric Lore & Aesthetics\n\n## Emotional Resonance & Continuity\n",
    
    # In-Book Novel Characters
    "characters/male-american.md": "# BOOK CHARACTER // MALE AMERICAN\n\n## Archetype & Backstory\n\n## Dialogue Style & Motivations\n",
    "characters/female-american.md": "# BOOK CHARACTER // FEMALE AMERICAN\n\n## Archetype & Backstory\n\n## Dialogue Style & Motivations\n",
    "characters/mexican.md": "# BOOK CHARACTER // MEXICAN\n\n## Archetype & Cultural Perspective\n\n## Dialogue Style & Motivations\n",
    
    # Knowledge RAG Index Placeholder
    "knowledge/manuscript-index.json": "[\n  {\n    \"id\": \"placeholder\",\n    \"source\": \"vault-notes.md\",\n    \"content\": \"Initial 90s vault index placeholder.\"\n  }\n]",
    
    # Raw Notes & Vault Intakes
    "manuscript_raw/vault-notes-90s.md": "# RAW VAULT NOTES // 1990s TIMELINE\n\n## Backstage & Concert Memories\n\n## Atmosphere & Era Specifics (No Screens)\n",
    "manuscript_raw/song-lyrics-vault.md": "# VAULT SONG LYRICS // MARTIN STRAYD\n\n## Chapter Header Lyrics\n\n## In-Scene Acoustic Passages\n",
    
    # Output Draft Placeholder
    "manuscript/novel-volume-1.md": "# SECRET SERVICE: BACKSTAGE WITH MARTIN STRAYD\n## Volume 1\n\n"
}

def create_structure():
    print("=" * 60)
    print("STRAYD HQ // INITIALIZING REPOSITORY STRUCTURE")
    print("=" * 60)

    # Create directories
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"[DIRECTORY CREATED] -> {folder}/")

    # Create empty title files
    for filepath, content in files.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[FILE CREATED]      -> {filepath}")

    print("=" * 60)
    print("SUCCESS: Structure and titled files are in place!")
    print("=" * 60)

if __name__ == "__main__":
    create_structure()
