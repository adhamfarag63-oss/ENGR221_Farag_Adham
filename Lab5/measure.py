import sys
import types


class FakeTurtle:
    def __getattr__(self, name):
        return lambda *args, **kwargs: None


fake = types.ModuleType("turtle")
fake.Turtle = FakeTurtle
fake.clearscreen = lambda: None
sys.modules["turtle"] = fake

from snowflake import KochSnowflake

if __name__ == "__main__":
    KochSnowflake(500, 7).compare_snowflake()
