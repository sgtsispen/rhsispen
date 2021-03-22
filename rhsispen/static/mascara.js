
var SPMaskBehavior = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
  };
  
$(function(){
  django.jQuery('.mask-cpf').mask('000.000.000-00', {reverse: true});
  django.jQuery('.mask-dt_nasc').mask('00/00/0000'); 
  django.jQuery('.mask-cep').mask('00000-000');
  //django.jQuery('.mask-contato').mask(SPMaskBehavior, spOptions); 
  //ANTES DE SALVAR NO BD, DEVE-SE TIRAR O MASK DAS LINHAS
  django.jQuery('#servidor_form').submit(function(){
      django.jQuery('#servidor_form').find(":input[class='mask-cpf']").unmask();
      django.jQuery('#servidor_form').find(":input[class='mask-cep']").unmask();
    });
});







 


function remover_mascaras(form){    
    $(form).find(':input[class*="-mask"]').unmask();
}
