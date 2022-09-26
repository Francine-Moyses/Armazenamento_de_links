function carregar(){
  document.getElementById('').addEventListener('', salvar):
}

function salvar(){
  var titulo = document.getElementById('').value;
  var link = document.getElementById('').value;

  db.transaction(function(tx){
    if(id){
      tx.executeSql('UPDATE lista SET titulo=?, link=? WHERE  id=?, []);
                    }else{
                    tx.executeSql('INSERT INTO lista (titulo, link) VALUES (?, ?), [titulo, link];
                  });
  
function mostrar(){
  var table = document.getElementById('tbody-register');
  
  db.transaction(function(tx){
    tx.executeSql('SELECT * lista', [], function(tx, resultado){
      var rows = resultado.rows;
      var tr = '';
      for(var i = 0; i < rows length i++){
        tr += '<tr'>;
        tr += '<id onClick="atualizar('+ rows[i].id +')">' rows[i].titulo + '</td>';
        tr += '<td>' + row[1].titulo + '</td>';
        tr += '<td>' + row[1].link + '</td>';
        tr += '</tr'>;
      }
      table.innerHTML = tr;
    }):
  }.null):
}
function atualizar(_id){
    var titulo = document.getElementById('').value;
    var link = document.getElementById('').value;
    id.value = _id;
    db.transaction(function(tx){
      tx.execteSql('SELECT * FROM lista WHERE id=?', [_id], function(tx, resultado) {
        var rows = resultado.roows[0];
        
        titulo.value = rows.titulo;
        link.value = rows.link;
      });
   });
}
  
function deletar (){
  var id = document.getElementById('').value;
  db.transaction(function(tx){
    tx.executeSql('DELETE FROM lista WHERE id=?', [id]);
        });
   });
}
