from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.auth import get_usuario_opcional

from app.controllers import auth_controller
from app.controllers import admin_controller


app = FastAPI(title="Sistema de estoque")

#Configurar o Fastapi para servir os arquivos estaticos (CSS, JS, Imaens)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

#inclui os routers dos controles
app.include_router(auth_controller.router)
app.include_router(admin_controller.router)


#Tela inicial
@app.get("/")
def home(
    request: Request,
    usuario = Depends(get_usuario_opcional)
    ):
    
    # nao logado - exibir pagina publica
    if usuario is None:
        return templates.TemplateResponse(
            request,
            "index.html",
            {"request": request}
        )
    
    #logado - exibir a tela principal com os dados do usuario
    return templates.TemplateResponse(
        request,
            "home.html",
            {"request": request, "usuario": usuario}
        )