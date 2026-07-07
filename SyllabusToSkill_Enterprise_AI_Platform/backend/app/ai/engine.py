def create_plan(goal,skills,syllabus):
    library={
    "data scientist":["Python","Statistics","Machine Learning","SQL"],
    "software engineer":["DSA","System Design","Cloud"],
    "ai engineer":["Python","LLM","Deep Learning","MLOps"]
    }
    target=library.get(goal.lower(),["Programming","Projects"])
    gaps=[x for x in target if x.lower() not in [s.lower() for s in skills]]
    return {"goal":goal,"skill_gaps":gaps,"roadmap":[{"month":i+1,"skill":x} for i,x in enumerate(gaps)]}
