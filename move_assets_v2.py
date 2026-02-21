
import os
import shutil
import glob

source_dir = "/Users/isang-won/.gemini/antigravity/brain/e0a97d7d-ff61-42be-8a1c-4e8b7aea086d/"
dest_dir = "/Users/isang-won/Desktop/project/antigravity project/HVC 창업가 MBTI 유형 테스트/assets/images/"

# Only the 14 files that need moving (fdmb and fdms are already there)
keys = [
    "fdtb", "fdts", 
    "fitb", "fits", "fimb", "fims", 
    "pdtb", "pdts", "pdmb", "pdms", 
    "pitb", "pits", "pimb", "pims"
]

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

print(f"Copying files from {source_dir} to {dest_dir}")

for key in keys:
    # Find latest file matching the key pattern
    pattern = os.path.join(source_dir, f"banana_{key}_*.png")
    files = glob.glob(pattern)
    
    if not files:
        print(f"Warning: No file found for {key}")
        continue
        
    # Take the latest file
    source_file = sorted(files)[-1]
    # Use _v2 suffix to avoid lock issues
    dest_file = os.path.join(dest_dir, f"banana_{key}_v2.png")
    
    try:
        shutil.copy2(source_file, dest_file)
        print(f"Copied {os.path.basename(source_file)} -> banana_{key}_v2.png")
    except Exception as e:
        print(f"Error copying {key}: {e}")

print("Done")
