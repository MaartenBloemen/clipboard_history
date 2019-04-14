function getClipboardHistory() {
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
            let response = JSON.parse(xmlHttp.responseText);

            fillTimeLine(response);
        }
    };
    xmlHttp.open("GET", "http://localhost:8001/api/v1/history", true);
    xmlHttp.send(null);
}

function fillTimeLine(jsonResponse) {
    let timeline = document.getElementById('timeline');
    timeline.innerHTML = "";

    let jsonArray = jsonResponse.history;
    let direction = "direction-r";

    for(let i = 0; i < jsonArray.length; i++) {
    let timelineItem = '<li><div class="'+direction+'"><div class="flag-wrapper"><span class="hexa"></span><span class="time-wrapper"><span class="time">'+jsonArray[i].time+'</span></span></div><div class="desc">'+jsonArray[i].text+'</div></div></li>';
    console.log(timelineItem);
    let doc = new DOMParser().parseFromString(timelineItem, "text/xml");
    timeline.appendChild(doc.documentElement);

    if (direction === 'direction-r') {
        direction = "direction-l";
    } else {
        direction = "direction-r";
    }
  }
}