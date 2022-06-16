from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse

app = APIRouter()
html = """
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>Authorization</title>
</head>
<body>
<h1>About Developer</h1>
<a href="https://python.org">Python</a>
<p> My name is Abdusamad Abdullakhanov, I am 17 years old and young python web developer. I am really glad to being able<br>
    to create a web app like thisAlso, if you wanna contact with me here is my email pythondeveloper441@gmail.com you<br>
    can actually contact with me maybe we can collaborate. If you take a look at my life and sister Sh that sucks!!!<br>
    She doesn't think about me but I used to do, so i did mistake with thinking about her, now I really hate sister Sh<br>
    
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJVIjSzhrooE17HTNjhtaShibZK5uAh9-0Nw&usqp=CAU"> 
</p>
<p>Was it useful?</p>
<h1>
    <button>Yes</button>
    <button>No</button>
</h1>

</body>
</html>
"""


@app.get("/about-us")
async def get_info():
    return HTMLResponse(content=html, status_code=status.HTTP_200_OK)


if __name__ == '__main__':
    print(__package__)
