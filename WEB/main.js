const fs = require('fs')

//-- Read html file
const REPO = fs.readFileSync('repo.html', 'utf-8')

//-- Read index.html
let INDEX = fs.readFileSync('main.html', 'utf-8')

//-- Name of the Json file to read
const JSON_FILE = fs.readFileSync("/home/ana/Documentos/TFG/TFG/DATA_JSON/total_data.json")
const JSON_FILESUM = fs.readFileSync("/home/ana/Documentos/TFG/TFG/DATA_JSON/summary_data.json")
const JSON_FILEREPO = fs.readFileSync("/home/ana/Documentos/TFG/TFG/DATA_JSON/repo_data.json")

//-- Create the store structure from the contents of the file
//-- Return us the json structure
var data = JSON.parse(JSON_FILE);
var summary = JSON.parse(JSON_FILESUM)
var data_repo = JSON.parse(JSON_FILEREPO)

//-- Variable that is going to have all the buttons available
let button = ''

//-- Get information
//-- Get Repository name
repository = Object.keys(data)

//-- Create a button for each repository
for (i=0; i<repository.length; i++){
  button += "<button role='link'onclick=window.location='" +
            repository[i] + ".html'>Repository " + repository[i]+
            "</button><br><br>" + '\n'
}
INDEX = INDEX.replace('BUTTON', button)
//-- Write total in new html file
fs.writeFileSync('index.html', INDEX);

//-- Obtain information from each repository
for (repo=0; repo<repository.length; repo++){
  //-- Assign the value of REPO
  let content = REPO
  //-- Variable total
  let total = ''
  let name_repo = "<h2> REPOSITORY: " + repository[repo] + "</h2>" + '\n'
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
    total += '<h4>LEVELS: <h4>' + '\n'
    for (i=0; i<Object.keys(levels).length; i++){
      keys = Object.keys(levels);
      values = Object.values(levels);
      total += ('<p>Levels ' + keys[i] + ': ' + values[i] + '</p>' + '\n');
    }
    //-- Get classes
    let clase = content_file["Class"]
    total += '<h4>CLASSES: <h4> ' + '\n'
    for (i=0; i<Object.keys(clase).length; i++){
      keys = Object.keys(clase)
      values = Object.values(clase)
      total += ('<p>Class ' + keys[i] + ': ' + values[i] + '</p>' + '\n')
    }
  }
  total_repo = repo_summary()
  content = content.replace('REPO', name_repo)
  content = content.replace('TOTAL', total)
  content = content.replace('SUMMARY', total_repo)

  name_html = (repository[repo] + '.html')


  //-- Write total in new html file
  fs.writeFileSync(name_html, content);
}

function repo_summary(){
  //-- Obtain repository summary information
  repos = Object.keys(data_repo)
  //console.log(repo)
  for(i=0; i<repos.length;i++){
    let total_repo = '';
    repo_name = repos[i]
    content = data_repo[repo_name]


    for(elem=0; elem<Object.keys(content).length; elem++){
      keys = Object.keys(content);
      values = Object.values(content);
      if (elem==0){
        total_repo += ('<h4>LEVELS: <h4>' + '\n');
      }else{
        total_repo += ('<h4>CLASSES: <h4>' + '\n');
      }
      for (value=0; value<Object.keys(values[elem]).length; value++){
        key = Object.keys(values[elem])[value];
        val =Object.values(values[elem])[value];
        total_repo += ('<p>' + keys[elem] + ' ' + key + ': ' + val +
                       '</p>' + '\n');
      }
    }
    return(total_repo)
  }
}

//-- Obtain summary information
let total_summary = ''
type = Object.keys(summary)
for (i=0; i<type.length; i++){
  key = type[i] //-- Levels or Class
  total_summary += '<h4>' + key.toUpperCase() + ':<h4> ' + '\n'
  content = summary[key]
  for(elem=0; elem<Object.keys(content).length; elem++){
    keys = Object.keys(content)
    values = Object.values(content)
    total_summary += ('<p>' + key + ' ' + keys[elem] + ': ' + values[elem] +
                      '</p>' + '\n')
  }
}
//console.log(total_summary)
INDEX = INDEX.replace('SUMMARY', total_summary)
//-- Write total in new html file
fs.writeFileSync('index.html', INDEX);