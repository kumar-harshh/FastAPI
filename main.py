from fastapi import FastAPI, Path

app=FastAPI()

@app.get("/")
def getapi():
    return {"Message":"Hello World"}


student={
    1:{
        "name":"leo",
        "class":"5th",
        "age":12
    },
    2:{
        "name":"libra",
        "class":"8th",
        "age":15    
    }
}

@app.get("/student/{id}")
def getstudent(id:int=Path(description="Enter the student ID", lt=3, gt=0)):
    return student[id]