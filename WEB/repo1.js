const fs = require('fs')

//-- Read html file
var REPO = fs.readFileSync('repo1.html', 'utf-8')

//-- Name of the Json file to read
const JSON_FILE = fs.readFileSync("/home/ana/Documentos/TFG/TFG/DATA_JSON/ptavi-final.json")

//-- Create the store structure from the contents of the file
//-- Return us the json structure
var data = JSON.parse(JSON_FILE);

//-- Variable total
let total = ''

//-- Get information
//-- Get Repository name
repository = Object.keys(data)
total += "<h2> REPOSITORY: " + repository + "</h2>"
//-- Get Files names
files = Object.keys(data[repository])

for (file=0; file<files.length; file++){
  //-- Get name
  name_file = files[file]
  total += '<h3>NAME FILE : ' + name_file + '<h3>'
  let content = data[repository][name_file]
  //-- Get levels
  let levels = content["Levels"]
  total += '<h4>LEVELS: <h4>'
  for (i=0; i<Object.keys(levels).length; i++){
    keys = Object.keys(levels)
    values = Object.values(levels)
    total += ('<p>Nivel ' + keys[i] + ': ' + values[i] + '</p>')
  }
  //-- Get classes
  let clase = content["Class"]
  total += '<h4>CLASSES: <h4>'
  for (i=0; i<Object.keys(clase).length; i++){
    keys = Object.keys(clase)
    values = Object.values(clase)
    total += ('<p>Class ' + keys[i] + ': ' + values[i] + '</p>')
  }
}

console.log(total)
REPO = REPO.replace('TOTAL', total)
console.log(REPO)

//-- Write total in new html file
fs.writeFileSync('repo1-bien.html', REPO);
