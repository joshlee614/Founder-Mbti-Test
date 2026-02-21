import os
import shutil
import glob

source_dir = "/Users/isang-won/.gemini/antigravity/brain/cafcea65-81f6-4719-b671-8eb162621a9e/"
dest_dir = "/Users/isang-won/Desktop/project/antigravity project/HVC 창업가 MBTI 유형 테스트/assets/images/"

keys = ["fdtb", "fdts", "fdmb", "fdms", "fitb", "fits", "fimb", "fims", 
        "pdtb", "pdts", "pdmb", "pdms", "pitb", "pits", "pimb", "pims"]

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for key in keys:
    pattern = os.path.join(source_dir, f"hylion_{key}_*.png")
    files = glob.glob(pattern)
    if not files:
        print(f"Warning: No file found for {key}")
        continue
    
    source_file = sorted(files)[-1]
    dest_file = os.path.join(dest_dir, f"hylion_{key}.png")
    shutil.copy(source_file, dest_file)
    print(f"Copied {source_file} -> {dest_file}")

print("Done")
