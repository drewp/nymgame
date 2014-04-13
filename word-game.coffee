Polymer 'word-game',
  attached: () ->
    true
  stepsChanged: () ->
    console.log("now steps", @steps)
    @stepRows = []
    for i in [0...parseInt(@steps)]
      @stepRows.push({
        id: "p"+i,
        drives: if i < parseInt(@steps) then "p"+(i+1) else "",
        word: if i == 0 then @first else ""
        })
      