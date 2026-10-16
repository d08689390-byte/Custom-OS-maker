class DraggableIcon:

    def __init__(
        self,
        canvas,
        item_id
    ):

        self.canvas = canvas

        self.item_id = item_id

        canvas.tag_bind(
            item_id,
            "<ButtonPress-1>",
            self.start
        )

        canvas.tag_bind(
            item_id,
            "<B1-Motion>",
            self.drag
        )

    def start(self, event):

        self.x = event.x
        self.y = event.y

    def drag(self, event):

        dx = event.x - self.x
        dy = event.y - self.y

        self.canvas.move(
            self.item_id,
            dx,
            dy
        )

        self.x = event.x
        self.y = event.y