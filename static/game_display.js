var display = document.getElementById('GameDisplay');
var display_context = display.getContext('2d');

display_context.fillStyle = "red";
display_context.fillRect(15, 25, 75, 75);

function fetchClubs()
{
    fetch('/produce_club/Ygplt7XxflI8gO2')
    .then(function(response)
    {
        return response.text();
    })
    .then(function(html)
    {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, "text/html");
        var js_script = document.createElement("script");

        js_script.setAttribute("src", "/static/show_range_value.js");
        js_script.setAttribute("type", "text/javascript");
        document.head.appendChild(js_script);
        document.getElementById('OptionsDisplay').innerHTML = html;
    })
}

function changeOptionsDisplay(event)
{
    let y = event.offsetX;
    let x = event.offsetY;

    if (y > 15 && y < (15+75) && x > 25 && x < (25+75))
    {
        fetchClubs();
    }
}


document.getElementById('GameDisplay').addEventListener('click', changeOptionsDisplay, false);

