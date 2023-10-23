var token = "427183ced61d8617d46c0f97a1674c876176fe5e";

var type  = "ADDRESS";
var $region = $("#region");
var $city   = $("#city");
var $street = $("#street");
var $house  = $("#house");

// регион и район
$region.suggestions({
  token: token,
  type: type,
  hint: false,
  bounds: "region-area"
});

// город и населенный пункт
$city.suggestions({
  token: token,
  type: type,
  hint: false,
  bounds: "city-settlement",
  constraints: $region
});

// улица
$street.suggestions({
  token: token,
  type: type,
  hint: false,
  bounds: "street",
  constraints: $city,
  count: 15
});

// дом
$house.suggestions({
  token: token,
  type: type,
  hint: false,
  noSuggestionsHint: false,
  bounds: "house",
  constraints: $street
});


console.log($house.suggestions())