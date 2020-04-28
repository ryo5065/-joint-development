$(function () {
  for (let i = 0; i < 10; i++) {
    // table タグを作成する
    var tableTag = $("<table />");

    var pTag = $("<p/>");

    for (let j = 0; j < 3; j++) {
      // tr タグを作成する
      var trTag = $("<tr />");

      // tr タグの子要素として th タグを追加する
      trTag.append($("<th />").html("サークル"));

      // tr タグの子要素として td タグを追加する

      trTag.append($("<td />").html("twitter"));

      trTag.append($("<td />").html("公式サイト"));

      // tableタグの子要素として 上記で作成した tr タグを追加する
      tableTag.append(trTag);
    }

    // HTMLに定義されているdivタグ内に作成したTABLEタグの内容を追加する
    // $("div[name=div1]").append(pTag.html("サッカー"));
    $("div[name=div1]").append(pTag.html("サッカー"));
    $("div[name=div1]").append(tableTag);
  }

  $("p").css("text-align", "center");
  $("p").css("margin-top", "50px");

  $("table").css("margin-top", "10px");
  $("table").css("width", "100%");
});
