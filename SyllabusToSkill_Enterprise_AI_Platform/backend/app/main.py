from fastapi import FastAPI
from pydantic import BaseModel
from ai.engine import create_plan
from ai.resume_parser import extract_skills

app=FastAPI(title="SyllabusToSkill Enterprise")

class Profile(BaseModel):
    career_goal:str
    skills:list[str]
    syllabus:str

@app.get("/")
def home():
    return {"status":"running"}

@app.post("/roadmap")
def roadmap(p:Profile):
    return create_plan(p.career_goal,p.skills,p.syllabus)

@app.post("/resume")
def resume(text:str):
    return {"skills":extract_skills(text)}
