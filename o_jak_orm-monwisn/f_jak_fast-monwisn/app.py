from fastapi import FastAPI, Depends, Response, status, Header, Query
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse, RedirectResponse

app = FastAPI()
security = HTTPBasic()
app.paths = []


# task 3.1


@app.get("/start", response_class=HTMLResponse)
def root():
    html_content = "<h1>The unix epoch started at 1970-01-01</h1>"
    
    return HTMLResponse(content=html_content, status_code=200)


# task 3.2


# task 3.3

@app.get('/info')
def info(format: str = Query(None), user_agent: str | None = Header(default=None)):
    
    if format == 'json':
        json_content = {"user_agent": user_agent}
        return JSONResponse(content=json_content)

    elif format == 'html':
        html_content = f'<input type="text" id=user-agent name=agent value="{user_agent}">'
        return HTMLResponse(content=html_content)

    else:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

  
# task 3.4

@app.put('/save/{string}')
def put(string: str):

    if string not in app.paths:
        app.paths.append(string)

        return Response(status_code=status.HTTP_200_OK)

    return app.paths


@app.get('/save/{string}')
def get(string: str):

    if string not in app.paths:
        app.paths.append(string)

        return Response(status_code=status.HTTP_404_NOT_FOUND)

    else:
        url = app.url_path_for('info')
        headers = {"Location": "/info"}

        return RedirectResponse(url=url, headers=headers, status_code=status.HTTP_301_MOVED_PERMANENTLY)


@app.delete('/save/{string}')
def delete(string: str, response: Response):

    app.paths.remove(string)

    return response.status_code
