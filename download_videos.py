import os
import json

with open("dump.txt", "r") as urlfile:
    for line in urlfile:
        print(line)

        linedata = json.loads(line)

        url = linedata["url"]
        title = linedata["video"]

        command = f'ffmpeg -i "{url}" -c copy -bsf:a aac_adtstoasc "{title}.mp4"'

        res = os.system(command)

        print("Returned Value: ", res)