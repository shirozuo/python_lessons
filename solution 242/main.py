import os.path

answer = set()

for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            answer.add(current_dir.replace(".\\", ""))

print("\n".join(sorted(answer)))
