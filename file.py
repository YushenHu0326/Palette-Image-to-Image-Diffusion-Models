import os
cnt = 0
for filename in os.listdir("."):
    if filename.endswith(".png"):
        os.rename(filename, str(cnt)+".png")
        cnt += 1
