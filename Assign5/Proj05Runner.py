def run(origin,segment):
   if segment in origin:
       pos = origin.index(segment) - 3
       if pos<0:
           pos = 0
       pos2 = origin.index(segment) + len(segment)+3
       if pos2 > len(origin):
           pos2 = len(origin)
       
       change = origin[pos: pos2]
       return "Daniel Mendoza" + "\n" + origin + "\n" + segment + "\n" + change
   else:
       return "Error"
