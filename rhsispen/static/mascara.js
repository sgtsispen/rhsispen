var options =  {
    onComplete: function(cep) {
      alert('CEP Completo!:' + cep);
    },
    onKeyPress: function(cep, event, currentField, options){
      console.log('Uma tecla foi pressionada!:', cep, ' Evento: ', event,
                  'Campo atual: ', currentField, ' Opções: ', options);
    },
    onChange: function(cep){
      console.log('cep aceito! ', cep);
    },
    onInvalid: function(val, e, f, invalid, options){
      var error = invalid[0];
      console.log ("Digite: ", error.v, " inválido para a posição: ", error.p, ". Esperamos algo como: ", error.e);
    }
  };
 
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
    django.jQuery('.mask-cep').mask('00000-000', options);
    //django.jQuery('.mask-contato').mask(SPMaskBehavior, spOptions); 

});

function remover_mascaras(form){    
    $(form).find(':input[class*="-mask"]').unmask();
}