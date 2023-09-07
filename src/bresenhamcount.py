def bresenham(x0, y0, x1, y1):  
    dx = abs(x1 - x0)  
    dy = abs(y1 - y0)  
  
    sx = -1 if x0 > x1 else 1  
    sy = -1 if y0 > y1 else 1  
  
    if dx > dy:  
        err = dx / 2.0  
        while x0 != x1:  
            yield x0, y0  
            err -= dy  
            if err < 0:  
                y0 += sy  
                err += dx  
            x0 += sx  
    else:  
        err = dy / 2.0  
        while y0 != y1:  
            yield x0, y0  
            err -= dx  
            if err < 0:  
                x0 += sx  
                err += dy  
            y0 += sy  
    yield x0, y0
