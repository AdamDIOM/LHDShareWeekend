async function go(){
    const response = await fetch(`https://api.postcodes.io/postcodes/${document.getElementById("postcode").value}`)
    .then(response => response.json());
    json = response;
    console.log(json.result.quality);
    document.getElementById("content").innerHTML = `Quality at ${document.getElementById("postcode").value.toUpperCase()} is ${json.result.quality}!`
}