$(document).ready(function(){
$(function($){
    $("#form").submit(function(event){
      event.preventDefault();
        $.ajax({
          url: "https://formspree.io/nachofuentes7164@gmail.com"
          method: "POST"
          data: {
            nombre: $("#nombre").val(),
            email: $("#email").val(),
            asunto: $("#asunto").val(),
            mensaje: $("#textarea").val(),
        },
          dataType: "json"
        }).done(function(){
          $("#nombre").val("");
            $("#email").val("");
            $("#asunto").val("");
            $("#textarea").val("");
          $(".formresponse").addClass("text-success").text("Mensaje enviado con éxito")         
        }).fail(function(){
          $(".formresponse").addClass("text-danger").text("Hubo un error en el envío de tu mensaje")
        });
    });
});
    });