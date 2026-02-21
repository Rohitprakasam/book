"""
Clear BookForge build artifacts and output to free space or start fresh.
Aligns with main.py / src layout: data/output and pipeline state.
"""

import shutil
from pathlib import Path


def clear_directory(directory_path: Path) -> None:
    """Removes all files and subdirectories in a directory, but keeps the directory itself."""
    if not directory_path.exists():
        print(f"Skipping {directory_path}: Directory does not exist.")
        return
    print(f"Cleaning {directory_path}...")
    for item in directory_path.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                item.unlink()
                print(f"  Deleted file: {item.name}")
            elif item.is_dir():
                shutil.rmtree(item)
                print(f"  Deleted directory: {item.name}")
        except Exception as e:
            print(f"  Failed to delete {item.name}: {e}")


def remove_file(file_path: Path) -> None:
    """Removes a specific file if it exists."""
    if not file_path.exists():
        print(f"Skipping {file_path}: File does not exist.")
        return
    try:
        file_path.unlink()
        print(f"Deleted file: {file_path}")
    except Exception as e:
        print(f"Failed to delete {file_path}: {e}")


def main() -> None:
    base_dir = Path(__file__).resolve().parent

    # Primary output dir (tagged manuscript, expanded draft, resolved manuscript, assets, JSON, .tex, .pdf)
    output_dir = base_dir / "data" / "output"
    
    # Vector DB Directory (must be cleared to prevent cross-contamination between books)
    chroma_dir = base_dir / "data" / "chroma_db"

    # Optional: standalone extracted_images dir if it was ever used at project root
    images_dir = base_dir / "extracted_images"

    print("Starting cleanup...")
    clear_directory(output_dir)
    clear_directory(chroma_dir)
    if images_dir.exists():
        clear_directory(images_dir)
    print("Cleanup complete.")


if __name__ == "__main__":
    main()
