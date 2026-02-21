
import os
import shutil
import glob
import time

source_dir = "/Users/isang-won/.gemini/antigravity/brain/e0a97d7d-ff61-42be-8a1c-4e8b7aea086d/"
dest_dir = "/Users/isang-won/Desktop/project/antigravity project/HVC 창업가 MBTI 유형 테스트/assets/avatars/"

keys = [
    "fdtb", "fdts", "fdmb", "fdms",
    "fitb", "fits", "fimb", "fims",
    "pdtb", "pdts", "pdmb", "pdms", 
    "pitb", "pits", "pimb", "pims"
]

print(f"Starting safe copy to {dest_dir}...")

for key in keys:
    # Find all files matching the key
    pattern = os.path.join(source_dir, f"banana_{key}_*.png")
    files = glob.glob(pattern)
    
    if not files:
        print(f"!! CRITICAL: No file found for {key}")
        continue
        
    # Sort by modification time to get the absolute latest
    latest_file = max(files, key=os.path.getmtime)
    dest_file = os.path.join(dest_dir, f"banana_{key}.png")
    
    print(f"Copying {os.path.basename(latest_file)} -> banana_{key}.png")
    
    try:
        shutil.copyfile(latest_file, dest_file)
    except Exception as e:
        print(f"!! Error on {key}: {e}")

print("Safe copy completed.")
