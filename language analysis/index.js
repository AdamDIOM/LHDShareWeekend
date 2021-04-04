async function go(){
    const response = await fetch(`https://api.dandelion.eu/datatxt/nex/v1/?lang=en&min_confidence=0&include=image%2Cabstract%2Ctypes%2Ccategories%2Clod&text=${document.getElementById("language").value}&social=False&top_entities=8&country=-1&token=86620aa0fa21496088900e25886b59ee`)
    .then(response => response.json());
    json = response;
    console.log(json.annotations);
    for(annotation in json.annotations){
        theText = "";
        for(str in json.annotations[annotation].categories){
            theText += json.annotations[annotation].categories[str];
            theText += ", ";
        }
        console.log(`${json.annotations[annotation].spot}: ${theText}`);
        document.getElementById("content").innerHTML += `${json.annotations[annotation].spot}: ${theText}<br>`
    }
    //document.getElementById("content").innerHTML = `Quality at ${document.getElementById("language").value.toUpperCase()} is ${json.result.quality}!`
}
