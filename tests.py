from BasicORM.model import BaseModel, FilterConditional


class Usuario(BaseModel):
    id: str
    email: str


if __name__ == "__main__":
    cond = [
        FilterConditional(field="email", conditional="==", value="giovanilzanini@hotmail.com")
    ]
    x = Usuario().filter(cond)
    for y in x:
        print(y)
    # x = Usuario(email="giovanilzanini@hotmail.com", id="Giovani").create()
    # print(x)