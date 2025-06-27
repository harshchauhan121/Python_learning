# Modifying Global Scope

enemies = 1


def increase_enemies():
    enemies += 1



increase_enemies()
print(f"enemies outside function: {enemies}")


