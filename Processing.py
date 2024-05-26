def setup():
  size(800, 600)
  background(0)

def draw():
  colors = [color(255, 0, 0), color(0, 255, 0), color(0, 0, 255), color(255, 255, 0), color(0, 255, 255), color(255, 0, 255)]
  fill(random.choice(colors))
  noStroke()
  shape = int(random(2))
  if shape == 0:
      ellipse(random(width), random(height), random(10, 100), random(10, 100))
  else:
      rect(random(width), random(height), random(50, 200), random(50, 200))