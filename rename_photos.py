import os
from datetime import datetime

# MOC-G3C Automated Photo Archiving
def rename_project_photos():
    # 1. Configuration
    project_name = input("Enter Project Name (e.g., SJ-36): ").strip()
    component_type = input("Enter Component Type (e.g., Sabliere, Ferme): ").strip()
    
    # Get current directory
    folder_path = os.getcwd()
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    count = 1
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            # Construct new name: YYYY-MM-DD_PROJECT-NAME_COMPONENT_TYPE_01.jpg
            extension = os.path.splitext(filename)[1]
            new_name = f"{date_str}_{project_name}_{component_type}_{count:02d}{extension}"
            
            os.rename(filename, new_name)
            print(f"Renamed: {filename} -> {new_name}")
            count += 1

    print(f"\n[SUCCESS] {count-1} photos archived under Protocol Lambda standards.")

if __name__ == "__main__":
    rename_project_photos()
