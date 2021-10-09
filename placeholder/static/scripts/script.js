$(document).ready(function () { //Vai rodar assim que estiver "Preparado"
    
    $(".loader").hide() // Vai ocutar o loader usando o .hide() assim que a pagina carregar
    
    // Vai pegar o evento click e ignorar o prevent do href
    $(".page-link").on('click', function(e){
        e.preventDefault();
        
        // Vai pegar o atributo do $(this) -> href 
        page = $(this).attr('href')
        
        // Vai pegar o value do input pesquisa
        pesq = $('#search').val()

        $.ajax({
            // Enviar os dados via ajax para a url / (a url atual do usuario)
            url:"/",
            data:'page='+page+'&search='+pesq,
            /*O metodo padrao aqui está como GET, por isso nao foi definido*/
            beforeSend:function(){
                $(".loader").show() // Antes do ajax retornar sucesso, o loader vai aparecer com o .show()
                $("#users_pag").hide() // E ocultar o conteudo antigo antes de aparece o novo com o .hide()
            },
            success:function(res){
                $("#users_pag").html(res) //Renderizar o html (user-list.html) com os dados retornado do backend
                $("#users_pag").show() // Vai revelar o novo conteudo com o .html() renderizado usando o .show()
                $(".loader").hide() // E ocultar o loader novamente com o .hide()
            }
        })
    })
})