from .maze import Maze
from .models.world_model import WorldModel
import threading
import time

def get_robo_builder(**kwargs):

    levels = kwargs.get("levels", {})
    robo_fn = kwargs.get("robo_fn", {})
    counter = 0

    def blank(world):
        pass

    def load_world(level, floating=False):
        nonlocal counter
        counter += 1
        return WorldModel(f"./worlds/{level}.json", levels.get(level, blank), {'ui_counter': counter, 'floating': floating})

    def bot_init(maze, level):
        bot = maze.bot()
        bot.set_trace('red')
        fn = robo_fn.get(level, blank)
        fn(bot)

    def generate_maze(level, floating=False, zoom=None):
        world = load_world(level, floating=floating)
        maze = Maze(world, floating=floating, zoom=zoom)
        bot_init(maze, level)
        return maze

    def get_bot(level, floating=False, zoom=None):
        maze = generate_maze(level, floating=floating, zoom=zoom)
        bot = maze.bot()
        return bot
    

    def wait_and_check(widget, sleep=0.05):
        while not widget.is_inited:
            time.sleep(sleep)
        if widget.is_inited:
            widget.js_call("flush_js_q", [])


    def wait_for_bot(level, floating=False, zoom=None):
        bot = get_bot(level, floating, zoom)
        maze = bot.world
        thread = threading.Thread(target=wait_and_check, args=(maze, 0.05,))
        thread.start()
        return bot

    return wait_for_bot
