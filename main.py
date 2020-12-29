from IslandPy.RenderWindow import RenderWindow
from IslandPy.Scenes.TestScene import TestScene


class CustomScene(TestScene):
    def __init__(self, name: str) -> None:
        super().__init__(name)


def main() -> None:
    s1 = TestScene("t1")
    scenes = [s1]
    r = RenderWindow(scenes)
    r.start("t1")


if __name__ == '__main__':
    main()
