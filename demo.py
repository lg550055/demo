from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
  return 'Welcome, my friend!!'

@app.get('/{name}')
def hello(name):
  return f'Welcome, {name}!!'