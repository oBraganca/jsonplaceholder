$(document).ready(function () { //Vai rodar os scripts assim que estiver "Preparado"

    pesq = '' // Inicializa a variavel pesq
    
    $('#search').bind('keyup', function(event){
        // Pega o evento keyup
        if (pesq != $(this).val()){
            // Se o a variavel pesq for diferente de value, vai fazer a requisição ajax
            pesq = $(this).val()
            $.ajax({
                url:"/",
                data:'search='+pesq,
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
        }
    })
})