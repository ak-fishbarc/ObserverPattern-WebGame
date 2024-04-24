// Get data from the server (html) from "event" attribute of element "news".
// Then display that in the browser.
news = document.getElementById("news");
news_to_parse = news.getAttribute("event");

document.body.innerHTML = news_to_parse;