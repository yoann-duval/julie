import html
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from src.adapters.persistence.in_memory_magic_link_repository import InMemoryMagicLinkRepository
from src.use_cases.generate_magic_link import GenerateMagicLink
from src.use_cases.consume_magic_link import ConsumeMagicLink
from src.core.exceptions import MagicLinkNotFound, MagicLinkAlreadyUsed

router = APIRouter()

# Simple singleton for in-memory storage persistence across requests
_repository = InMemoryMagicLinkRepository()

def get_repository():
    return _repository

class GenerateLinkRequest(BaseModel):
    first_name: str

@router.post("/generate-magic-link")
async def generate_magic_link(
    request: GenerateLinkRequest,
    repo: InMemoryMagicLinkRepository = Depends(get_repository)
):
    use_case = GenerateMagicLink(repo)
    token = use_case.execute(request.first_name)
    # In a real app, this would send an email.
    # Here we return the link for the user to click.
    return {"magic_link_url": f"/welcome?token={token}", "token": token}

@router.get("/welcome", response_class=HTMLResponse)
async def welcome(
    token: str = Query(...),
    repo: InMemoryMagicLinkRepository = Depends(get_repository)
):
    use_case = ConsumeMagicLink(repo)
    try:
        first_name = use_case.execute(token)
        safe_name = html.escape(first_name)
        return f"""
        <html>
            <head>
                <title>Bienvenue</title>
            </head>
            <body>
                <h1>Bonjour {safe_name}</h1>
            </body>
        </html>
        """
    except MagicLinkNotFound:
        raise HTTPException(status_code=404, detail="Lien invalide")
    except MagicLinkAlreadyUsed:
        raise HTTPException(status_code=400, detail="Ce lien a déjà été utilisé")
