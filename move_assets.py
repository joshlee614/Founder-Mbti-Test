
import os
import shutil
import glob

source_dir = "/Users/isang-won/.gemini/antigravity/brain/e0a97d7d-ff61-42be-8a1c-4e8b7aea086d/"
dest_dir = "/Users/isang-won/Desktop/project/antigravity project/HVC 창업가 MBTI 유형 테스트/assets/images/"

mapping = {
    "banana_fdtb": "banana_fdtb.png",
    "banana_fdts": "banana_fdts.png",
    "banana_fdmb": "banana_fdmb.png",
    "banana_fdms": "banana_fdms.png",
    "banana_fitb": "banana_fitb.png",
    "banana_fits": "banana_fits.png",
    "banana_fimb": "banana_fimb.png",
    "banana_fims": "banana_fims.png",
    "banana_pdtb": "banana_pdtb.png",
    "banana_pdts": "banana_pdts.png",
    "banana_pdmb": "banana_pdmb.png",
    "banana_pdms": "banana_pdms.png",
    "banana_pitb": "banana_pitb.png",
    "banana_pits": "banana_pits.png",
    "banana_pimb": "banana_pimb.png",
    "banana_pims": "banana_pims.png"
}

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

print(f"Moving files from {source_dir} to {dest_dir}")

for key, target_name in mapping.items():
    # Find file matching the key in source
    pattern = os.path.join(source_dir, f"{key}_*.png")
    files = glob.glob(pattern)
    
    if not files:
        print(f"Warning: No file found for {key}")
        continue
        
    # Take the latest file if multiple (should be one usually)
    source_file = sorted(files)[-1]
    dest_file = os.path.join(dest_dir, target_name)
    
    try:
        shutil.move(source_file, dest_file)
        print(f"Moved {source_file} -> {dest_file}")
    except Exception as e:
        print(f"Error moving {key}: {e}")

print("Done")
