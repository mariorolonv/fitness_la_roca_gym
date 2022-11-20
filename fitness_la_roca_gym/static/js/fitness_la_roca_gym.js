function RemoveMessage() {
    $("#message-success").addClass("d-none");
}
function SelectTotal(e) {
    var total =  e.target.selectedOptions[0].getAttribute("data-total")
    document.getElementById("id_total").value = total;
}
$(document).ready(function()
{
  //Defino los totales de mis columnas en 0
  var total1_col4 = 0;
  var total2_col4 = 0;
  var total3_col4 = 0;
  var total4_col4 = 0;
  var total5_col4 = 0;
  //Recorro todos los tr ubicados en el tbody
  $('#kt_table_users_0 tbody').find('tr').each(function (i, el) {   
        //Voy incrementando las variables segun la fila ( .eq(0) representa la fila 1 )     
        total1_col4 += parseInt($(this).find('td').eq(3).text());       
    });
    $('#kt_table_users_1 tbody').find('tr').each(function (i, el) {     
        total2_col4 += parseInt($(this).find('td').eq(3).text());         
    });
    $('#kt_table_users_2 tbody').find('tr').each(function (i, el) {    
        total3_col4 += parseInt($(this).find('td').eq(3).text());            
    });
    $('#kt_table_users_3 tbody').find('tr').each(function (i, el) {    
        total4_col4 += parseInt($(this).find('td').eq(3).text());      
    });
    $('#kt_table_users_4 tbody').find('tr').each(function (i, el) {    
        total5_col4 += parseInt($(this).find('td').eq(3).text());       
    });
    //Muestro el resultado en el th correspondiente a la columna
    $('#total1-all').text(total1_col4);
    $('#total2-all').text(total2_col4);
    $('#total3-all').text(total3_col4);
    $('#total4-all').text(total4_col4);

});
// var fecha = new Date($('#date-created').val());
// var dias  = 7;
// fecha.setDate(fecha.getDate() + dias);
// console.info(date_created)

$(document).ready(function(){
    var vCurrentDate=new Date($('#date-created').val());
    $('#inpCurrentDate').val(formatDateYMD(vCurrentDate));
    $('#inpEndDate').val(formatDateYMD(sumDays(vCurrentDate, 0)))
});

$(document).ready(function(){
    var vCurrentDate=new Date($('#date-created').val());
    $('#inpCurrentDate').val(formatDateYMD(vCurrentDate));
    $('#inpEndDateW').val(formatDateYMD(sumDays(vCurrentDate, 7)))
});

$(document).ready(function(){
    var vCurrentDate=new Date($('#date-created').val());
    $('#inpCurrentDate').val(formatDateYMD(vCurrentDate));
    $('#inpEndDateF').val(formatDateYMD(sumDays(vCurrentDate, 15)))
});

$(document).ready(function(){
    var vCurrentDate=new Date($('#date-created').val());
    $('#inpCurrentDate').val(formatDateYMD(vCurrentDate));
    $('#inpEndDateM').val(formatDateYMD(sumMonths(vCurrentDate, 1)))
});

function sumDays(pDate, pSumDays) {
    var vDate= new Date(pDate);

    vDate.setDate(vDate.getDate()+pSumDays);
    return vDate;
}

function sumMonths(pDate, pSumMonths) {
    var vDate= new Date(pDate);
    vDate.setMonth(vDate.getMonth()+pSumMonths);
    return vDate;
}

function formatDateYMD(pDate) {
    var vDate = new Date(pDate);
    var vDay = vDate.getDate();
    var vMonth = vDate.getMonth()+1;
    var vYear = vDate.getFullYear();

    vDay=vDay<10? "0"+vDay: vDay;
    vMonth= vMonth<10 ? "0"+vMonth: vMonth;

    return vDay+"-"+vMonth+"-"+vYear;
}
