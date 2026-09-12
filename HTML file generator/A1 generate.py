def get_specific_line(file_path: str, line_number: int) -> str | None:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    if line_number < len(lines):
        return lines[line_number].strip()
    else:
        return None

weekCur = "06WEEK2026"
file_path = "linkBlock.txt"
line_number = 0
line_number2 = 1
line_number3 = 2 
line_number4 = 0
video_id = get_specific_line(file_path, line_number)
video_id2 = get_specific_line(file_path, line_number2)
video_id3 = get_specific_line(file_path, line_number3)
video_id4 = get_specific_line(file_path, line_number4)

if video_id:
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Videos</title>
<link rel="stylesheet" href="../Atticus.css">
</head>
<body>
<h1>Monday</h1>
<br>
  <h2 align=center fontcolor=Blue>Hello Atticus, if you have questions about the video, please ask your teacher!</h2>
<br> 
	<div>Science
    	<br>
    	<iframe width="840" height="473" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
		</div>
          <p><a href="https://www.youtube.com/watch?v={video_id}"> Direct link to video </a></p><br>
	<div>PE
		<br>
		<iframe width="840" height="473" src="https://www.youtube.com/embed/{video_id2}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
		</div>
          <p><a href="https://www.youtube.com/watch?v={video_id2}"> Direct link to video </a></p><br>
    <div>ASL
    	<br>
    	<iframe width="840" height="473" src="https://www.youtube.com/embed/{video_id3}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
		</div>
          <p><a href="https://www.youtube.com/watch?v={video_id3}"> Direct link to video </a></p><br>
	       
	<section><a style="font-weight:bold" href="../index.html" target="_self" title="Click Here!" font-weight=bold>Back to Home!</a></section>

</body>
</html>
    """
    # write a loop to find the current week to write to, to reduce manual labor
    with open(f"{weekCur}/AT-D1.html", 'w') as html_file:
        html_file.write(html_content)
else:
    print("Invalid line number.")