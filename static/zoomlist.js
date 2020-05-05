$(function() {
  $(".change-color").click(function(){
    var $click = $(this)
    var $detail = $(this).closest("div").children("tr.hide-details")
if($click.hasClass('open')){
  $click.removeClass('open');
  $click.next().hide();
  $click.find("span").text("+");
}
  else{
    $click.addClass('open');
    $click.next().show();
    $click.find("span").text("-");
}
})
});