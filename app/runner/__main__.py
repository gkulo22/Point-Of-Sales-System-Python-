from apexdevkit.server import UvicornServer

from app.runner.setup import setup

if __name__ == '__main__':
    UvicornServer.from_env().run(setup())

// or run this command in terminal: uvicorn app.runner.asgi:app --reload
