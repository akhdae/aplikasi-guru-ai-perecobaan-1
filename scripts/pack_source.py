import os
import zipfile

def pack_project():
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    public_dir = os.path.join(workspace_root, "public")
    os.makedirs(public_dir, exist_ok=True)
    zip_path = os.path.join(public_dir, "pkbm-darul-hikam-source.zip")
    
    ignored_dirs = {
        "node_modules",
        "dist",
        ".git",
        ".aistudio",
        "__pycache__"
    }
    
    ignored_files = {
        ".env",
        "pkbm-darul-hikam-source.zip",
        ".DS_Store"
    }

    print(f"Creating zip archive at: {zip_path}")
    
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(workspace_root):
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if d not in ignored_dirs and not d.startswith(".aistudio")]
            
            for file in files:
                if file in ignored_files or file.endswith(".zip") or file.endswith(".pyc"):
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, workspace_root)
                # Store under root folder in zip for neat extraction
                archive_name = os.path.join("pkbm-darul-hikam", rel_path)
                zipf.write(full_path, archive_name)
                
    file_size_kb = os.path.getsize(zip_path) / 1024
    print(f"Successfully created zip archive ({file_size_kb:.2f} KB) at {zip_path}")

if __name__ == "__main__":
    pack_project()
