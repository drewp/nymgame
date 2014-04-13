Polymer 'word-picker',
  attached: () ->
    @word = @attributes.word.value
  wordChanged: ->
    @choices = syns[@word]
    @pick = ""
    @pickChanged()
  pickChanged: (o, n) ->
    drives = @attributes.drives.value
    if drives and drives != ""
      other = document.getElementById(drives)
      if other?
        other.word = @pick
  clickItem: (ev) ->
    @pick = ev.toElement.attributes.choice.value
