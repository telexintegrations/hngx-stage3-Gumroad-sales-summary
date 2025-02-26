from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.models.payloadModels import TickRequest
from app.services.gumroadServices import getGumroadData
from app.utils.integrationJsonServices import integrationJSON

router = APIRouter()

@router.post("/tick")
@router.post("/tick/")
async def tickEndpoint(payload: TickRequest, background_tasks: BackgroundTasks):
    returnURL = payload.return_url

    gumroadAPIKey = None

    for setting in payload.settings:
        if setting.label == "gumroad_api_key":
            gumroadAPIKey = setting.default
            break

    if not returnURL:
        raise HTTPException(status_code=400, detail="Missing return_url")
    
    if not gumroadAPIKey:
        raise HTTPException(status_code=400, detail="Gumroad API key not found")
    
    background_tasks.add_task(getGumroadData, gumroadAPIKey, returnURL)

    return {"status": "Processing request"}

@router.get("/integration-json")
def getIntegrationJSON():
    return integrationJSON()