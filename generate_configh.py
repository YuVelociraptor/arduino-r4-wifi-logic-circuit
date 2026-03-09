from dotenv import dotenv_values

env = dotenv_values(".env")

with open("config.h", "w") as f:
    for k,v in env.items():
        f.write(f'#define {k} "{v}"\n')