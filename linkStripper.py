
def linkStripper(file_path: str) -> str:
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    links: list[str] = []
    
    for line in lines:
        if "https://www.youtube.com/watch?v=" in line:
            video_id = line.split("https://www.youtube.com/watch?v=")[1][:11]
            links.append(video_id)
        elif "https://www.youtube.com/shorts/" in line:
            video_id = line.split("https://www.youtube.com/shorts/")[1][:11]
            links.append(video_id)
        elif "https://youtu.be/" in line:
            video_id = line.split("https://youtu.be/")[1][:11]
            links.append(video_id)

    links_text = "\n".join(links).strip()
    return links_text

file_path = "Links.txt"  # Use relative path now that the working directory is set
links_text = linkStripper(file_path)

print(links_text)

output_file_path = "LinkBlock.txt"
with open(output_file_path, "w") as output_file:
    output_file.write(links_text)