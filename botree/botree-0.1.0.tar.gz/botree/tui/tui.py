from textual.app import App
from textual.widgets import Placeholder
from textual.widget import Widget
from textual.reactive import Reactive
from rich.panel import Panel

class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel(f"{self.text} [b]World[/b]", style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

class SimpleApp(App):

    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(Placeholder(), edge="top", size=20)
        await self.view.dock(Hover(text="salve"), edge="top")


SimpleApp.run(log="textual.log")