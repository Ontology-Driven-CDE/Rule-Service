from urllib.request import Request
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
router = APIRouter()
import json
import os
from pathlib import Path

AllShapes = Path('Public/Shapes/fsosh.ttl').read_text()
HydraulicShapes = Path('Public/Shapes/HydraulicShapes.ttl').read_text()


@router.get("/")
async def root():
    return {"Message": "Frontpage"}

@router.get("/allShapes")
async def calculate_pipes(request: Request):
    return AllShapes

@router.get("/hydraulicShapes")
async def calculate_pipes(request: Request):
    return HydraulicShapes