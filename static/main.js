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
    let timeline = document.getElementById("timeline");
    timeline.innerHTML = "";

    let jsonArray = jsonResponse.history;
    let direction = "direction-r";

    for (let i = 0; i < jsonArray.length; i++) {
        let timelineItem = document.createElement("li");
        let directionDiv = document.createElement("div");
        directionDiv.className = direction;

        let flagWrapper = document.createElement("div");
        flagWrapper.className = "flag-wrapper";

        let hexa = document.createElement("span");
        hexa.className = "hexa";
        let timeWrapper = document.createElement("span");
        timeWrapper.className = "time-wrapper";

        let timeSpan = document.createElement("span");
        timeSpan.className = "time";
        timeSpan.innerHTML = jsonArray[i].time;

        timeWrapper.appendChild(timeSpan);

        flagWrapper.appendChild(hexa);
        flagWrapper.appendChild(timeWrapper);

        let description = document.createElement("div");
        description.className = "desc";
        description.innerHTML = jsonArray[i].text;
        description.onclick = function () {
            let xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function () {
                if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
                    let response = JSON.parse(xmlHttp.responseText);
                    alert("Copied to clipboard: " + response.clipboard)
                }
            };
            xmlHttp.open("GET", "http://localhost:8001/api/v1/history/" + i, true);
            xmlHttp.send(null);
        };

        directionDiv.appendChild(flagWrapper);
        directionDiv.appendChild(description);

        timelineItem.appendChild(directionDiv);

        timeline.appendChild(timelineItem);

        if (direction === "direction-r") {
            direction = "direction-l";
        } else {
            direction = "direction-r";
        }
    }
}