const fs = require('fs')

//-- Read html file
const REPO = fs.readFileSync('repo.html', 'utf-8')

//-- Name of the Json file to read
const JSON_FILE = fs.readFileSync("/home/ana/Documentos/TFG/TFG/DATA_JSON/total_data.json")

//-- Create the store structure from the contents of the file
//-- Return us the json structure
var data = JSON.parse(JSON_FILE);

//-- Get information
//-- Get Repository name
repository = Object.keys(data)
for (repo=0; repo<repository.length; repo++){
  //-- Assign the value of REPO
  let content = REPO
  //-- Variable total
  let total = ''
  total += "<h2> REPOSITORY: " + repository[repo] + "</h2>"
  //-- Get total content
  content_total = data[repository[repo]]

  //-- Get Files names
  files = Object.keys(content_total)

  for (file=0; file<files.length; file++){
    //-- Get name
    name_file = files[file]
    total += '<h3>NAME FILE : ' + name_file + '<h3>'
    let content_file = data[repository[repo]][name_file]

    //-- Get levels
    let levels = content_file["Levels"]
    total += '<h4>LEVELS: <h4>'
    for (i=0; i<Object.keys(levels).length; i++){
      keys = Object.keys(levels);
      values = Object.values(levels);
      total += ('<p>Nivel ' + keys[i] + ': ' + values[i] + '</p>');
    }
    //-- Get classes
    let clase = content_file["Class"]
    total += '<h4>CLASSES: <h4>'
    for (i=0; i<Object.keys(clase).length; i++){
      keys = Object.keys(clase)
      values = Object.values(clase)
      total += ('<p>Class ' + keys[i] + ': ' + values[i] + '</p>')
    }
  }
  content = content.replace('TOTAL', total)
  name_html = (repository[repo] + '.html')

  //-- Write total in new html file
  fs.writeFileSync(name_html, content);
}
