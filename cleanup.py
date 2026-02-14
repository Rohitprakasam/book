
import os
import shutil
from pathlib import Path

# Paths
OUTPUT_DIR = Path("data/output")
INTERMEDIATE_DIR = OUTPUT_DIR / "intermediates"

# Files to DELETE (Debug/Temporary)
FILES_TO_DELETE = [
    "debug.tex",
    "error_log.txt",
    "BookForge_Preview.html",  # Replaced by Final
    "suhbook.cls", # Duplicate in root
    "_analyze.py",
    "generate_book_now.py",
    "regenerate_final.py"
]

# Files to MOVE (Intermediate steps, keep for reference)
FILES_TO_MOVE = [
    "tagged_manuscript.txt",
    "expanded_draft.md",
    "resolved_manuscript.md",
    "ready_for_press.md"
]

def cleanup():
    """
    Clean up the output directory by:
    1. Deleting debug/temp files.
    2. Moving intermediate files to a subfolder.
    """
    if not OUTPUT_DIR.exists():
        print(f"❌ Output directory not found: {OUTPUT_DIR}")
        return

    # Create intermediate folder
    INTERMEDIATE_DIR.mkdir(exist_ok=True)

    print(f"🧹 Cleaning up {OUTPUT_DIR}...")

    # 1. DELETE
    for filename in FILES_TO_DELETE:
        file_path = OUTPUT_DIR / filename
        if file_path.exists():
            try:
                os.remove(file_path)
                print(f"   🗑️ Deleted: {filename}")
            except Exception as e:
                print(f"   ❌ Failed to delete {filename}: {e}")

    # 2. MOVE -> DELETE (Aggressive Cleanup for GitHub)
    if INTERMEDIATE_DIR.exists():
        try:
            shutil.rmtree(INTERMEDIATE_DIR)
            print(f"   🗑️ Deleted folder: {INTERMEDIATE_DIR}")
        except Exception as e:
            print(f"   ❌ Failed to delete {INTERMEDIATE_DIR}: {e}")

    # Root Level Cleanup
    for filename in FILES_TO_DELETE:
        # Check root
        root_file = Path(filename)
        if root_file.exists():
             try:
                os.remove(root_file)
                print(f"   🗑️ Deleted: {filename}")
             except Exception as e:
                 print(f"   ❌ Failed to delete {filename}: {e}")

    print("\n✅ Aggressive Cleanup Complete!")
    print("   Ready for git push.")

if __name__ == "__main__":
    cleanup()
