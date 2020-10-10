"""This code comes from: https://gist.github.com/bakineugene/76c8f9bcec5b390e45df
and https://gist.github.com/novel-yet-trivial/3eddfce704db3082e38c84664fc1fdf8"""
import tkinter as tk
from ...configure import EXTRA_SPACE_AFTER_SCROLL
from .frame import FrameTemplate

# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame


class ScrolledFrameTemplate(FrameTemplate):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """

    def __init__(self, parent, *args, **kw):
        super().__init__(parent, *args, **kw)
        # create a canvas object and a vertical scrollbar for scrolling it
        canvas_container = tk.Frame(self)
        canvas_container.pack(fill="both", expand=1, side="top")

        vscrollbar = tk.Scrollbar(canvas_container, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(canvas_container,
                           bd=0,
                           highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        canvas.bind("<Enter>", self._bind_mouse)
        canvas.bind("<Leave>", self._unbind_mouse)

        self.canvas = canvas

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        self.interior_id = interior_id =\
            canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            if not interior:
                return
            # update the scrollbars to match the size of the inner frame
            if canvas.winfo_height() < interior.winfo_reqheight():
                height = interior.winfo_reqheight() + EXTRA_SPACE_AFTER_SCROLL
            else:
                height = 0
            size = (interior.winfo_reqwidth(), height)
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
