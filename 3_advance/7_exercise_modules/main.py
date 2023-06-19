from canvas import root
from authentication import render_entry

# prevent us from circular imports
if __name__ == '__main__':
    render_entry()
    root.mainloop()
