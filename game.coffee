words = Object.keys(syns)

findPath = (steps) ->

  path = []
  while path.length != steps + 1
    path = [words[_.random(words.length - 1)]]
    for lp in [0...4]
      s = syns[path[path.length - 1]]
      if not s.length
        break
      next = s[_.random(s.length - 1)]
      if next in path
        break
      path.push(next)
  path
  

window.addEventListener 'polymer-ready', (ev) ->

  path = findPath(4)
  game = document.querySelector('word-game')
  game.first = path[0]
  game.last = path[path.length - 1]
  game.steps = path.length - 1
